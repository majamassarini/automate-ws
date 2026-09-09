#!/usr/bin/env python3
"""Field test server for automate-ws.

Starts a real aiohttp server using fixture appliance data from
ws/tests/project/appliances.yaml, with cookie-based sessions so no
external Redis is needed.

Run from the repo root:
    python field_test/server.py

Or via make:
    make field-test

Then visit http://localhost:8080

Default credentials (from ws/authorization.py):
    admin / admin  — view + edit + configure
    user  / user   — view + edit
"""

import logging
import os
import pathlib
import sys

from aiohttp import web
from aiohttp_security import SessionIdentityPolicy
from aiohttp_security import setup as setup_security
from aiohttp_session import SimpleCookieStorage
from aiohttp_session import setup as setup_session
import aiohttp_jinja2
import jinja2

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import ws  # noqa: E402 — must come after sys.path update
from ws.tests.testcase import Resources  # noqa: E402

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
)
logging.getLogger("ws").setLevel(logging.DEBUG)


async def make_app() -> web.Application:
    app = web.Application()

    # Cookie-based sessions — no Redis required
    setup_session(app, SimpleCookieStorage())

    # Security
    policy = SessionIdentityPolicy()
    brain_policy = ws.authorization.Policy()
    setup_security(app, policy, brain_policy)
    app["credentials"] = brain_policy.credentials

    # Fixture appliances from ws/tests/project/
    resources = Resources(None, None, "ws", "brain")

    websocket_handler = ws.handler.websocket.Handler(resources)
    on_redis_msg = ws.OnRedisMsg(websocket_handler, resources)
    resources.redis_gateway.run(
        on_redis_msg.on_appliance_updated,
        on_redis_msg.on_performer_updated,
    )
    app.on_shutdown.append(websocket_handler.on_shutdown)

    ws.routes.setup(app, resources, websocket_handler)

    app.add_routes([web.static("/static", str(ROOT / "ws" / "static"))])
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.FileSystemLoader(str(ROOT / "ws" / "templates")),
    )
    from ws.__main__ import make_loki_url

    loki_base = os.environ.get("LOKI_BASE_URL", "")
    loki_uid = os.environ.get("LOKI_DATASOURCE_UID", "")
    aiohttp_jinja2.get_env(app).globals["loki_base_url"] = loki_base
    aiohttp_jinja2.get_env(app).globals["loki_datasource_uid"] = loki_uid
    aiohttp_jinja2.get_env(app).globals["make_loki_url"] = make_loki_url

    return app


if __name__ == "__main__":
    print()
    print("  automate-ws field test server")
    print("  ─────────────────────────────")
    print("  URL  : http://localhost:8080")
    print("  Login: admin / admin  (full access)")
    print("         user  / user   (view + edit)")
    print()
    web.run_app(make_app(), host="0.0.0.0", port=8080)
