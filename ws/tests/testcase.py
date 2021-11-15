import os
import copy
import pathlib
import aiohttp_jinja2
import jinja2
import logging
import home
import ws

from aiohttp.test_utils import AioHTTPTestCase
from aiohttp import web


LOGGER_NAME = "ws tests"


class RedisGatewayStub:
    def run(self, _, __):
        pass

    async def update(self, appliance):
        logging.getLogger(__name__).warning("update {}".format(appliance))

    async def save(self, appliance):
        logging.getLogger(__name__).warning("save {}".format(appliance))

    async def notify(self, appliance):
        logging.getLogger(__name__).warning("notify {}".format(appliance))

    async def get_history(self, appliance, num_of_events):
        history = list()
        for i in range(0, num_of_events):
            a = copy.deepcopy(appliance)
            if i == 1:
                a.notify(home.appliance.light.event.forced.event.Event.On)
            history.append((i, a))
        return history


class Resources(home.builder.listener.Resources):
    def __init__(self, redis_host, redis_port, my_node_name, other_nodes_names):
        from ws.tests import testcase  # noqa

        yaml_dir = os.path.join(
            pathlib.Path(testcase.__file__).resolve().parent, "project"
        )
        super(Resources, self).__init__(
            yaml_dir, redis_host, redis_port, my_node_name, other_nodes_names
        )
        self._redis_gateway = RedisGatewayStub()
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.websockets = []


class MyHomeTestCase(AioHTTPTestCase):
    def get_app(self):
        app = web.Application()
        resources = Resources(None, None, "ws", "brain")
        app.resources = resources
        websocket_handler = ws.handler.websocket.Handler(resources)
        app.on_shutdown.append(websocket_handler.on_shutdown)

        on_redis_msg = ws.OnRedisMsg(websocket_handler, resources)
        resources.redis_gateway.run(
            on_redis_msg.on_appliance_updated, on_redis_msg.on_performer_updated
        )

        graphs_handler = ws.handler.graphs.Handler(resources, None, None)

        ws.routes.setup(app, resources, websocket_handler, graphs_handler)
        app.add_routes(
            [
                web.static(
                    "/static", os.path.join(os.path.dirname(__file__), "../static")
                )
            ]
        )
        aiohttp_jinja2.setup(
            app,
            loader=jinja2.FileSystemLoader(
                os.path.join(os.path.dirname(__file__), "../templates")
            ),
        )

        return app
