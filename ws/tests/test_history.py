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

    async def test_duration_shown(self):
        request = await self.client.request(
            "GET", "/appliance/simple%20light/history"
        )
        text = await request.text()
        # Stub produces entries 1 second apart so duration "1s" appears
        assert "1s" in text

    async def test_filter_today(self):
        request = await self.client.request(
            "GET", "/appliance/simple%20light/history?filter=today"
        )
        assert request.status == 200

    async def test_filter_yesterday(self):
        request = await self.client.request(
            "GET", "/appliance/simple%20light/history?filter=yesterday"
        )
        assert request.status == 200

    async def test_filter_custom_date_range(self):
        request = await self.client.request(
            "GET",
            "/appliance/simple%20light/history"
            "?filter=custom&from_date=2020-01-01&to_date=2020-01-31",
        )
        assert request.status == 200


if __name__ == "__main__":
    unittest.main()
