Blockly.defineBlocksWithJsonArray(
    [
        {
            "type": "light_forced",
            "message0": "light.forced.Event %1",
            "args0": [
                {
                    "type": "field_dropdown",
                    "name": "event",
                    "options": [
                        [
                            "On",
                            "On"
                        ],
                        [
                            "Off",
                            "Off"
                        ]
                    ]
                }
            ],
            "previousStatement": "home.Event",
            "nextStatement": "home.Event",
            "colour": 205,
            "tooltip": "",
            "helpUrl": ""
        },
         {
            "type": "light_brightness",
            "message0": "light.brightness %1 %",
            "args0": [
                {
                    "type": "field_number",
                    "name": "int",
                    "value": 50,
                    "min": 0,
                    "max": 100,
                    "precision": 1
                }
            ],
            "previousStatement": "home.Event",
            "nextStatement": "home.Event",
            "colour": 205,
            "tooltip": "",
            "helpUrl": ""
        },
         {
            "type": "light_circadian_rhythm_brightness",
            "message0": "light.circadian_rhythm.brightness %1 %",
            "args0": [
                {
                    "type": "field_number",
                    "name": "int",
                    "value": 50,
                    "min": 0,
                    "max": 100,
                    "precision": 1
                }
            ],
            "previousStatement": "home.Event",
            "nextStatement": "home.Event",
            "colour": 205,
            "tooltip": "",
            "helpUrl": ""
        },
         {
            "type": "light_lux_balancing_brightness",
            "message0": "light.lux_balancing.brightness %1 %",
            "args0": [
                {
                    "type": "field_number",
                    "name": "int",
                    "value": 50,
                    "min": 0,
                    "max": 100,
                    "precision": 1
                }
            ],
            "previousStatement": "home.Event",
            "nextStatement": "home.Event",
            "colour": 205,
            "tooltip": "",
            "helpUrl": ""
        },
         {
            "type": "light_show_starting_brightness",
            "message0": "light.show.starting_brightness %1 %",
            "args0": [
                {
                    "type": "field_number",
                    "name": "int",
                    "value": 50,
                    "min": 0,
                    "max": 100,
                    "precision": 1
                }
            ],
            "previousStatement": "home.Event",
            "nextStatement": "home.Event",
            "colour": 205,
            "tooltip": "",
            "helpUrl": ""
        },
         {
            "type": "light_show_ending_brightness",
            "message0": "light.show.ending_brightness %1 %",
            "args0": [
                {
                    "type": "field_number",
                    "name": "int",
                    "value": 50,
                    "min": 0,
                    "max": 100,
                    "precision": 1
                }
            ],
            "previousStatement": "home.Event",
            "nextStatement": "home.Event",
            "colour": 205,
            "tooltip": "",
            "helpUrl": ""
        },
         {
            "type": "light_saturation",
            "message0": "light.saturation %1",
            "args0": [
                {
                    "type": "field_number",
                    "name": "int",
                    "value": 50,
                    "min": 0,
                    "max": 100,
                    "precision": 1
                }
            ],
            "previousStatement": "home.Event",
            "nextStatement": "home.Event",
            "colour": 205,
            "tooltip": "",
            "helpUrl": ""
        },
         {
            "type": "light_circadian_rhythm_saturation",
            "message0": "light.circadian_rhythm.saturation %1",
            "args0": [
                {
                    "type": "field_number",
                    "name": "int",
                    "value": 50,
                    "min": 0,
                    "max": 100,
                    "precision": 1
                }
            ],
            "previousStatement": "home.Event",
            "nextStatement": "home.Event",
            "colour": 205,
            "tooltip": "",
            "helpUrl": ""
        },
          {
            "type": "light_temperature",
            "message0": "light.temperature %1 kelvin",
            "args0": [
                {
                    "type": "field_number",
                    "name": "int",
                    "value": 3500,
                    "precision": 1
                }
            ],
            "previousStatement": "home.Event",
            "nextStatement": "home.Event",
            "colour": 205,
            "tooltip": "",
            "helpUrl": ""
        },
          {
            "type": "light_circadian_rhythm_temperature",
            "message0": "light.circadian_rhythm.temperature %1 kelvin",
            "args0": [
                {
                    "type": "field_number",
                    "name": "int",
                    "value": 3500,
                    "precision": 1
                }
            ],
            "previousStatement": "home.Event",
            "nextStatement": "home.Event",
            "colour": 205,
            "tooltip": "",
            "helpUrl": ""
        },
          {
            "type": "light_hue",
            "message0": "light.hue %1",
            "args0": [
                {
                    "type": "field_number",
                    "name": "int",
                    "value": 205,
                    "min": 0,
                    "max": 360,
                    "precision": 1
                }
            ],
            "previousStatement": "home.Event",
            "nextStatement": "home.Event",
            "colour": 205,
            "tooltip": "",
            "helpUrl": ""
        },
          {
            "type": "light_circadian_rhythm_hue",
            "message0": "light.circadian_rhythm.hue %1",
            "args0": [
                {
                    "type": "field_number",
                    "name": "int",
                    "value": 205,
                    "min": 0,
                    "max": 360,
                    "precision": 1
                }
            ],
            "previousStatement": "home.Event",
            "nextStatement": "home.Event",
            "colour": 205,
            "tooltip": "",
            "helpUrl": ""
        },
        {
            "type": "light_show_starting_hue",
            "message0": "light.show.starting_hue %1",
            "args0": [
                {
                    "type": "field_number",
                    "name": "int",
                    "value": 205,
                    "min": 0,
                    "max": 360,
                    "precision": 1
                }
            ],
            "previousStatement": "home.Event",
            "nextStatement": "home.Event",
            "colour": 205,
            "tooltip": "",
            "helpUrl": ""
        },
        {
            "type": "light_show_ending_hue",
            "message0": "light.show.ending_hue %1",
            "args0": [
                {
                    "type": "field_number",
                    "name": "int",
                    "value": 205,
                    "min": 0,
                    "max": 360,
                    "precision": 1
                }
            ],
            "previousStatement": "home.Event",
            "nextStatement": "home.Event",
            "colour": 205,
            "tooltip": "",
            "helpUrl": ""
        },
        {
            "type": "light_show_cycles",
            "message0": "light.show.cycles %1",
            "args0": [
                {
                    "type": "field_number",
                    "name": "int",
                    "value": 100,
                    "precision": 1
                }
            ],
            "previousStatement": "home.Event",
            "nextStatement": "home.Event",
            "colour": 205,
            "tooltip": "",
            "helpUrl": ""
        },
        {
            "type": "light_show_period",
            "message0": "light.show.period %1 milliseconds",
            "args0": [
                {
                    "type": "field_number",
                    "name": "int",
                    "value": 60000,
                    "precision": 1
                }
            ],
            "previousStatement": "home.Event",
            "nextStatement": "home.Event",
            "colour": 205,
            "tooltip": "",
            "helpUrl": ""
        },
    ])