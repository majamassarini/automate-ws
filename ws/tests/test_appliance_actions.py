"""HTTP-level tests for the appliance action endpoints:

- POST /appliance/{name}/apply_to_collection
- POST /appliance/{name}/apply_to_others
- POST /appliance/{name}/enable
- POST /appliance/{name}/send_to_collection
- POST /appliance/{name}/send_to_others
- GET  /appliance/{name}/send_modal
- POST /appliance/{name}/send_to_selected
"""

import unittest
from ws.tests.testcase import AuthenticatedTestCase

_MODULE = "home.appliance.light.event.forced"
_KLASS = "Event"
_LIGHT = "simple%20light"


class ApplyToCollectionTestCase(AuthenticatedTestCase):
    async def test_post_enable(self):
        r = await self.client.request(
            "POST",
            f"/appliance/{_LIGHT}/apply_to_collection",
            data={"module": _MODULE, "klass": _KLASS, "value": "true"},
        )
        self.assertEqual(r.status, 200)

    async def test_post_disable(self):
        r = await self.client.request(
            "POST",
            f"/appliance/{_LIGHT}/apply_to_collection",
            data={"module": _MODULE, "klass": _KLASS, "value": "false"},
        )
        self.assertEqual(r.status, 200)


class ApplyToOthersTestCase(AuthenticatedTestCase):
    async def test_post_enable(self):
        r = await self.client.request(
            "POST",
            f"/appliance/{_LIGHT}/apply_to_others",
            data={"module": _MODULE, "klass": _KLASS, "value": "true"},
        )
        self.assertEqual(r.status, 200)

    async def test_post_disable(self):
        r = await self.client.request(
            "POST",
            f"/appliance/{_LIGHT}/apply_to_others",
            data={"module": _MODULE, "klass": _KLASS, "value": "false"},
        )
        self.assertEqual(r.status, 200)


class EnableTestCase(AuthenticatedTestCase):
    async def test_post_enable(self):
        r = await self.client.request(
            "POST",
            f"/appliance/{_LIGHT}/enable",
            data={"module": _MODULE, "klass": _KLASS, "value": "true"},
        )
        self.assertEqual(r.status, 200)

    async def test_post_disable(self):
        r = await self.client.request(
            "POST",
            f"/appliance/{_LIGHT}/enable",
            data={"module": _MODULE, "klass": _KLASS, "value": "false"},
        )
        self.assertEqual(r.status, 200)


class SendToCollectionTestCase(AuthenticatedTestCase):
    async def test_post(self):
        r = await self.client.request(
            "POST",
            f"/appliance/{_LIGHT}/send_to_collection",
            data={"module": _MODULE, "klass": _KLASS},
        )
        self.assertEqual(r.status, 200)


class SendToOthersTestCase(AuthenticatedTestCase):
    async def test_post(self):
        r = await self.client.request(
            "POST",
            f"/appliance/{_LIGHT}/send_to_others",
            data={"module": _MODULE, "klass": _KLASS},
        )
        self.assertEqual(r.status, 200)


class SendModalTestCase(AuthenticatedTestCase):
    async def test_get(self):
        r = await self.client.request(
            "GET",
            f"/appliance/{_LIGHT}/send_modal",
            params={"module": _MODULE, "klass": _KLASS},
        )
        self.assertEqual(r.status, 200)


class SendToSelectedTestCase(AuthenticatedTestCase):
    async def test_post_send_value(self):
        r = await self.client.request(
            "POST",
            f"/appliance/{_LIGHT}/send_to_selected",
            data={
                "module": _MODULE,
                "klass": _KLASS,
                "send_type": "send_value",
                "appliance_name": "simple light",
            },
        )
        self.assertEqual(r.status, 200)

    async def test_post_send_enabled(self):
        r = await self.client.request(
            "POST",
            f"/appliance/{_LIGHT}/send_to_selected",
            data={
                "module": _MODULE,
                "klass": _KLASS,
                "send_type": "send_enabled",
                "appliance_name": "simple light",
            },
        )
        self.assertEqual(r.status, 200)

    async def test_post_no_selected(self):
        r = await self.client.request(
            "POST",
            f"/appliance/{_LIGHT}/send_to_selected",
            data={
                "module": _MODULE,
                "klass": _KLASS,
                "send_type": "send_value",
            },
        )
        self.assertEqual(r.status, 200)


if __name__ == "__main__":
    unittest.main()
