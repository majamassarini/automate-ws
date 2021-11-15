import json
import aiohttp
import aiohttp_jinja2

from urllib.parse import parse_qsl  # noqa
from multidict import MultiDict  # noqa


from ws.handler.appliance import Handler as Parent

START = """
from typing import NamedTuple, Iterable

import home
import knx_plugin
import knx_stack


class ApplianceInfo(NamedTuple):
    appliance: 'home.Appliance'
    collection: str


class PerformerTriggerInfo(NamedTuple):
    appliance: str
    performer: 'home.Performer'


class PerformerCommandInfo(NamedTuple):
    appliance: str
    performer: 'home.Performer'


class SchedulerInfo(NamedTuple):
    appliances: Iterable[str]
    triggers: Iterable['home.scheduler.Trigger']


class Blockly(home.MyHome):

    def __init__(self, appliances: Iterable[ApplianceInfo],
                 trigger_performers: Iterable[PerformerTriggerInfo],
                 command_performers: Iterable[PerformerCommandInfo],
                 scheduler: Iterable[SchedulerInfo]):
        self.__appliances = appliances
        self.__trigger_performers = trigger_performers
        self.__command_performers = command_performers
        self.__scheduler = scheduler
        super(Blockly, self).__init__()

    def _build_appliances(self):
        collection = home.appliance.Collection()
        for appliance_, collection_name in self.__appliances:
            if collection_name in collection:
                collection[collection_name].add(appliance_)
            else:
                collection[collection_name] = set([appliance_])
        return collection

    def _build_performers(self):
        performers = list()
        for _, performer in self.__trigger_performers:
            performers.append(performer)
        for _, performer in self.__command_performers:
            performers.append(performer)
        return performers

    def _build_group_of_performers(self):
        return {}

    def _build_scheduler_triggers(self):
        triggers = list()
        for _, triggers_ in self.__scheduler:
            triggers.extend(triggers_)
        return triggers

    def _build_schedule_infos(self):
        schedule_infos = list()
        appliance_command_performers = {}
        for appliance_name, performer in self.__command_performers:
            if appliance_name in appliance_command_performers:
                appliance_command_performers[appliance_name].append(performer)
            else:
                appliance_command_performers[appliance_name] = list([performer, ])

        for appliance_names, scheduler_triggers_ in self.__scheduler:
            for appliance_name in appliance_names:
                schedule_infos.append((appliance_command_performers[appliance_name], scheduler_triggers_))
        return schedule_infos


appliances = list()
trigger_performers = list()
command_performers = list()
scheduler = list()

"""

END = """
my_home = Blockly(appliances, trigger_performers, command_performers, scheduler)
"""


class Handler(Parent):

    ENCODING = "utf-8"

    @aiohttp_jinja2.template("editor.html")
    async def get(self, request):
        user = await self.get_user(request)
        return {"user": user}

    async def post(self, request):
        request_data = await request.post()
        try:
            xml = request_data["xml"]
        except KeyError:
            xml = None
        if xml:
            with open("/tmp/workspace.xml", "w") as fd:
                fd.write(xml)
            return aiohttp.web.Response()
        else:
            try:
                code = request_data["code"]
                with open("/tmp/workspace.py", "w") as fd:
                    fd.write(START)
                    fd.write(code)
                    fd.write(END)
                return aiohttp.web.Response()
            except KeyError:
                with open("/tmp/workspace.xml", "r") as fd:
                    xml_text = fd.read()
                return aiohttp.web.Response(
                    body=json.dumps(xml_text).encode(self.ENCODING),
                    content_type="application/json",
                )
