import unittest
from aiohttp.test_utils import unittest_run_loop
from ws.tests.testcase import MyHomeTestCase


class CollectionsTestCase(MyHomeTestCase):
    @unittest_run_loop
    async def test_get(self):
        request = await self.client.request("GET", "/collections")
        assert request.status == 200
        text = await request.text()
        for collection in self.app.resources.appliances:
            for appliance in self.app.resources.appliances[collection]:
                assert appliance.name.replace(" ", "-") in text


if __name__ == "__main__":
    unittest.main()
