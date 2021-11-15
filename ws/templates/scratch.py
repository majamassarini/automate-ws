from typing import NamedTuple, Iterable

import home
import knx_plugin
import knx_stack


class ApplianceInfo(NamedTuple):
    appliance: "home.Appliance"
    collection: str


class PerformerTriggerInfo(NamedTuple):
    appliance: str
    performer: "home.Performer"


class PerformerCommandInfo(NamedTuple):
    appliance: str
    performer: "home.Performer"


class SchedulerInfo(NamedTuple):
    appliances: Iterable[str]
    triggers: Iterable["home.scheduler.Trigger"]


class Blockly(home.MyHome):
    def __init__(
        self,
        appliances: Iterable[ApplianceInfo],
        trigger_performers: Iterable[PerformerTriggerInfo],
        command_performers: Iterable[PerformerCommandInfo],
        scheduler: Iterable[SchedulerInfo],
    ):
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
                appliance_command_performers[appliance_name] = list(
                    [
                        performer,
                    ]
                )

        for appliance_names, scheduler_triggers_ in self.__scheduler:
            for appliance_name in appliance_names:
                schedule_infos.append(
                    (appliance_command_performers[appliance_name], scheduler_triggers_)
                )
        return schedule_infos


appliances = list()
trigger_performers = list()
command_performers = list()
scheduler = list()

appliance = home.appliance.socket.presence.Appliance("pippo", [])
appliances.append(ApplianceInfo(appliance, "da modificare"))
forced_on_performer = home.Performer(
    "trigger forced on for pippo",
    appliance,
    [],
    (
        [
            knx_plugin.trigger.dpt_switch.On.make(
                (
                    [
                        knx_stack.GroupAddress(free_style=0),
                    ]
                ),
                [
                    home.appliance.socket.event.forced.Event.On,
                ],
            ),
        ]
    ),
)
trigger_performers.append(PerformerTriggerInfo("pippo", forced_on_performer))
forced_off_performer = home.Performer(
    "trigger forced off for pippo",
    appliance,
    [],
    (
        [
            knx_plugin.trigger.dpt_switch.Off.make(
                (
                    [
                        knx_stack.GroupAddress(free_style=0),
                    ]
                ),
                [
                    home.appliance.socket.event.forced.Event.Off,
                ],
            ),
        ]
    ),
)
trigger_performers.append(PerformerTriggerInfo("pippo", forced_off_performer))
command_performer = home.Performer(
    "commands for pippo",
    appliance,
    (
        [
            knx_plugin.command.dpt_switch.OnOff.make(
                (
                    [
                        knx_stack.GroupAddress(free_style=0),
                    ]
                )
            ),
        ]
    ),
    [],
)
command_performers.append(PerformerCommandInfo("pippo", command_performer))

appliance = home.appliance.sensor.alarm.Appliance("pluto", [])
appliances.append(ApplianceInfo(appliance, "da modificare"))
armed_on_performer = home.Performer(
    "trigger armed on for pluto",
    appliance,
    [],
    (
        [
            knx_plugin.trigger.dpt_switch.On.make(
                (
                    [
                        knx_stack.GroupAddress(free_style=0),
                    ]
                ),
                [
                    home.event.alarm.armed.Event.On,
                ],
            ),
        ]
    ),
)
trigger_performers.append(PerformerTriggerInfo("pluto", armed_on_performer))
armed_off_performer = home.Performer(
    "trigger armed off for pluto",
    appliance,
    [],
    (
        [
            knx_plugin.trigger.dpt_switch.Off.make(
                (
                    [
                        knx_stack.GroupAddress(free_style=0),
                    ]
                ),
                [
                    home.event.alarm.armed.Event.Off,
                ],
            ),
        ]
    ),
)
trigger_performers.append(PerformerTriggerInfo("pluto", armed_off_performer))
triggered_on_performer = home.Performer(
    "trigger armed on for pluto",
    appliance,
    [],
    (
        [
            knx_plugin.trigger.dpt_switch.On.make(
                (
                    [
                        knx_stack.GroupAddress(free_style=0),
                    ]
                ),
                [
                    home.event.alarm.triggered.Event.On,
                ],
            ),
        ]
    ),
)
trigger_performers.append(PerformerTriggerInfo("pluto", triggered_on_performer))
triggered_off_performer = home.Performer(
    "trigger armed off for pluto",
    appliance,
    [],
    (
        [
            knx_plugin.trigger.dpt_switch.Off.make(
                (
                    [
                        knx_stack.GroupAddress(free_style=0),
                    ]
                ),
                [
                    home.event.alarm.triggered.Event.Off,
                ],
            ),
        ]
    ),
)
trigger_performers.append(PerformerTriggerInfo("pluto", triggered_off_performer))
command_performer = home.Performer(
    "commands for pluto",
    appliance,
    (
        [
            knx_plugin.command.dpt_switch.OnOff.make(
                (
                    [
                        knx_stack.GroupAddress(free_style=0),
                    ]
                )
            ),
        ]
    ),
    [],
)
command_performers.append(PerformerCommandInfo("pluto", command_performer))
scheduler_triggers = list()
for protocol_trigger in armed_on_performer.triggers:
    scheduler_triggers.append(
        home.scheduler.trigger.protocol.Trigger(
            name="scheduler protocol trigger alarm armed on (pluto)",
            events=[home.event.presence.Event.On],
            protocol_trigger=protocol_trigger,
        )
    )
scheduler.append(
    SchedulerInfo(
        [
            "pippo",
        ],
        scheduler_triggers,
    )
)
scheduler_triggers = list()
for protocol_trigger in armed_off_performer.triggers:
    scheduler_triggers.append(
        home.scheduler.trigger.protocol.Trigger(
            name="scheduler protocol trigger alarm armed off (pluto)",
            events=[home.event.presence.Event.Off],
            protocol_trigger=protocol_trigger,
        )
    )
scheduler.append(
    SchedulerInfo(
        [
            "pippo",
        ],
        scheduler_triggers,
    )
)
scheduler_triggers = list()
for protocol_trigger in triggered_on_performer.triggers:
    scheduler_triggers.append(
        home.scheduler.trigger.protocol.Trigger(
            name="scheduler protocol trigger alarm triggered on (pluto)",
            events=[home.event.presence.Event.On],
            protocol_trigger=protocol_trigger,
        )
    )
scheduler.append(
    SchedulerInfo(
        [
            "pippo",
        ],
        scheduler_triggers,
    )
)
scheduler_triggers = list()
for protocol_trigger in triggered_off_performer.triggers:
    scheduler_triggers.append(
        home.scheduler.trigger.protocol.Trigger(
            name="scheduler protocol trigger alarm triggered off (pluto)",
            events=[home.event.presence.Event.Off],
            protocol_trigger=protocol_trigger,
        )
    )
scheduler.append(
    SchedulerInfo(
        [
            "pippo",
        ],
        scheduler_triggers,
    )
)


blockly_builder = Blockly(appliances, trigger_performers, command_performers, scheduler)
