Blockly.Python['protocol_triggers'] = function(block) {
  var statements_protocol_trigger = Blockly.Python.statementToCode(block, 'protocol_trigger');
  var code = '[' + statements_protocol_trigger + ']';
  return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['protocol_commands'] = function(block) {
  var statements_protocol_command = Blockly.Python.statementToCode(block, 'protocol_command');
  var code = '[' + statements_protocol_command + ']';
  return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['appliance_socket_presence_socket'] = function(block) {
  var text_name = block.getFieldValue('name');
  var collection_name = block.getFieldValue('collection');

  myObject.home_events = "[home.appliance.socket.event.forced.Event.On, ]";
  myObject.schedulers_for = "forced on (" + text_name + ")";
  var value_forced_on = Blockly.Python.valueToCode(block, 'forced_on', Blockly.Python.ORDER_ATOMIC);
  var statements_forced_on_schedulers = Blockly.Python.statementToCode(block, 'forced_on_schedulers');

  myObject.home_events = "[home.appliance.socket.event.forced.Event.Off, ]";
  myObject.schedulers_for = "forced off (" + text_name + ")";
  var value_forced_off = Blockly.Python.valueToCode(block, 'forced_off', Blockly.Python.ORDER_ATOMIC);
  var statements_forced_off_schedulers = Blockly.Python.statementToCode(block, 'forced_off_schedulers');

  myObject.home_events = "[home.event.presence.Event.On, ]";
  myObject.schedulers_for = "presence on (" + text_name + ")";
  var value_presence_on = Blockly.Python.valueToCode(block, 'presence_on', Blockly.Python.ORDER_ATOMIC);
  var statements_presence_on_schedulers = Blockly.Python.statementToCode(block, 'presence_on_schedulers');

  myObject.home_events = "[home.event.presence.Event.Off, ]";
  myObject.schedulers_for = "presence off (" + text_name + ")";
  var value_presence_off = Blockly.Python.valueToCode(block, 'presence_off', Blockly.Python.ORDER_ATOMIC);
  var statements_presence_off_schedulers = Blockly.Python.statementToCode(block, 'presence_off_schedulers');

  var value_state = Blockly.Python.valueToCode(block, 'state', Blockly.Python.ORDER_ATOMIC);
  var code = 'appliance = home.appliance.socket.presence.Appliance("' + text_name + '", [])\n' +
      'appliances.append(ApplianceInfo(appliance, "'+ collection_name + '"))\n';
  if (value_forced_on)
      code = code +
      'forced_on_performer = home.Performer("trigger forced on for ' + text_name + '", appliance, [], ' + value_forced_on + ')\n' +
      'trigger_performers.append(PerformerTriggerInfo("' + text_name + '", forced_on_performer))\n';
  if (value_forced_off)
      code = code +
      'forced_off_performer = home.Performer("trigger forced off for ' + text_name + '", appliance, [], ' + value_forced_off + ')\n' +
      'trigger_performers.append(PerformerTriggerInfo("' + text_name + '", forced_off_performer))\n';
  if (value_presence_on)
      code = code +
      'presence_on_performer = home.Performer("trigger presence on for ' + text_name + '", appliance, [], ' + value_presence_on + ')\n' +
      'trigger_performers.append(PerformerTriggerInfo("' + text_name + '", presence_on_performer))\n';
  if (value_presence_off)
      code = code +
      'presence_off_performer = home.Performer("trigger presence off for ' + text_name + '", appliance, [], ' + value_presence_off + ')\n' +
      'trigger_performers.append(PerformerTriggerInfo("' + text_name + '", presence_off_performer))\n';

  if (value_state)
      code = code +
      'command_performer = home.Performer("commands for ' + text_name + '", appliance, ' + value_state + ', [])\n' +
      'command_performers.append(PerformerCommandInfo("' + text_name + '", command_performer))\n';

  if (statements_forced_on_schedulers)
      code = code +
          'scheduler_triggers = list()\n' +
          'for protocol_trigger in forced_on_performer.triggers:\n' +
          statements_forced_on_schedulers;
  if (statements_forced_off_schedulers)
      code = code +
          'scheduler_triggers = list()\n' +
          'for protocol_trigger in forced_off_performer.triggers:\n' +
          statements_forced_off_schedulers;
  if (statements_presence_on_schedulers)
    code = code +
      'scheduler_triggers = list()\n' +
      'for protocol_trigger in presence_on_performer.triggers:\n' +
      statements_presence_on_schedulers;
  if (statements_presence_off_schedulers)
    code = code +
      'scheduler_triggers = list()\n' +
      'for protocol_trigger in presence_off_performer.triggers:\n' +
      statements_presence_off_schedulers;
  return code;
};

Blockly.Python['appliance_curtain_outdoor_curtain'] = function(block) {
  var text_name = block.getFieldValue('name');
  var collection_name = block.getFieldValue('collection');

  myObject.home_events = "[home.appliance.curtain.event.forced.Event.Opened, ]";
  myObject.schedulers_for = "forced opened (" + text_name + ")";
  var value_forced_opened = Blockly.Python.valueToCode(block, 'forced_opened', Blockly.Python.ORDER_ATOMIC);
  var statements_forced_opened_schedulers = Blockly.Python.statementToCode(block, 'forced_opened_schedulers');

  myObject.home_events = "[home.appliance.curtain.event.forced.Event.Closed, ]";
  myObject.schedulers_for = "forced closed (" + text_name + ")";
  var value_forced_closed = Blockly.Python.valueToCode(block, 'forced_closed', Blockly.Python.ORDER_ATOMIC);
  var statements_forced_closed_schedulers = Blockly.Python.statementToCode(block, 'forced_closed_schedulers');

  myObject.home_events = "[home.event.wind.Event.Weak, ]";
  myObject.schedulers_for = "wind weak (" + text_name + ")";
  var value_wind_weak = Blockly.Python.valueToCode(block, 'wind_weak', Blockly.Python.ORDER_ATOMIC);
  var statements_wind_weak_schedulers = Blockly.Python.statementToCode(block, 'wind_weak_schedulers');

  myObject.home_events = "[home.event.wind.Event.Strong, ]";
  myObject.schedulers_for = "wind strong (" + text_name + ")";
  var value_wind_strong = Blockly.Python.valueToCode(block, 'wind_strong', Blockly.Python.ORDER_ATOMIC);
  var statements_wind_strong_schedulers = Blockly.Python.statementToCode(block, 'wind_strong_schedulers');

  myObject.home_events = "[home.event.sun.brightness.Event.Bright, ]";
  myObject.schedulers_for = "sun brightness bright (" + text_name + ")";
  var value_sun_brightness_bright = Blockly.Python.valueToCode(block, 'sun_brightness_bright', Blockly.Python.ORDER_ATOMIC);
  var statements_sun_brightness_bright_schedulers = Blockly.Python.statementToCode(block, 'sun_brightness_bright_schedulers');

  myObject.home_events = "[home.event.sun.brightness.Event.Dark, ]";
  myObject.schedulers_for = "sun brightness dark (" + text_name + ")";
  var value_sun_brightness_dark = Blockly.Python.valueToCode(block, 'sun_brightness_dark', Blockly.Python.ORDER_ATOMIC);
  var statements_sun_brightness_dark_schedulers = Blockly.Python.statementToCode(block, 'sun_brightness_dark_schedulers');

  myObject.home_events = "[home.event.sun.brightness.Event.DeepDark, ]";
  myObject.schedulers_for = "sun brightness deepdark (" + text_name + ")";
  var value_sun_brightness_deepdark = Blockly.Python.valueToCode(block, 'sun_brightness_deepdark', Blockly.Python.ORDER_ATOMIC);
  var statements_sun_brightness_deepdark_schedulers = Blockly.Python.statementToCode(block, 'sun_brightness_deepdark_schedulers');

  myObject.home_events = "[home.event.sun.twilight.civil.Event.Sunrise, ]";
  myObject.schedulers_for = "sun twilight civil sunrise (" + text_name + ")";
  var value_sun_twilight_sunrise = Blockly.Python.valueToCode(block, 'sun_twilight_sunrise', Blockly.Python.ORDER_ATOMIC);
  var statements_sun_twilight_sunrise_schedulers = Blockly.Python.statementToCode(block, 'sun_twilight_sunrise_schedulers');

  myObject.home_events = "[home.event.sun.twilight.civil.Event.Sunset, ]";
  myObject.schedulers_for = "sun twilight civil sunset (" + text_name + ")";
  var value_sun_twilight_sunset = Blockly.Python.valueToCode(block, 'sun_twilight_sunset', Blockly.Python.ORDER_ATOMIC);
  var statements_sun_twilight_sunset_schedulers = Blockly.Python.statementToCode(block, 'sun_twilight_sunset_schedulers');

  myObject.home_events = "[home.event.sun.hit.Event.Sunhit, ]";
  myObject.schedulers_for = "sun sunhit (" + text_name + ")";
  var value_sun_hit_sunhit = Blockly.Python.valueToCode(block, 'sun_hit_sunhit', Blockly.Python.ORDER_ATOMIC);
  var statements_sun_hit_sunhit_schedulers = Blockly.Python.statementToCode(block, 'sun_hit_sunhit_schedulers');

  myObject.home_events = "[home.event.sun.hit.Event.Sunleft, ]";
  myObject.schedulers_for = "sun sunleft (" + text_name + ")";
  var value_sun_hit_sunleft = Blockly.Python.valueToCode(block, 'sun_hit_sunleft', Blockly.Python.ORDER_ATOMIC);
  var statements_sun_hit_sunleft_schedulers = Blockly.Python.statementToCode(block, 'sun_hit_sunleft_schedulers');

  var value_state = Blockly.Python.valueToCode(block, 'state', Blockly.Python.ORDER_ATOMIC);
  var code = 'appliance = home.appliance.curtain.outdoor.Appliance("' + text_name + '", [])\n' +
      'appliances.append(ApplianceInfo(appliance, "'+ collection_name + '"))\n';
  if (value_forced_opened)
    code = code +
        'forced_opened_performer = home.Performer("trigger forced opened for ' + text_name + '", appliance, [], ' + value_forced_opened + ')\n' +
        'trigger_performers.append(PerformerTriggerInfo("' + text_name + '", forced_opened_performer))\n';
  if (value_forced_closed)
    code = code +
        'forced_closed_performer = home.Performer("trigger forced closed for ' + text_name + '", appliance, [], ' + value_forced_closed + ')\n' +
        'trigger_performers.append(PerformerTriggerInfo("' + text_name + '", forced_closed_performer))\n';
  if (value_wind_weak)
    code = code +
        'wind_weak_performer = home.Performer("trigger wind weak for ' + text_name + '", appliance, [], ' + value_wind_weak + ')\n' +
        'trigger_performers.append(PerformerTriggerInfo("' + text_name + '", wind_weak_performer))\n';
  if (value_wind_strong)
    code = code +
        'wind_strong_performer = home.Performer("trigger wind strong for ' + text_name + '", appliance, [], ' + value_wind_strong + ')\n' +
        'trigger_performers.append(PerformerTriggerInfo("' + text_name + '", wind_strong_performer))\n';
  if (value_sun_brightness_bright)
    code = code +
        'sun_brightness_bright_performer = home.Performer("trigger sun brightness bright for ' + text_name + '", appliance, [], ' + value_sun_brightness_bright + ')\n' +
        'trigger_performers.append(PerformerTriggerInfo("' + text_name + '", sun_brightness_bright_performer))\n';
  if (value_sun_brightness_dark)
    code = code +
        'sun_brightness_dark_performer = home.Performer("trigger sun brightness dark for ' + text_name + '", appliance, [], ' + value_sun_brightness_dark + ')\n' +
        'trigger_performers.append(PerformerTriggerInfo("' + text_name + '", sun_brightness_dark_performer))\n';
  if (value_sun_brightness_deepdark)
    code = code +
        'sun_brightness_deepdark_performer = home.Performer("trigger sun brightness deepdark for ' + text_name + '", appliance, [], ' + value_sun_brightness_deepdark + ')\n' +
        'trigger_performers.append(PerformerTriggerInfo("' + text_name + '", sun_brightness_deepdark_performer))\n';
  if (value_sun_twilight_sunrise)
    code = code +
        'sun_twilight_sunrise_performer = home.Performer("trigger sun twilight sunrise for ' + text_name + '", appliance, [], ' + value_sun_twilight_sunrise + ')\n' +
        'trigger_performers.append(PerformerTriggerInfo("' + text_name + '", sun_twilight_sunrise_performer))\n';
  if (value_sun_twilight_sunset)
    code = code +
        'sun_twilight_sunset_performer = home.Performer("trigger sun twilight sunset for ' + text_name + '", appliance, [], ' + value_sun_twilight_sunset + ')\n' +
        'trigger_performers.append(PerformerTriggerInfo("' + text_name + '", sun_twilight_sunset_performer))\n';
  if (value_sun_hit_sunhit)
    code = code +
        'sun_hit_sunhit_performer = home.Performer("trigger sun hit sunhit for ' + text_name + '", appliance, [], ' + value_sun_hit_sunhit + ')\n' +
        'trigger_performers.append(PerformerTriggerInfo("' + text_name + '", sun_hit_sunhit_performer))\n';
  if (value_sun_hit_sunleft)
    code = code +
        'sun_hit_sunleft_performer = home.Performer("trigger sun hit sunleft for ' + text_name + '", appliance, [], ' + value_sun_hit_sunleft + ')\n' +
        'trigger_performers.append(PerformerTriggerInfo("' + text_name + '", sun_hit_sunleft_performer))\n';

  if (value_state)
    code = code +
        'command_performer = home.Performer("commands for ' + text_name + '", appliance, ' + value_state + ', [])\n' +
        'command_performers.append(PerformerCommandInfo("' + text_name + '", command_performer))\n';

  if (statements_forced_opened_schedulers)
    code = code +
        'scheduler_triggers = list()\n' +
        'for protocol_trigger in forced_opened_performer.triggers:\n' +
        statements_forced_opened_schedulers;
  if (statements_forced_closed_schedulers)
    code = code +
        'scheduler_triggers = list()\n' +
        'for protocol_trigger in forced_closed_performer.triggers:\n' +
        statements_forced_closed_schedulers;
  if (statements_wind_weak_schedulers)
    code = code +
        'scheduler_triggers = list()\n' +
        'for protocol_trigger in wind_weak_performer.triggers:\n' +
        statements_wind_weak_schedulers;
  if (statements_wind_strong_schedulers)
    code = code +
        'scheduler_triggers = list()\n' +
        'for protocol_trigger in wind_strong_performer.triggers:\n' +
        statements_wind_strong_schedulers;
  if (statements_sun_brightness_bright_schedulers)
    code = code +
        'scheduler_triggers = list()\n' +
        'for protocol_trigger in sun_brightness_bright_performer.triggers:\n' +
        statements_sun_brightness_bright_schedulers;
  if (statements_sun_brightness_dark_schedulers)
    code = code +
        'scheduler_triggers = list()\n' +
        'for protocol_trigger in sun_brightness_dark_performer.triggers:\n' +
        statements_sun_brightness_dark_schedulers;
  if (statements_sun_brightness_deepdark_schedulers)
    code = code +
        'scheduler_triggers = list()\n' +
        'for protocol_trigger in sun_brightness_deepdark_performer.triggers:\n' +
        statements_sun_brightness_deepdark_schedulers;
  if (statements_sun_twilight_sunrise_schedulers)
    code = code +
        'scheduler_triggers = list()\n' +
        'for protocol_trigger in sun_twilight_sunrise_performer.triggers:\n' +
        statements_sun_twilight_sunrise_schedulers;
  if (statements_sun_twilight_sunset_schedulers)
    code = code +
        'scheduler_triggers = list()\n' +
        'for protocol_trigger in sun_twilight_sunset_performer.triggers:\n' +
        statements_sun_twilight_sunset_schedulers;
  if (statements_sun_hit_sunhit_schedulers)
    code = code +
        'scheduler_triggers = list()\n' +
        'for protocol_trigger in sun_hit_sunhit_performer.triggers:\n' +
        statements_sun_hit_sunhit_schedulers;
  if (statements_sun_hit_sunleft_schedulers)
    code = code +
        'scheduler_triggers = list()\n' +
        'for protocol_trigger in sun_hit_sunleft_performer.triggers:\n' +
        statements_sun_hit_sunleft_schedulers;
  return code;
};

Blockly.Python['appliance_sensor_lux'] = function(block) {
  var text_name = block.getFieldValue('name');
  var collection_name = block.getFieldValue('collection');

  myObject.home_events = "[]";
  myObject.schedulers_for = "value lux (" + text_name + ")";
  var value_lux = Blockly.Python.valueToCode(block, 'lux', Blockly.Python.ORDER_ATOMIC);
  var statements_lux_schedulers = Blockly.Python.statementToCode(block, 'lux_schedulers');

  var value_state = Blockly.Python.valueToCode(block, 'state', Blockly.Python.ORDER_ATOMIC);
  var code = 'appliance = home.appliance.sensor.luxmeter.Appliance("' + text_name + '", [])\n' +
      'appliances.append(ApplianceInfo(appliance, "'+ collection_name + '"))\n';

  if (value_lux)
      code = code +
      'lux_performer = home.Performer("lux value for ' + text_name + '", appliance, [], ' + value_lux + ')\n' +
      'trigger_performers.append(PerformerTriggerInfo("' + text_name + '", lux_performer))\n';

  if (value_state)
      code = code +
      'command_performer = home.Performer("commands for ' + text_name + '", appliance, ' + value_state + ', [])\n' +
      'command_performers.append(PerformerCommandInfo("' + text_name + '", command_performer))\n';

  if (statements_lux_schedulers)
      code = code +
          'scheduler_triggers = list()\n' +
          'for protocol_trigger in lux_performer.triggers:\n' +
          statements_lux_schedulers;
  return code;
};

Blockly.Python['appliance_sensor_anemometer'] = function(block) {
  var text_name = block.getFieldValue('name');
  var collection_name = block.getFieldValue('collection');

  myObject.home_events = "[]";
  myObject.schedulers_for = "value anemometer (" + text_name + ")";
  var value_wind = Blockly.Python.valueToCode(block, 'wind', Blockly.Python.ORDER_ATOMIC);
  var statements_wind_schedulers = Blockly.Python.statementToCode(block, 'wind_schedulers');

  var value_state = Blockly.Python.valueToCode(block, 'state', Blockly.Python.ORDER_ATOMIC);
  var code = 'appliance = home.appliance.sensor.anemometer.Appliance("' + text_name + '", [])\n' +
      'appliances.append(ApplianceInfo(appliance, "'+ collection_name + '"))\n';

  if (value_wind)
    code = code +
        'wind_performer = home.Performer("anemometer value for ' + text_name + '", appliance, [], ' + value_wind + ')\n' +
        'trigger_performers.append(PerformerTriggerInfo("' + text_name + '", wind_performer))\n';

  if (value_state)
    code = code +
        'command_performer = home.Performer("commands for ' + text_name + '", appliance, ' + value_state + ', [])\n' +
        'command_performers.append(PerformerCommandInfo("' + text_name + '", command_performer))\n';

  if (statements_wind_schedulers)
    code = code +
        'scheduler_triggers = list()\n' +
        'for protocol_trigger in wind_performer.triggers:\n' +
        statements_wind_schedulers;
  return code;
};

Blockly.Python['appliance_sensor_alarm'] = function(block) {
  var text_name = block.getFieldValue('name');
  var collection_name = block.getFieldValue('collection');

  myObject.home_events = "[home.event.alarm.armed.Event.On, ]";
  myObject.schedulers_for = "alarm armed on (" + text_name + ")";
  var value_alarm_armed_on = Blockly.Python.valueToCode(block, 'alarm_armed_on', Blockly.Python.ORDER_ATOMIC);
  var statements_armed_on_schedulers = Blockly.Python.statementToCode(block, 'armed_on_schedulers');

  myObject.home_events = "[home.event.alarm.armed.Event.Off, ]";
  myObject.schedulers_for = "alarm armed off (" + text_name + ")";
  var value_alarm_armed_off = Blockly.Python.valueToCode(block, 'alarm_armed_off', Blockly.Python.ORDER_ATOMIC);
  var statements_armed_off_schedulers = Blockly.Python.statementToCode(block, 'armed_off_schedulers');

  myObject.home_events = "[home.event.alarm.triggered.Event.On, ]";
  myObject.schedulers_for = "alarm triggered on (" + text_name + ")";
  var value_alarm_triggered_on = Blockly.Python.valueToCode(block, 'alarm_triggered_on', Blockly.Python.ORDER_ATOMIC);
  var statements_triggered_on_schedulers = Blockly.Python.statementToCode(block, 'triggered_on_schedulers');

  myObject.home_events = "[home.event.alarm.triggered.Event.Off, ]";
  myObject.schedulers_for = "alarm triggered off (" + text_name + ")";
  var value_alarm_triggered_off = Blockly.Python.valueToCode(block, 'alarm_triggered_off', Blockly.Python.ORDER_ATOMIC);
  var statements_triggered_off_schedulers = Blockly.Python.statementToCode(block, 'triggered_off_schedulers');

  var value_state = Blockly.Python.valueToCode(block, 'state', Blockly.Python.ORDER_ATOMIC);
  var code = 'appliance = home.appliance.sensor.alarm.Appliance("' + text_name + '", [])\n' +
      'appliances.append(ApplianceInfo(appliance, "'+ collection_name + '"))\n';

  if (value_alarm_armed_on)
    code = code +
        'armed_on_performer = home.Performer("trigger armed on for ' + text_name + '", appliance, [], ' + value_alarm_armed_on + ')\n' +
        'trigger_performers.append(PerformerTriggerInfo("' + text_name + '", armed_on_performer))\n';
  if (value_alarm_armed_off)
    code = code +
        'armed_off_performer = home.Performer("trigger armed off for ' + text_name + '", appliance, [], ' + value_alarm_armed_off + ')\n' +
        'trigger_performers.append(PerformerTriggerInfo("' + text_name + '", armed_off_performer))\n';
  if (value_alarm_triggered_on)
    code = code +
        'triggered_on_performer = home.Performer("trigger armed on for ' + text_name + '", appliance, [], ' + value_alarm_triggered_on + ')\n' +
        'trigger_performers.append(PerformerTriggerInfo("' + text_name + '", triggered_on_performer))\n';
  if (value_alarm_triggered_off)
    code = code +
        'triggered_off_performer = home.Performer("trigger armed off for ' + text_name + '", appliance, [], ' + value_alarm_triggered_off + ')\n' +
        'trigger_performers.append(PerformerTriggerInfo("' + text_name + '", triggered_off_performer))\n';

  if (value_state)
    code = code +
        'command_performer = home.Performer("commands for ' + text_name + '", appliance, ' + value_state + ', [])\n' +
        'command_performers.append(PerformerCommandInfo("' + text_name + '", command_performer))\n';

  if (statements_armed_on_schedulers)
    code = code +
        'scheduler_triggers = list()\n' +
        'for protocol_trigger in armed_on_performer.triggers:\n' +
        statements_armed_on_schedulers;
  if (statements_armed_off_schedulers)
    code = code +
        'scheduler_triggers = list()\n' +
        'for protocol_trigger in armed_off_performer.triggers:\n' +
        statements_armed_off_schedulers;
  if (statements_triggered_on_schedulers)
    code = code +
        'scheduler_triggers = list()\n' +
        'for protocol_trigger in triggered_on_performer.triggers:\n' +
        statements_triggered_on_schedulers;
  if (statements_triggered_off_schedulers)
    code = code +
        'scheduler_triggers = list()\n' +
        'for protocol_trigger in triggered_off_performer.triggers:\n' +
        statements_triggered_off_schedulers;
  return code;
};
