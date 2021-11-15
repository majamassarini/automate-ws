Blockly.defineBlocksWithJsonArray(
    [
        {
            "type": "appliance_name",
            "message0": "appliance %1",
            "args0": [
                {
                    "type": "field_input",
                    "name": "name",
                    "text": "name"
                }
            ],
            "previousStatement": "appliance.Name",
            "nextStatement": "appliance.Name",
            "colour": 205,
            "tooltip": "",
            "helpUrl": ""
        },
        {
            "type": "scheduler_trigger",
            "message0": "scheduler trigger (protocol trigger) %1 events: %2 for %3",
            "args0": [
                {
                    "type": "input_dummy"
                },
                {
                    "type": "input_statement",
                    "name": "events",
                    "check": "home.Event",
                    "align": "RIGHT"
                },
                {
                    "type": "input_statement",
                    "name": "appliance_name",
                    "check": "appliance.Name",
                    "align": "RIGHT"
                }
            ],
            "inputsInline": false,
            "previousStatement": "scheduler.Trigger",
            "nextStatement": "scheduler.Trigger",
            "colour": 205,
            "tooltip": "",
            "helpUrl": ""
        },
        {
            "type": "scheduler_trigger_delay",
            "message0": "scheduler trigger (delay protocol trigger) %1 events: %2 for %3 %4 delay %5",
            "args0": [
                {
                    "type": "input_dummy"
                },
                {
                    "type": "input_statement",
                    "name": "events",
                    "check": "home.Event",
                    "align": "RIGHT"
                },
                {
                    "type": "input_statement",
                    "name": "appliance_name",
                    "check": "appliance.Name",
                    "align": "RIGHT"
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "field_number",
                    "name": "delay",
                    "value": 1,
                    "precision": 0.01
                }
            ],
            "inputsInline": false,
            "previousStatement": "scheduler.Trigger",
            "nextStatement": "scheduler.Trigger",
            "colour": 205,
            "tooltip": "",
            "helpUrl": ""
        },
        {
            "type": "scheduler_trigger_sunrise",
            "message0": "%1 (sunrise) %2 events: [home.event.sun.phase.Sunrise, ] %3 + %4 for %5 at %6 latitude %7 %8 longitude %9 %10 elevation %11",
            "args0": [
                {
                    "type": "field_input",
                    "name": "name",
                    "text": "scheduler trigger"
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "input_statement",
                    "name": "events",
                    "check": "home.Event",
                    "align": "RIGHT"
                },
                {
                    "type": "input_statement",
                    "name": "appliance_name",
                    "check": "appliance.Name",
                    "align": "RIGHT"
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "field_number",
                    "name": "latitude",
                    "value": 45.22,
                    "precision": 0.01
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "field_number",
                    "name": "longitude",
                    "value": 13.33,
                    "precision": 0.01
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "field_number",
                    "name": "elevation",
                    "value": 100,
                    "precision": 1
                }
            ],
            "inputsInline": false,
            "colour": 205,
            "tooltip": "",
            "helpUrl": ""
        },
        {
            "type": "scheduler_trigger_sunset",
            "message0": "%1 (sunset) %2 events: [home.event.sun.phase.Sunset, ] %3 + %4 for %5 at %6 latitude %7 %8 longitude %9 %10 elevation %11",
            "args0": [
                {
                    "type": "field_input",
                    "name": "name",
                    "text": "scheduler trigger"
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "input_statement",
                    "name": "events",
                    "check": "home.Event",
                    "align": "RIGHT"
                },
                {
                    "type": "input_statement",
                    "name": "appliance_name",
                    "check": "appliance.Name",
                    "align": "RIGHT"
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "field_number",
                    "name": "latitude",
                    "value": 45.22,
                    "precision": 0.01
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "field_number",
                    "name": "longitude",
                    "value": 13.33,
                    "precision": 0.01
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "field_number",
                    "name": "elevation",
                    "value": 100,
                    "precision": 1
                }
            ],
            "inputsInline": false,
            "colour": 205,
            "tooltip": "",
            "helpUrl": ""
        },
        {
            "type": "scheduler_trigger_sunhit",
            "message0": "%1 (sunhit) %2 events: [home.event.sun.hit.Sunhit, ] %3 + %4 " +
                "for %5 " +
                "at %6 latitude %7 %8 longitude %9 %10 elevation %11 %12" +
                "bottom altitude %13 %14" +
                "upper altitude %15 %16" +
                "min azimuth %17 %18" +
                "max azimuth %19",
            "args0": [
                {
                    "type": "field_input",
                    "name": "name",
                    "text": "scheduler trigger"
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "input_statement",
                    "name": "events",
                    "check": "home.Event",
                    "align": "RIGHT"
                },
                {
                    "type": "input_statement",
                    "name": "appliance_name",
                    "check": "appliance.Name",
                    "align": "RIGHT"
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "field_number",
                    "name": "latitude",
                    "value": 45.22,
                    "precision": 0.01
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "field_number",
                    "name": "longitude",
                    "value": 13.33,
                    "precision": 0.01
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "field_number",
                    "name": "elevation",
                    "value": 100,
                    "precision": 1
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "field_number",
                    "name": "bottom_altitude",
                    "value": 100,
                    "precision": 1
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "field_number",
                    "name": "upper_altitude",
                    "value": 200,
                    "precision": 1
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "field_number",
                    "name": "min_azimuth",
                    "value": 100,
                    "precision": 1
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "field_number",
                    "name": "max_azimuth",
                    "value": 100,
                    "precision": 1
                }
            ],
            "inputsInline": false,
            "colour": 205,
            "tooltip": "",
            "helpUrl": ""
        },
        {
            "type": "scheduler_trigger_sunleft",
            "message0": "%1 (sunleft) %2 events: [home.event.sun.hit.Sunleft, ] %3 + %4 " +
                "for %5 " +
                "at %6 latitude %7 %8 longitude %9 %10 elevation %11 %12" +
                "bottom altitude %13 %14" +
                "upper altitude %15 %16" +
                "min azimuth %17 %18" +
                "max azimuth %19",
            "args0": [
                {
                    "type": "field_input",
                    "name": "name",
                    "text": "scheduler trigger"
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "input_statement",
                    "name": "events",
                    "check": "home.Event",
                    "align": "RIGHT"
                },
                {
                    "type": "input_statement",
                    "name": "appliance_name",
                    "check": "appliance.Name",
                    "align": "RIGHT"
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "field_number",
                    "name": "latitude",
                    "value": 45.22,
                    "precision": 0.01
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "field_number",
                    "name": "longitude",
                    "value": 13.33,
                    "precision": 0.01
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "field_number",
                    "name": "elevation",
                    "value": 100,
                    "precision": 1
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "field_number",
                    "name": "bottom_altitude",
                    "value": 100,
                    "precision": 1
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "field_number",
                    "name": "upper_altitude",
                    "value": 200,
                    "precision": 1
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "field_number",
                    "name": "min_azimuth",
                    "value": 100,
                    "precision": 1
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "field_number",
                    "name": "max_azimuth",
                    "value": 100,
                    "precision": 1
                }
            ],
            "inputsInline": false,
            "colour": 205,
            "tooltip": "",
            "helpUrl": ""
        },
        {
            "type": "scheduler_trigger_cron",
            "message0": "%1 (cron) %2 events: [ ] %3 + %4 for %5 when %6 year %7 %8 month %9 %10 day %11 %12 week %13 %14 day_of_week %15 %16 hour %17 %18 minute %19 %20 start_date %21 %22 end_date %23",
            "args0": [
                {
                    "type": "field_input",
                    "name": "name",
                    "text": "scheduler trigger"
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "input_statement",
                    "name": "events",
                    "check": "home.Event",
                    "align": "RIGHT"
                },
                {
                    "type": "input_statement",
                    "name": "appliance_name",
                    "check": "appliance.Name"
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "field_input",
                    "name": "year",
                    "text": ""
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "field_input",
                    "name": "month",
                    "text": ""
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "field_input",
                    "name": "day",
                    "text": ""
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "field_input",
                    "name": "week",
                    "text": ""
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "field_input",
                    "name": "day_of_week",
                    "text": ""
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "field_input",
                    "name": "hour",
                    "text": ""
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "field_input",
                    "name": "minute",
                    "text": ""
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "field_input",
                    "name": "start_date",
                    "text": ""
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "field_input",
                    "name": "end_date",
                    "text": ""
                }
            ],
            "colour": 205,
            "tooltip": "",
            "helpUrl": ""
        }
    ])