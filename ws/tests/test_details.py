import unittest
from ws.tests.testcase import MyHomeTestCase


class DetailsTestCase(MyHomeTestCase):
    async def test_get(self):
        for collection in self.app.resources.appliances:
            for appliance in self.app.resources.appliances[collection]:
                url = "/appliance/{}/details".format(
                    appliance.name.replace(" ", "%20")
                )
                request = await self.client.request("GET", url)
                assert request.status == 200
                text = await request.text()
                assert appliance.name in text

    async def test_protocol_trigger_shows_performer_name(self):
        """Protocol trigger details include the name of the triggering performer."""
        from ws.handler.details import Handler

        resources = self.app.resources
        handler = Handler(resources)

        found = False
        for collection in resources.appliances:
            for appliance in resources.appliances[collection]:
                performers = handler.get_performers(appliance)
                _, all_group_performers = handler.get_group_of_performers(
                    appliance
                )
                reactive, scheduled = handler.get_scheduler_triggers(
                    all_group_performers, performers
                )
                for entry in reactive + scheduled:
                    for detail in entry["details"]:
                        if detail["label"] in (
                            "Triggered by performer",
                            "Triggered by (A+)",
                        ):
                            found = True
                            break
                    if found:
                        break
                if found:
                    break
            if found:
                break

        assert (
            found
        ), "No 'Triggered by performer' detail found in any appliance"


if __name__ == "__main__":
    unittest.main()
