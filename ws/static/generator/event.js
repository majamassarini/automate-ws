Blockly.Python['event_int'] = function(block) {
  var number_int = block.getFieldValue('int');
  var code = number_int + ', ';
  return code;
};

Blockly.Python['event_float'] = function(block) {
  var number_float = block.getFieldValue('float');
  var code = number_float + ', ';
  return code;
};

Blockly.Python['event_string'] = function(block) {
  var text_string = block.getFieldValue('string');
  var code = text_string + ', ';
  return code;
};

Blockly.Python['home_event_alarm_armed_event'] = function(block) {
  var dropdown_event = block.getFieldValue('event');
  var code = 'home.event.alarm.armed.Event.' + dropdown_event + ', ';
  return code;
};

Blockly.Python['home_event_alarm_triggered_event'] = function(block) {
  var dropdown_event = block.getFieldValue('event');
  var code = 'home.event.alarm.triggered.Event.' + dropdown_event + ', ';
  return code;
};

Blockly.Python['home_event_power_consumption_event'] = function(block) {
  var dropdown_event = block.getFieldValue('event');
  var code = 'home.event.power.consumption.Event.' + dropdown_event + ', ';
  return code;
};

Blockly.Python['home_event_power_consumption_duration_event'] = function(block) {
  var dropdown_event = block.getFieldValue('event');
  var code = 'home.event.power.consumption.duration.Event.' + dropdown_event + ', ';
  return code;
};

Blockly.Python['home_event_power_production_event'] = function(block) {
  var dropdown_event = block.getFieldValue('event');
  var code = 'home.event.power.consumption.Event.' + dropdown_event + ', ';
  return code;
};

Blockly.Python['home_event_power_production_duration_event'] = function(block) {
  var dropdown_event = block.getFieldValue('event');
  var code = 'home.event.power.consumption.duration.Event.' + dropdown_event + ', ';
  return code;
};

Blockly.Python['home_event_sun_brightness_event'] = function(block) {
  var dropdown_event = block.getFieldValue('event');
  var code = 'home.event.sun.brightness.Event.' + dropdown_event + ', ';
  return code;
};

Blockly.Python['home_event_sun_hit_event'] = function(block) {
  var dropdown_event = block.getFieldValue('event');
  var code = 'home.event.sun.hit.Event.' + dropdown_event + ', ';
  return code;
};

Blockly.Python['home_event_sun_phase_event'] = function(block) {
  var dropdown_event = block.getFieldValue('event');
  var code = 'home.event.sun.phase.Event.' + dropdown_event + ', ';
  return code;
};

Blockly.Python['home_event_wind_event'] = function(block) {
  var dropdown_event = block.getFieldValue('event');
  var code = 'home.event.wind.Event.' + dropdown_event + ', ';
  return code;
};

Blockly.Python['home_event_motion_event'] = function(block) {
  var dropdown_event = block.getFieldValue('event');
  var code = 'home.event.motion.Event.' + dropdown_event + ', ';
  return code;
};

Blockly.Python['home_event_show_event'] = function(block) {
  var dropdown_event = block.getFieldValue('event');
  var code = 'home.event.show.Event.' + dropdown_event + ', ';
  return code;
};

Blockly.Python['home_event_sleepiness_event'] = function(block) {
  var dropdown_event = block.getFieldValue('event');
  var code = 'home.event.sleepiness.Event.' + dropdown_event + ', ';
  return code;
};

Blockly.Python['home_event_waveform_event'] = function(block) {
  var dropdown_event = block.getFieldValue('event');
  var code = 'home.event.waveform.Event.' + dropdown_event + ', ';
  return code;
};

Blockly.Python['home_event_presence_event'] = function(block) {
  var dropdown_event = block.getFieldValue('event');
  var code = 'home.event.presence.Event.' + dropdown_event + ', ';
  return code;
};

Blockly.Python['home_event_courtesy_event'] = function(block) {
  var dropdown_event = block.getFieldValue('event');
  var code = 'home.event.courtesy.Event.' + dropdown_event + ', ';
  return code;
};

Blockly.Python['home_event_scene_event'] = function(block) {
  var dropdown_event = block.getFieldValue('event');
  var code = 'home.event.scene.Event.' + dropdown_event + ', ';
  return code;
};
Blockly.Python['home_event_sun_brightness_event'] = function(block) {
  var dropdown_event = block.getFieldValue('event');
  var code = 'home.event.sun.brightness.Event.' + dropdown_event + ', ';
  return code;
};
