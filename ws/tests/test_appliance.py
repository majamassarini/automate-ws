import unittest
from ws.tests.testcase import AuthenticatedTestCase, MyHomeTestCase


class ApplianceGetTestCase(MyHomeTestCase):
    async def test_get(self):
        for collection in self.app.resources.appliances:
            for appliance in self.app.resources.appliances[collection]:
                request = await self.client.request(
                    "GET",
                    "/appliance/{}".format(appliance.name.replace(" ", "%20")),
                )
                assert request.status == 200
                text = await request.text()
                assert appliance.name in text


class AppliancePostTestCase(AuthenticatedTestCase):
    async def test_post(self):
        request = await self.client.request(
            "POST",
            "/appliance/simple%20light",
            data={
                "module": "home.appliance.light.event.forced",
                "klass": "Event",
                "value": "Off",
            },
        )
        assert request.status == 200
        text = await request.text()
        assert "simple light" in text
        assert "Off" in text

    async def test_post_unknown_event_returns_400(self):
        request = await self.client.request(
            "POST",
            "/appliance/simple%20light",
            data={
                "module": "os",
                "klass": "system",
                "value": "x",
            },
        )
        assert request.status == 400


if __name__ == "__main__":
    unittest.main()
