Blockly.defineBlocksWithJsonArray(
    [
        {
            "type": "protocol_triggers",
            "message0": "triggers %1 %2",
            "args0": [
                {
                    "type": "input_dummy"
                },
                {
                    "type": "input_statement",
                    "name": "protocol_trigger",
                    "check": "protocol.Trigger"
                }
            ],
            "inputsInline": true,
            "output": "protocol.Triggers",
            "colour": 215,
            "tooltip": "",
            "helpUrl": ""
        },
        {
            "type": "protocol_commands",
            "message0": "commands %1 %2",
            "args0": [
                {
                    "type": "input_dummy"
                },
                {
                    "type": "input_statement",
                    "name": "protocol_command",
                    "check": "protocol.Command"
                }
            ],
            "output": "protocol.Commands",
            "colour": 225,
            "tooltip": "",
            "helpUrl": ""
        },
        {
            "type": "appliance_socket_presence_socket",
            "message0": "%1 %2 %3 socket.presence.Appliance %4 " +
                "socket.forced.Event.On %5 %6 socket.forced.Event.Off %7 %8 " +
                "event.presence.Event.On %9 %10 event.presence.Event.Off %11 %12 " +
                "%13",
            "args0": [
                {
                    "type": "field_input",
                    "name": "name",
                    "text": "socket name"
                },
                {
                    "type": "field_input",
                    "name": "collection",
                    "text": "collection name"
                },
                {
                    "type": "input_dummy",
                    "align": "LEFT"
                },
                {
                    "type": "input_dummy",
                    "align": "LEFT"
                },
                {
                    "type": "input_value",
                    "name": "forced_on",
                    "check": "protocol.Triggers",
                    "align": "RIGHT"
                },
                {
                    "type": "input_statement",
                    "name": "forced_on_schedulers",
                    "check": "scheduler.Trigger"
                },
                {
                    "type": "input_value",
                    "name": "forced_off",
                    "check": "protocol.Triggers",
                    "align": "RIGHT"
                },
                {
                    "type": "input_statement",
                    "name": "forced_off_schedulers",
                    "check": "scheduler.Trigger"
                },
                {
                    "type": "input_value",
                    "name": "presence_on",
                    "check": "protocol.Triggers",
                    "align": "RIGHT"
                },
                {
                    "type": "input_statement",
                    "name": "presence_on_schedulers",
                    "check": "scheduler.Trigger"
                },
                {
                    "type": "input_value",
                    "name": "presence_off",
                    "check": "protocol.Triggers",
                    "align": "RIGHT"
                },
                {
                    "type": "input_statement",
                    "name": "presence_off_schedulers",
                    "check": "scheduler.Trigger"
                },
                {
                    "type": "input_value",
                    "name": "state",
                    "check": "protocol.Commands",
                    "align": "RIGHT"
                }
            ],
            "inputsInline": false,
            "colour": 220,
            "tooltip": "",
            "helpUrl": ""
        },
        {
            "type": "appliance_curtain_outdoor_curtain",
            "message0": "%1 %2 %3 curtain.outdoor.Appliance %4 " +
                "curtain.forced.Event.Opened %5 %6 curtain.forced.Event.Closed %7 %8 " +
                "event.wind.Event.Weak %9 %10 event.wind.Event.Strong %11 %12 " +
                "event.sun.brightness.Bright %13 %14 event.sun.brightness.Dark %15 %16 event.sun.brightness.DeepDark %17 %18 " +
                "event.sun.twilight.civil.Event.Sunrise %19 %20 event.sun.twilight.civil.Event.Sunset %21 %22 " +
                "event.sun.hit.Event.Sunhit %23 %24 event.sun.hit.Event.Sunleft %25 %26 " +
                "%27",
            "args0": [
                {
                    "type": "field_input",
                    "name": "name",
                    "text": "socket name"
                },
                {
                    "type": "field_input",
                    "name": "collection",
                    "text": "collection name"
                },
                {
                    "type": "input_dummy",
                    "align": "LEFT"
                },
                {
                    "type": "input_dummy",
                    "align": "LEFT"
                },
                {
                    "type": "input_value",
                    "name": "forced_opened",
                    "check": "protocol.Triggers",
                    "align": "RIGHT"
                },
                {
                    "type": "input_statement",
                    "name": "forced_opened_schedulers",
                    "check": "scheduler.Trigger"
                },
                {
                    "type": "input_value",
                    "name": "forced_closed",
                    "check": "protocol.Triggers",
                    "align": "RIGHT"
                },
                {
                    "type": "input_statement",
                    "name": "forced_closed_schedulers",
                    "check": "scheduler.Trigger"
                },
                {
                    "type": "input_value",
                    "name": "wind_weak",
                    "check": "protocol.Triggers",
                    "align": "RIGHT"
                },
                {
                    "type": "input_statement",
                    "name": "wind_weak_schedulers",
                    "check": "scheduler.Trigger"
                },
                {
                    "type": "input_value",
                    "name": "wind_strong",
                    "check": "protocol.Triggers",
                    "align": "RIGHT"
                },
                {
                    "type": "input_statement",
                    "name": "wind_strong_schedulers",
                    "check": "scheduler.Trigger"
                },
                {
                    "type": "input_value",
                    "name": "sun_brightness_bright",
                    "check": "protocol.Triggers",
                    "align": "RIGHT"
                },
                {
                    "type": "input_statement",
                    "name": "sun_brightness_bright_schedulers",
                    "check": "scheduler.Trigger"
                },
                {
                    "type": "input_value",
                    "name": "sun_brightness_dark",
                    "check": "protocol.Triggers",
                    "align": "RIGHT"
                },
                {
                    "type": "input_statement",
                    "name": "sun_brightness_dark_schedulers",
                    "check": "scheduler.Trigger"
                },
                {
                    "type": "input_value",
                    "name": "sun_brightness_deepdark",
                    "check": "protocol.Triggers",
                    "align": "RIGHT"
                },
                {
                    "type": "input_statement",
                    "name": "sun_brightness_deepdark_schedulers",
                    "check": "scheduler.Trigger"
                },
                {
                    "type": "input_value",
                    "name": "sun_twilight_sunrise",
                    "check": "protocol.Triggers",
                    "align": "RIGHT"
                },
                {
                    "type": "input_statement",
                    "name": "sun_twilight_sunrise_schedulers",
                    "check": "scheduler.Trigger"
                },
                {
                    "type": "input_value",
                    "name": "sun_twilight_sunset",
                    "check": "protocol.Triggers",
                    "align": "RIGHT"
                },
                {
                    "type": "input_statement",
                    "name": "sun_twilight_sunset_schedulers",
                    "check": "scheduler.Trigger"
                },
                {
                    "type": "input_value",
                    "name": "sun_hit_sunhit",
                    "check": "protocol.Triggers",
                    "align": "RIGHT"
                },
                {
                    "type": "input_statement",
                    "name": "sun_hit_sunhit_schedulers",
                    "check": "scheduler.Trigger"
                },
                {
                    "type": "input_value",
                    "name": "sun_hit_sunleft",
                    "check": "protocol.Triggers",
                    "align": "RIGHT"
                },
                {
                    "type": "input_statement",
                    "name": "sun_hit_sunleft_schedulers",
                    "check": "scheduler.Trigger"
                },
                {
                    "type": "input_value",
                    "name": "state",
                    "check": "protocol.Commands",
                    "align": "RIGHT"
                }
            ],
            "inputsInline": false,
            "colour": 220,
            "tooltip": "",
            "helpUrl": ""
        },
        {
            "type": "appliance_sensor_alarm",
            "message0": "%1 %2 %3 sensor.alarm.Appliance %4 " +
                "event.alarm.armed.Event.On %5 %6 event.alarm.armed.Event.Off %7 %8 " +
                "event.alarm.triggered.Event.On %9 %10 event.alarm.triggered.Event.Off %11 %12 " +
                "%13",
            "args0": [
                {
                    "type": "field_input",
                    "name": "name",
                    "text": "sensor name"
                },
                {
                    "type": "field_input",
                    "name": "collection",
                    "text": "collection name"
                },
                {
                    "type": "input_dummy",
                    "align": "LEFT"
                },
                {
                    "type": "input_dummy",
                    "align": "LEFT"
                },
                {
                    "type": "input_value",
                    "name": "alarm_armed_on",
                    "check": "protocol.Triggers",
                    "align": "RIGHT"
                },
                {
                    "type": "input_statement",
                    "name": "armed_on_schedulers",
                    "check": "scheduler.Trigger"
                },
                {
                    "type": "input_value",
                    "name": "alarm_armed_off",
                    "check": "protocol.Triggers",
                    "align": "RIGHT"
                },
                {
                    "type": "input_statement",
                    "name": "armed_off_schedulers",
                    "check": "scheduler.Trigger"
                },
                {
                    "type": "input_value",
                    "name": "alarm_triggered_on",
                    "check": "protocol.Triggers",
                    "align": "RIGHT"
                },
                {
                    "type": "input_statement",
                    "name": "triggered_on_schedulers",
                    "check": "scheduler.Trigger"
                },
                {
                    "type": "input_value",
                    "name": "alarm_triggered_off",
                    "check": "protocol.Triggers",
                    "align": "RIGHT"
                },
                {
                    "type": "input_statement",
                    "name": "triggered_off_schedulers",
                    "check": "scheduler.Trigger"
                },
                {
                    "type": "input_value",
                    "name": "state",
                    "check": "protocol.Commands",
                    "align": "RIGHT"
                }
            ],
            "inputsInline": false,
            "colour": 220,
            "tooltip": "",
            "helpUrl": ""
        },
        {
            "type": "appliance_sensor_lux",
            "message0": "%1 %2 %3 sensor.luxmeter.Appliance %4 lux %5 %6 %7",
            "args0": [
                {
                    "type": "field_input",
                    "name": "name",
                    "text": "sensor name"
                },
                {
                    "type": "field_input",
                    "name": "collection",
                    "text": "collection name"
                },
                {
                    "type": "input_dummy",
                    "align": "LEFT"
                },
                {
                    "type": "input_dummy",
                    "align": "LEFT"
                },
                {
                    "type": "input_value",
                    "name": "lux",
                    "check": "protocol.Triggers",
                    "align": "RIGHT"
                },
                {
                    "type": "input_statement",
                    "name": "lux_schedulers",
                    "check": "scheduler.Trigger"
                },
                {
                    "type": "input_value",
                    "name": "state",
                    "check": "protocol.Commands",
                    "align": "RIGHT"
                }
            ],
            "inputsInline": false,
            "colour": 220,
            "tooltip": "",
            "helpUrl": ""
        },
        {
            "type": "appliance_sensor_anemometer",
            "message0": "%1 %2 %3 sensor.anemometer.Appliance %4 wind %5 %6 %7",
            "args0": [
                {
                    "type": "field_input",
                    "name": "name",
                    "text": "sensor name"
                },
                {
                    "type": "field_input",
                    "name": "collection",
                    "text": "collection name"
                },
                {
                    "type": "input_dummy",
                    "align": "LEFT"
                },
                {
                    "type": "input_dummy",
                    "align": "LEFT"
                },
                {
                    "type": "input_value",
                    "name": "wind",
                    "check": "protocol.Triggers",
                    "align": "RIGHT"
                },
                {
                    "type": "input_statement",
                    "name": "wind_schedulers",
                    "check": "scheduler.Trigger"
                },
                {
                    "type": "input_value",
                    "name": "state",
                    "check": "protocol.Commands",
                    "align": "RIGHT"
                }
            ],
            "inputsInline": false,
            "colour": 220,
            "tooltip": "",
            "helpUrl": ""
        },
    ])