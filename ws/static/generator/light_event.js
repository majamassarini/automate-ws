Blockly.Python['light_forced'] = function(block) {
  var dropdown_event = block.getFieldValue('event');
  var code = 'home.appliance.light.event.forced.Event.' + dropdown_event + ', ';
  return code;
};

Blockly.Python['light_brightness'] = function(block) {
  var number_int = block.getFieldValue('int');
  var code = 'home.appliance.light.event.brightness.Event(' + number_int + '), ';
  return code;
};

Blockly.Python['light_circadian_rhythm_brightness'] = function(block) {
  var number_int = block.getFieldValue('int');
  var code = 'home.appliance.light.event.circadian_rhythm.brightness.Event(' + number_int + '), ';
  return code;
};

Blockly.Python['light_lux_balancing_brightness'] = function(block) {
  var number_int = block.getFieldValue('int');
  var code = 'home.appliance.light.event.lux_balancing.brightness.Event(' + number_int + '), ';
  return code;
};

Blockly.Python['light_show_starting_brightness'] = function(block) {
  var number_int = block.getFieldValue('int');
  var code = 'home.appliance.light.event.show.starting_brightness.Event(' + number_int + '), ';
  return code;
};

Blockly.Python['light_show_ending_brightness'] = function(block) {
  var number_int = block.getFieldValue('int');
  var code = 'home.appliance.light.event.show.ending_brightness.Event(' + number_int + '), ';
  return code;
};

Blockly.Python['light_saturation'] = function(block) {
  var number_int = block.getFieldValue('int');
  var code = 'home.appliance.light.event.saturation.Event(' + number_int + '), ';
  return code;
};

Blockly.Python['light_circadian_rhythm_saturation'] = function(block) {
  var number_int = block.getFieldValue('int');
  var code = 'home.appliance.light.event.circadian_rhythm.saturation.Event(' + number_int + '), ';
  return code;
};

Blockly.Python['light_temperature'] = function(block) {
  var number_int = block.getFieldValue('int');
  var code = 'home.appliance.light.event.temperature.Event(' + number_int + '), ';
  return code;
};

Blockly.Python['light_circadian_rhythm_temperature'] = function(block) {
  var number_int = block.getFieldValue('int');
  var code = 'home.appliance.light.event.circadian_rhythm.temperature.Event(' + number_int + '), ';
  return code;
};

Blockly.Python['light_hue'] = function(block) {
  var number_int = block.getFieldValue('int');
  var code = 'home.appliance.light.event.hue.Event(' + number_int + '), ';
  return code;
};

Blockly.Python['light_circadian_rhythm_hue'] = function(block) {
  var number_int = block.getFieldValue('int');
  var code = 'home.appliance.light.event.circadian_rhythm.hue.Event(' + number_int + '), ';
  return code;
};


Blockly.Python['light_show_starting_hue'] = function(block) {
  var number_int = block.getFieldValue('int');
  var code = 'home.appliance.light.event.show.starting_hue.Event(' + number_int + '), ';
  return code;
};

Blockly.Python['light_show_ending_hue'] = function(block) {
  var number_int = block.getFieldValue('int');
  var code = 'home.appliance.light.event.show.ending_hue.Event(' + number_int + '), ';
  return code;
};

Blockly.Python['light_show_cycles'] = function(block) {
  var number_int = block.getFieldValue('int');
  var code = 'home.appliance.light.event.show.cycles.Event(' + number_int + '), ';
  return code;
};

Blockly.Python['light_show_period'] = function(block) {
  var number_int = block.getFieldValue('int');
  var code = 'home.appliance.light.event.show.period.Event(' + number_int + '), ';
  return code;
};

