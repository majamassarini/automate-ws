import unittest
from aiohttp.test_utils import unittest_run_loop
from ws.tests.testcase import MyHomeTestCase


class ApplianceTestCase(MyHomeTestCase):
    @unittest_run_loop
    async def test_get(self):
        for collection in self.app.resources.appliances:
            for appliance in self.app.resources.appliances[collection]:
                request = await self.client.request(
                    "GET",
                    "/appliance/{}/graphs".format(appliance.name.replace(" ", "%20")),
                )
                assert request.status == 200
                text = await request.text()
                assert appliance.name in text


if __name__ == "__main__":
    unittest.main()
