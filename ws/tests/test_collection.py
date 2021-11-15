import unittest
from aiohttp.test_utils import unittest_run_loop
from ws.tests.testcase import MyHomeTestCase


class CollectionTestCase(MyHomeTestCase):
    @unittest_run_loop
    async def test_get(self):
        for collection in self.app.resources.appliances:
            request = await self.client.request(
                "GET", "/collection/{}".format(collection)
            )
            assert request.status == 200
            text = await request.text()
            for appliance in self.app.resources.appliances[collection]:
                assert appliance.name in text


if __name__ == "__main__":
    unittest.main()
