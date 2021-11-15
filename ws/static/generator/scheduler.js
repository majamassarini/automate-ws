Blockly.Python['appliance_name'] = function(block) {
  var text_name = block.getFieldValue('name');
  var code = '"' + text_name + '", ';
  return code;
};

Blockly.Python['scheduler_trigger'] = function(block) {
  var statements_events = Blockly.Python.statementToCode(block, 'events');
  var statements_appliance_name = Blockly.Python.statementToCode(block, 'appliance_name');
  var code = '    scheduler_triggers.append(home.scheduler.trigger.protocol.Trigger(name="scheduler protocol trigger ' + myObject.schedulers_for + '",\n' +
             '                                                                      events=[ ' + statements_events + '],\n' +
             '                                                                      protocol_trigger=protocol_trigger))\n' +
             'scheduler.append(SchedulerInfo([' + statements_appliance_name + '], scheduler_triggers))\n'
  ;
  return code;
};

Blockly.Python['scheduler_trigger_delay'] = function(block) {
  var statements_events = Blockly.Python.statementToCode(block, 'events');
  var statements_appliance_name = Blockly.Python.statementToCode(block, 'appliance_name');
  var number_delay = block.getFieldValue('delay');
  var code = '    scheduler_triggers.append(home.scheduler.trigger.protocol.Trigger(name="scheduler protocol trigger ' + myObject.schedulers_for + '",\n' +
      '                                                                      events=[ ' + statements_events + '],\n' +
      '                                                                      protocol_trigger=protocol_trigger,\n' +
      '                                                                      timeout_seconds=' + number_delay + '))\n' +
      'scheduler.append(SchedulerInfo([' + statements_appliance_name + '], scheduler_triggers))\n'
  ;
  return code;
};

Blockly.Python['scheduler_trigger_sunrise'] = function(block) {
  var text_name = block.getFieldValue('name');
  var number_latitude = block.getFieldValue('latitude');
  var number_longitude = block.getFieldValue('longitude');
  var number_elevation = block.getFieldValue('elevation');
  var statements_events = Blockly.Python.statementToCode(block, 'events');
  var statements_appliance_name = Blockly.Python.statementToCode(block, 'appliance_name');
  var code = 'scheduler_triggers = list()\n' +
      'scheduler_triggers.append(home.scheduler.trigger.sun.sunrise.Trigger(name="' + text_name + ' (scheduler sunrise trigger)",\n' +
      '                                                                     events=[ ' + statements_events + '],\n' +
      '                                                                     latitude=' + number_latitude + ',\n' +
      '                                                                     longitude=' + number_longitude + ',\n' +
      '                                                                     elevation=' + number_elevation + '))\n' +
      'scheduler.append(SchedulerInfo([' + statements_appliance_name + '], scheduler_triggers))\n'
  ;
  return code;
};

Blockly.Python['scheduler_trigger_sunset'] = function(block) {
  var text_name = block.getFieldValue('name');
  var number_latitude = block.getFieldValue('latitude');
  var number_longitude = block.getFieldValue('longitude');
  var number_elevation = block.getFieldValue('elevation');
  var statements_events = Blockly.Python.statementToCode(block, 'events');
  var statements_appliance_name = Blockly.Python.statementToCode(block, 'appliance_name');
  var code = 'scheduler_triggers = list()\n' +
      'scheduler_triggers.append(home.scheduler.trigger.sun.sunset.Trigger(name="' + text_name + ' (scheduler sunset trigger)",\n' +
      '                                                                    events=[ ' + statements_events + '],\n' +
      '                                                                    latitude=' + number_latitude + ',\n' +
      '                                                                    longitude=' + number_longitude + ',\n' +
      '                                                                    elevation=' + number_elevation + '))\n' +
      'scheduler.append(SchedulerInfo([' + statements_appliance_name + '], scheduler_triggers))\n'
  ;
  return code;
};

