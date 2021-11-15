Blockly.defineBlocksWithJsonArray(
    [
        {
            "type": "event_int",
            "message0": "%1",
            "args0": [
                {
                    "type": "field_number",
                    "name": "int",
                    "value": 1,
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
            "type": "event_float",
            "message0": "%1",
            "args0": [
                {
                    "type": "field_number",
                    "name": "float",
                    "value": 0.01,
                    "precision": 0.01
                }
            ],
            "previousStatement": "home.Event",
            "nextStatement": "home.Event",
            "colour": 205,
            "tooltip": "",
            "helpUrl": ""
        },
        {
            "type": "event_string",
            "message0": "%1",
            "args0": [
                {
                    "type": "field_input",
                    "name": "string",
                    "text": "a string"
                }
            ],
            "previousStatement": "home.Event",
            "nextStatement": "home.Event",
            "colour": 205,
            "tooltip": "",
            "helpUrl": ""
        },
        {
            "type": "home_event_alarm_armed_event",
            "message0": "alarm.armed.Event %1",
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
            "type": "home_event_alarm_triggered_event",
            "message0": "alarm.triggered.Event %1",
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
            "type": "home_event_power_consumption_event",
            "message0": "power.consumption.Event %1",
            "args0": [
                {
                    "type": "field_dropdown",
                    "name": "event",
                    "options": [
                        [
                            "No",
                            "No"
                        ],
                        [
                            "Low",
                            "Low"
                        ],
                        [
                            "High",
                            "High"
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
            "type": "home_event_power_consumption_duration_event",
            "message0": "power.consumption.duration.Event %1",
            "args0": [
                {
                    "type": "field_dropdown",
                    "name": "event",
                    "options": [
                        [
                            "Short",
                            "Short"
                        ],
                        [
                            "Long",
                            "Long"
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
            "type": "home_event_power_production_event",
            "message0": "power.production.Event %1",
            "args0": [
                {
                    "type": "field_dropdown",
                    "name": "event",
                    "options": [
                        [
                            "No",
                            "No"
                        ],
                        [
                            "Low",
                            "Low"
                        ],
                        [
                            "High",
                            "High"
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
            "type": "home_event_power_production_duration_event",
            "message0": "power.production.duration.Event %1",
            "args0": [
                {
                    "type": "field_dropdown",
                    "name": "event",
                    "options": [
                        [
                            "Short",
                            "Short"
                        ],
                        [
                            "Long",
                            "Long"
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
            "type": "home_event_sun_brightness_event",
            "message0": "sun_brightness.Event %1",
            "args0": [
                {
                    "type": "field_dropdown",
                    "name": "event",
                    "options": [
                        [
                            "Bright",
                            "Bright"
                        ],
                        [
                            "Dark",
                            "Dark"
                        ],
                        [
                            "DeepDark",
                            "DeepDark"
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
            "type": "home_event_sun_hit_event",
            "message0": "sun.hit.Event %1",
            "args0": [
                {
                    "type": "field_dropdown",
                    "name": "event",
                    "options": [
                        [
                            "Sunhit",
                            "Sunhit"
                        ],
                        [
                            "Sunleft",
                            "Sunleft"
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
            "type": "home_event_sun_phase_event",
            "message0": "sun.phase.Event %1",
            "args0": [
                {
                    "type": "field_dropdown",
                    "name": "event",
                    "options": [
                        [
                            "Sunrise",
                            "Sunrise"
                        ],
                        [
                            "Sunset",
                            "Sunset"
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
            "type": "home_event_wind_event",
            "message0": "wind.Event %1",
            "args0": [
                {
                    "type": "field_dropdown",
                    "name": "event",
                    "options": [
                        [
                            "Strong",
                            "Strong"
                        ],
                        [
                            "Weak",
                            "Weak"
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
            "type": "home_event_enable_event",
            "message0": "enable.Event %1",
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
            "type": "home_event_motion_event",
            "message0": "motion.Event %1",
            "args0": [
                {
                    "type": "field_dropdown",
                    "name": "event",
                    "options": [
                        [
                            "Spotted",
                            "Spotted"
                        ],
                        [
                            "Missed",
                            "Missed"
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
            "type": "home_event_show_event",
            "message0": "show.Event %1",
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
            "type": "home_event_sleepiness_event",
            "message0": "sleepiness.Event %1",
            "args0": [
                {
                    "type": "field_dropdown",
                    "name": "event",
                    "options": [
                        [
                            "Asleep",
                            "Asleep"
                        ],
                        [
                            "Awake",
                            "Awake"
                        ],
                        [
                            "Sleepy",
                            "Sleepy"
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
            "type": "home_event_waveform_event",
            "message0": "waveform.Event %1",
            "args0": [
                {
                    "type": "field_dropdown",
                    "name": "event",
                    "options": [
                        [
                            "Saw",
                            "Saw"
                        ],
                        [
                            "Sine",
                            "Sine"
                        ],
                        [
                            "HalfSine",
                            "HalfSine"
                        ],
                        [
                            "Triangle",
                            "Triangle"
                        ],
                        [
                            "Pulse",
                            "Pulse"
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
            "type": "home_event_presence_event",
            "message0": "presence.Event %1",
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
            "type": "home_event_courtesy_event",
            "message0": "courtesy.Event %1",
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
            "type": "home_event_scene_event",
            "message0": "scene.Event %1",
            "args0": [
                {
                    "type": "field_dropdown",
                    "name": "event",
                    "options": [
                        [
                            "Triggered",
                            "Triggered"
                        ],
                        [
                            "Untriggered",
                            "Untriggered"
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
            "type": "home_event_sun_brightness_event",
            "message0": "sun.brightness.Event %1",
            "args0": [
                {
                    "type": "field_dropdown",
                    "name": "event",
                    "options": [
                        [
                            "Bright",
                            "Bright"
                        ],
                        [
                            "Dark",
                            "Dark"
                        ],
                        [
                            "DeepDark",
                            "DeepDark"
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
    ])