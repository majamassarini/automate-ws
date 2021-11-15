Blockly.defineBlocksWithJsonArray(
    [
        {
            "type": "knx_free_address",
            "lastDummyAlign0": "RIGHT",
            "message0": "0x %1",
            "args0": [
                {
                    "type": "field_number",
                    "name": "address",
                    "value": 0,
                    "min": 0,
                    "max": 65536,
                    "precision": 1
                }
            ],
            "previousStatement": "knx.Address",
            "nextStatement": "knx.Address",
            "colour": 275,
            "tooltip": "",
            "helpUrl": ""
        },
        {
            "type": "knx_two_level_address",
            "lastDummyAlign0": "RIGHT",
            "message0": "%1 / %2",
            "args0": [
                {
                    "type": "field_number",
                    "name": "main",
                    "value": 0,
                    "min": 0,
                    "max": 32,
                    "precision": 1
                },
                {
                    "type": "field_number",
                    "name": "sub",
                    "value": 0,
                    "min": 0,
                    "max": 2048,
                    "precision": 1
                }
            ],
            "previousStatement": "knx.Address",
            "nextStatement": "knx.Address",
            "colour": 275,
            "tooltip": "",
            "helpUrl": ""
        },
        {
            "type": "knx_three_level_address",
            "lastDummyAlign0": "RIGHT",
            "message0": "%1 / %2 / %3",
            "args0": [
                {
                    "type": "field_number",
                    "name": "main",
                    "value": 0,
                    "min": 0,
                    "max": 32,
                    "precision": 1
                },
                {
                    "type": "field_number",
                    "name": "middle",
                    "value": 0,
                    "min": 0,
                    "max": 8,
                    "precision": 1
                },
                {
                    "type": "field_number",
                    "name": "sub",
                    "value": 0,
                    "min": 0,
                    "max": 256,
                    "precision": 1
                }
            ],
            "previousStatement": "knx.Address",
            "nextStatement": "knx.Address",
            "colour": 275,
            "tooltip": "",
            "helpUrl": ""
        },
        {
            "type": "knx_addresses",
            "message0": "addresses %1 %2",
            "args0": [
                {
                    "type": "input_dummy"
                },
                {
                    "type": "input_statement",
                    "name": "addresses",
                    "check": "knx.Address"
                }
            ],
            "inputsInline": true,
            "output": "knx.Addresses",
            "colour": 275,
            "tooltip": "",
            "helpUrl": ""
        },
        {
            "type": "knx_plugin_trigger_dpt_switch_on",
            "message0": "events: [] %1 when equal %2 DPT_Switch.On %3",
            "args0": [
                {
                    "type": "input_dummy"
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "input_value",
                    "name": "addresses",
                    "check": "knx.Addresses",
                    "align": "RIGHT"
                }
            ],
            "previousStatement": "protocol.Trigger",
            "nextStatement": "protocol.Trigger",
            "colour": 280,
            "tooltip": "",
            "helpUrl": ""
        },
        {
            "type": "knx_plugin_trigger_dpt_switch_off",
            "message0": "events: [] %1 when equal %2 DPT_Switch.Off %3",
            "args0": [
                {
                    "type": "input_dummy"
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "input_value",
                    "name": "addresses",
                    "check": "knx.Addresses",
                    "align": "RIGHT"
                }
            ],
            "previousStatement": "protocol.Trigger",
            "nextStatement": "protocol.Trigger",
            "colour": 280,
            "tooltip": "",
            "helpUrl": ""
        },
        {
            "type": "knx_plugin_trigger_dpt_updown_opened",
            "message0": "events: [] %1 when equal %2 DPT_UpDown.Up %3",
            "args0": [
                {
                    "type": "input_dummy"
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "input_value",
                    "name": "addresses",
                    "check": "knx.Addresses",
                    "align": "RIGHT"
                }
            ],
            "previousStatement": "protocol.Trigger",
            "nextStatement": "protocol.Trigger",
            "colour": 280,
            "tooltip": "",
            "helpUrl": ""
        },
        {
            "type": "knx_plugin_trigger_dpt_updown_closed",
            "message0": "events: [] %1 when equal %2 DPT_UpDown.Down %3",
            "args0": [
                {
                    "type": "input_dummy"
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "input_value",
                    "name": "addresses",
                    "check": "knx.Addresses",
                    "align": "RIGHT"
                }
            ],
            "previousStatement": "protocol.Trigger",
            "nextStatement": "protocol.Trigger",
            "colour": 280,
            "tooltip": "",
            "helpUrl": ""
        },
        {
            "type": "knx_plugin_trigger_dpt_value_lux_always",
            "message0": "events: [float, ] %1 when read %2 DPT_Value_Lux %3",
            "args0": [
                {
                    "type": "input_dummy"
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "input_value",
                    "name": "addresses",
                    "check": "knx.Addresses",
                    "align": "RIGHT"
                }
            ],
            "previousStatement": "protocol.Trigger",
            "nextStatement": "protocol.Trigger",
            "colour": 280,
            "tooltip": "",
            "helpUrl": ""
        },
        {
            "type": "knx_plugin_trigger_dpt_value_wsp_always",
            "message0": "events: [float, ] %1 when read %2 DPT_Value_Wsp %3",
            "args0": [
                {
                    "type": "input_dummy"
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "input_value",
                    "name": "addresses",
                    "check": "knx.Addresses",
                    "align": "RIGHT"
                }
            ],
            "previousStatement": "protocol.Trigger",
            "nextStatement": "protocol.Trigger",
            "colour": 280,
            "tooltip": "",
            "helpUrl": ""
        },
        {
            "type": "knx_plugin_trigger_dpt_value_lux_bright",
            "message0": "events: [home.event.sun.brightness.Bright, ] %1 when mean(value) > %2 lux %3 with %4 samples %5 DPT_Value_Lux %6",
            "args0": [
                {
                    "type": "input_dummy"
                },
                {   "type": "field_number",
                    "name": "value",
                    "value": 45000,
                    "precision": 1
                },
                {
                    "type": "input_dummy"
                },
                {   "type": "field_number",
                    "name": "samples",
                    "value": 50,
                    "precision": 1
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "input_value",
                    "name": "addresses",
                    "check": "knx.Addresses",
                    "align": "RIGHT"
                },
            ],
            "previousStatement": "protocol.Trigger",
            "nextStatement": "protocol.Trigger",
            "colour": 280,
            "tooltip": "",
            "helpUrl": ""
        },
        {
            "type": "knx_plugin_trigger_dpt_value_lux_dark",
            "message0": "events: [home.event.sun.brightness.Dark, ] %1 when deepdark = %2lux %3 and deepdark < mean(value) < deepdark + %4lux %5 with %6 samples %7 DPT_Value_Lux %8",
            "args0": [
                {
                    "type": "input_dummy"
                },
                {"type": "field_number",
                    "name": "value",
                    "value": 4000,
                    "precision": 1
                },
                {
                    "type": "input_dummy"
                },
                {"type": "field_number",
                    "name": "range",
                    "value": 15000,
                    "precision": 1
                },
                {
                    "type": "input_dummy"
                },
                {"type": "field_number",
                    "name": "samples",
                    "value": 50,
                    "precision": 1
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "input_value",
                    "name": "addresses",
                    "check": "knx.Addresses",
                    "align": "RIGHT"
                },
            ],
            "previousStatement": "protocol.Trigger",
            "nextStatement": "protocol.Trigger",
            "colour": 280,
            "tooltip": "",
            "helpUrl": ""
        },
        {
            "type": "knx_plugin_trigger_dpt_value_lux_deepdark",
            "message0": "events: [home.event.sun.brightness.DeepDark, ] %1 if mean(value) < %2lux %3 with %4 samples %5 DPT_Value_Lux %6",
            "args0": [
                {
                    "type": "input_dummy"
                },
                {"type": "field_number",
                    "name": "value",
                    "value": 4000,
                    "precision": 1
                },
                {
                    "type": "input_dummy"
                },
                {"type": "field_number",
                    "name": "samples",
                    "value": 50,
                    "precision": 1
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "input_value",
                    "name": "addresses",
                    "check": "knx.Addresses",
                    "align": "RIGHT"
                },
            ],
            "previousStatement": "protocol.Trigger",
            "nextStatement": "protocol.Trigger",
            "colour": 280,
            "tooltip": "",
            "helpUrl": ""
        },
        {
            "type": "knx_plugin_trigger_dpt_value_wsp_strong",
            "message0": "events: [home.event.wind.Strong, ] %1 when value > %2wsp %3 DPT_Value_Wsp %4",
            "args0": [
                {
                    "type": "input_dummy"
                },
                {"type": "field_number",
                    "name": "value",
                    "value": 4.00,
                    "precision": .01
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "input_value",
                    "name": "addresses",
                    "check": "knx.Addresses",
                    "align": "RIGHT"
                },
            ],
            "previousStatement": "protocol.Trigger",
            "nextStatement": "protocol.Trigger",
            "colour": 280,
            "tooltip": "",
            "helpUrl": ""
        },
        {
            "type": "knx_plugin_trigger_dpt_value_wsp_weak",
            "message0": "events: [home.event.wind.Weak, ] %1 if mean(value) < %2wsp %3 with %4 samples %5 DPT_Value_Wsp %6",
            "args0": [
                {
                    "type": "input_dummy"
                },
                {"type": "field_number",
                    "name": "value",
                    "value": 2.00,
                    "precision": .01
                },
                {
                    "type": "input_dummy"
                },
                {"type": "field_number",
                    "name": "samples",
                    "value": 30,
                    "precision": 1
                },
                {
                    "type": "input_dummy"
                },
                {
                    "type": "input_value",
                    "name": "addresses",
                    "check": "knx.Addresses",
                    "align": "RIGHT"
                },
            ],
            "previousStatement": "protocol.Trigger",
            "nextStatement": "protocol.Trigger",
            "colour": 280,
            "tooltip": "",
            "helpUrl": ""
        },
        {
            "type": "knx_plugin_command_dpt_switch_onoff",
            "message0": "DPT_Switch.OnOff %1",
            "args0": [
                {
                    "type": "input_value",
                    "name": "addresses",
                    "check": "knx.Addresses",
                    "align": "RIGHT"
                }
            ],
            "previousStatement": "protocol.Command",
            "nextStatement": "protocol.Command",
            "colour": 270,
            "tooltip": "",
            "helpUrl": ""
        },
        {
            "type": "knx_plugin_command_dpt_updown_updown",
            "message0": "DPT_UpDown.UpDown %1",
            "args0": [
                {
                    "type": "input_value",
                    "name": "addresses",
                    "check": "knx.Addresses",
                    "align": "RIGHT"
                }
            ],
            "previousStatement": "protocol.Command",
            "nextStatement": "protocol.Command",
            "colour": 270,
            "tooltip": "",
            "helpUrl": ""
        },
        {
            "type": "knx_plugin_command_dpt_updown_up",
            "message0": "DPT_UpDown.Up %1",
            "args0": [
                {
                    "type": "input_value",
                    "name": "addresses",
                    "check": "knx.Addresses",
                    "align": "RIGHT"
                }
            ],
            "previousStatement": "protocol.Command",
            "nextStatement": "protocol.Command",
            "colour": 270,
            "tooltip": "",
            "helpUrl": ""
        },
    ])