Blockly.Python['scheduler_trigger_sunhit'] = function(block) {
  var text_name = block.getFieldValue('name');
  var number_latitude = block.getFieldValue('latitude');
  var number_longitude = block.getFieldValue('longitude');
  var number_elevation = block.getFieldValue('elevation');
  var number_bottom_altitude = block.getFieldValue('bottom_altitude');
  var number_upper_altitude = block.getFieldValue('upper_altitude');
  var number_min_azimuth = block.getFieldValue('min_azimuth');
  var number_max_azimuth = block.getFieldValue('max_azimuth');
  var statements_events = Blockly.Python.statementToCode(block, 'events');
  var statements_appliance_name = Blockly.Python.statementToCode(block, 'appliance_name');
  var code = 'scheduler_triggers = list()\n' +
      'scheduler_triggers.append(home.scheduler.trigger.sun.sunhit.Trigger(name="' + text_name + ' (scheduler sunhit trigger)",\n' +
      '                                                                    events=[ ' + statements_events + '],\n' +
      '                                                                    latitude=' + number_latitude + ',\n' +
      '                                                                    longitude=' + number_longitude + ',\n' +
      '                                                                    elevation=' + number_elevation + ',\n' +
      '                                                                    position=home.scheduler.trigger.sun.Position(' + number_bottom_altitude + ', ' +
                                                                                                                          + number_upper_altitude + ', ' +
                                                                                                                          + number_min_azimuth + ', ' +
                                                                                                                          + number_max_azimuth + ')))\n' +
      'scheduler.append(SchedulerInfo([' + statements_appliance_name + '], scheduler_triggers))\n'
  ;
  return code;
};

Blockly.Python['scheduler_trigger_sunleft'] = function(block) {
  var text_name = block.getFieldValue('name');
  var number_latitude = block.getFieldValue('latitude');
  var number_longitude = block.getFieldValue('longitude');
  var number_elevation = block.getFieldValue('elevation');
  var number_bottom_altitude = block.getFieldValue('bottom_altitude');
  var number_upper_altitude = block.getFieldValue('upper_altitude');
  var number_min_azimuth = block.getFieldValue('min_azimuth');
  var number_max_azimuth = block.getFieldValue('max_azimuth');
  var statements_events = Blockly.Python.statementToCode(block, 'events');
  var statements_appliance_name = Blockly.Python.statementToCode(block, 'appliance_name');
  var code = 'scheduler_triggers = list()\n' +
      'scheduler_triggers.append(home.scheduler.trigger.sun.sunleft.Trigger(name="' + text_name + ' (scheduler sunleft trigger)",\n' +
      '                                                                     events=[ ' + statements_events + '],\n' +
      '                                                                     latitude=' + number_latitude + ',\n' +
      '                                                                     longitude=' + number_longitude + ',\n' +
      '                                                                     elevation=' + number_elevation + ',\n' +
      '                                                                     position=home.scheduler.trigger.sun.Position(' + number_bottom_altitude + ', ' +
                                                                                                                           + number_upper_altitude + ', ' +
                                                                                                                           + number_min_azimuth + ', ' +
                                                                                                                           + number_max_azimuth + ')))\n' +
      'scheduler.append(SchedulerInfo([' + statements_appliance_name + '], scheduler_triggers))\n'
  ;
  return code;
};

Blockly.Python['scheduler_trigger_cron'] = function(block) {
  var text_name = block.getFieldValue('name');
  var statements_events = Blockly.Python.statementToCode(block, 'events');
  var statements_appliance_name = Blockly.Python.statementToCode(block, 'appliance_name');
  var text_year = block.getFieldValue('year');
  var text_month = block.getFieldValue('month');
  var text_day = block.getFieldValue('day');
  var text_week = block.getFieldValue('week');
  var text_day_of_week = block.getFieldValue('day_of_week');
  var text_hour = block.getFieldValue('hour');
  var text_minute = block.getFieldValue('minute');
  var text_start_date = block.getFieldValue('start_date');
  var text_end_date = block.getFieldValue('end_date');
  var code = 'scheduler_triggers = list()\n' +
      'scheduler_triggers.append(home.scheduler.trigger.cron.Trigger(name="' + text_name + ' (scheduler sunleft trigger)",\n' +
      '                                                              events=[ ' + statements_events + '],\n' +
      '                                                              year=' + text_year + ',\n' +
      '                                                              month=' + text_month + ',\n' +
      '                                                              day=' + text_day + ',\n' +
      '                                                              week=' + text_week + ',\n' +
      '                                                              day_of_week=' + text_day_of_week + ',\n' +
      '                                                              hour=' + text_hour + ',\n' +
      '                                                              minute=' + text_minute + ',\n' +
      '                                                              start_date=' + text_start_date + ',\n' +
      '                                                              end_date=' + text_end_date + ',\n' +
                                                                     '))\n' +
      'scheduler.append(SchedulerInfo([' + statements_appliance_name + '], scheduler_triggers))\n'
  ;
  return code;
};
