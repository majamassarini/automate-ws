#!/usr/bin/env python3

import logging.config
import os
import sys
import time

from aiohttp import web
from aiohttp_session import setup as setup_session, get_session
from aiohttp_session.redis_storage import RedisStorage
from aiohttp_security import setup as setup_security
from aiohttp_security import SessionIdentityPolicy
import aiohttp_jinja2
import jinja2
import asyncio

import redis.asyncio as aioredis

import home
import ws

sys.path.append("..")


async def handler(request: web.Request) -> web.Response:
    session = await get_session(request)
    last_visit = session["last_visit"] if "last_visit" in session else None
    session["last_visit"] = time.time()
    text = "Last visited: {}".format(last_visit)
    return web.Response(text=text)


class Resources(home.builder.listener.Resources):
    def __init__(
        self, yaml_dir, redis_host, redis_port, my_node_name, other_nodes_names
    ):
        super(Resources, self).__init__(
            yaml_dir, redis_host, redis_port, my_node_name, other_nodes_names
        )
        self.websockets = []


if __name__ == "__main__":
    (options, _) = home.options.parser().parse_args()
    if options.configuration_file:
        options = home.configs.parse(vars(options), options.configuration_file)

    if options.knx_usbhid or options.knxnet_ip:
        import knx_plugin
    if options.lifx:
        import lifx_plugin
    if options.sonos:
        import soco_plugin
    if options.somfy_sdn:
        import somfy_sdn_plugin
    if options.home_assistant:
        import home_assistant_plugin

    configuration = ws.conf.default_logging_configuration(
        options.logging_dir, logging_level=options.webserver_logging_level
    )
    logging.config.dictConfig(configuration)

    async def main() -> web.Application:
        app = web.Application()

        # session setup
        redis_client = aioredis.Redis(
            host=options.redis_host,
            port=int(options.redis_port),
        )
        storage = RedisStorage(redis_client)
        setup_session(app, storage)

        async def dispose_redis(application: web.Application) -> None:
            await redis_client.close()

        app.on_cleanup.append(dispose_redis)

        # security setup
        policy = SessionIdentityPolicy()
        brain_policy = ws.authorization.Policy()
        setup_security(app, policy, brain_policy)
        app["credentials"] = brain_policy.credentials

        resources = Resources(
            options.project_dir,
            options.redis_host,
            options.redis_port,
            options.webserver_node_name,
            options.webserver_other_nodes_names,
        )
        websocket_handler = ws.handler.websocket.Handler(resources)
        if options.graphite_feeder:
            graphs_handler = ws.handler.graphs.Handler(
                resources,
                options.graphite_feeder_server_host,
                options.graphite_feeder_server_port,
            )
        else:
            graphs_handler = None

        on_redis_msg = ws.OnRedisMsg(websocket_handler, resources)
        await resources.redis_gateway.connect()
        resources.redis_gateway.create_tasks(
            asyncio.get_running_loop(),
            on_redis_msg.on_appliance_updated,
            on_redis_msg.on_performer_updated,
        )
        app.on_shutdown.append(websocket_handler.on_shutdown)

        ws.routes.setup(app, resources, websocket_handler, graphs_handler)
        app.add_routes(
            [
                web.static(
                    "/static",
                    os.path.join(options.webserver_dir, "static"),
                )
            ]
        )
        app.add_routes(
            [
                web.static(
                    "/configuration",
                    options.project_dir,
                    show_index=True,
                )
            ]
        )
        app.add_routes(
            [web.static("/logs", options.logging_dir, show_index=True)]
        )

        aiohttp_jinja2.setup(
            app,
            loader=jinja2.FileSystemLoader(
                os.path.join(options.webserver_dir, "templates")
            ),
        )

        return app

    web.run_app(main(), host="0.0.0.0", port=int(options.webserver_port))
