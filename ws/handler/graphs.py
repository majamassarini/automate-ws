import aiohttp_jinja2
from tzlocal import get_localzone

import graphite_feeder
from ws.handler import Handler as Parent


class Handler(Parent):

    DEFAULT_FROM_NUMBER = "24"
    DEFAULT_FROM_UNIT = "h"

    def __init__(self, home_resources, graphite_host, graphite_port):
        super(Handler, self).__init__(home_resources)
        self._graphite_host = graphite_host
        self._graphite_port = graphite_port
        self._timezone = get_localzone()
        self._url = (
            "http://{graphite_host}:{graphite_port}/render?{targets}"
            "&format=png"
            "&tz={timezone}"
            "&width=1200"
            "&height=100"
            "&bgcolor=white"
            "&fgcolor=black"
            "&fontBold=True"
        )
        self._url2 = (
            "http://{graphite_host}:{graphite_port}/render?{targets}"
            "&format=png"
            "&tz={timezone}"
            "&width=640"
            "&height=480"
            "&bgcolor=white"
            "&fgcolor=black"
            "&fontBold=True"
        )

    async def get_graph_urls(
        self, base_url, appliance, from_number=None, from_unit=None
    ):
        urls = list()
        targets = list()
        handler = graphite_feeder.handler.appliance.registry.mapper[appliance.__class__]
        try:
            targets = handler(self._home_resources, appliance, from_number, from_unit)
        except TypeError:
            self._logger.warning("handler {} not mapped".format(handler))

        for target in targets:
            url = base_url.format(
                targets=target,
                graphite_host=self._graphite_host,
                graphite_port=self._graphite_port,
                timezone=self._timezone,
            )
            urls.append(url)
        return urls

    async def _get_response_data(
        self, request, appliance, from_number=None, from_unit=None
    ):
        graph_urls = await self.get_graph_urls(
            self._url, appliance, from_number, from_unit
        )
        graph_urls_modal = await self.get_graph_urls(
            self._url2, appliance, from_number, from_unit
        )
        collection = self._home_resources.appliances.collection_for(appliance)
        collection_url = request.app.router["collection"].url_for(name=collection)
        graphs_url = request.app.router["graphs"].url_for(name=appliance.name)
        user = await self.get_user(request)
        return {
            "user": user,
            "appliance": appliance,
            "id": self.get_html_id(appliance.name),
            "appliance_uri": request.app.router["appliance"].url_for(
                name=appliance.name
            ),
            "collection_url": collection_url,
            "collection": collection,
            "graph_urls": graph_urls,
            "graph_urls_modal": graph_urls_modal,
            "graphs_url": graphs_url,
            "from_number": from_number,
            "units": {"h": "hours", "d": "days", "m": "months"},
            "selected_unit": from_unit,
        }

    @aiohttp_jinja2.template("graphs.html")
    async def get(self, request):
        appliance = await self.get_appliance(request)
        response_data = await self._get_response_data(request, appliance)
        return response_data

    @aiohttp_jinja2.template("graphs.html")
    async def post(self, request):
        request_data = await request.post()
        from_number = request_data["from-number"]
        from_unit = request_data["from-unit"]
        appliance = await self.get_appliance(request)
        response_data = await self._get_response_data(
            request, appliance, from_number, from_unit
        )
        return response_data
