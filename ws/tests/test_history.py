import unittest
from ws.tests.testcase import MyHomeTestCase


class ApplianceTestCase(MyHomeTestCase):
    async def test_get(self):
        request = await self.client.request(
            "GET", "/appliance/simple%20light/history"
        )
        assert request.status == 200
        text = await request.text()
        assert "Forced On" in text
        assert "Off" in text


if __name__ == "__main__":
    unittest.main()
