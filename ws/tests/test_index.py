import unittest
from ws.tests.testcase import MyHomeTestCase


class CollectionsTestCase(MyHomeTestCase):
    async def test_get(self):
        request = await self.client.request("GET", "/")
        assert request.status == 200
        text = await request.text()
        assert "simple light" in text


if __name__ == "__main__":
    unittest.main()
