Blockly.Python['knx_free_address'] = function(block) {
  var number_address = block.getFieldValue('address');
  var code = 'knx_stack.GroupAddress(free_style=' + number_address + '), ';
  return code;
};

Blockly.Python['knx_two_level_address'] = function(block) {
  var number_main = block.getFieldValue('main');
  var number_sub = block.getFieldValue('sub');
  var code = 'knx_stack.GroupAddress(two_level_style=knx_stack.address.TwoLevelStyle(main=' + number_main + ', sub=' + number_sub + ')), ';
  return code;
};

Blockly.Python['knx_three_level_address'] = function(block) {
  var number_main = block.getFieldValue('main');
  var number_middle = block.getFieldValue('middle');
  var number_sub = block.getFieldValue('sub');
  var code = 'knx_stack.GroupAddress(three_level_style=knx_stack.address.ThreeLevelStyle(main=' + number_main + ', middle=' + number_middle + ', sub=' + number_sub + ')), ';
  return code;
};

Blockly.Python['knx_addresses'] = function(block) {
  var statements_addresses = Blockly.Python.statementToCode(block, 'addresses');
  var code = '[' + statements_addresses + ']';
  return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['knx_plugin_trigger_dpt_switch_on'] = function(block) {
  var value_addresses = Blockly.Python.valueToCode(block, 'addresses', Blockly.Python.ORDER_ATOMIC);
  var code = 'knx_plugin.trigger.dpt_switch.On.make(' + value_addresses + ', ' + myObject.home_events + '), ';
  return code;
};

Blockly.Python['knx_plugin_trigger_dpt_switch_off'] = function(block) {
  var value_addresses = Blockly.Python.valueToCode(block, 'addresses', Blockly.Python.ORDER_ATOMIC);
  var code = 'knx_plugin.trigger.dpt_switch.Off.make(' + value_addresses + ', ' + myObject.home_events + '), ';
  return code;
};

Blockly.Python['knx_plugin_trigger_dpt_updown_opened'] = function(block) {
  var value_addresses = Blockly.Python.valueToCode(block, 'addresses', Blockly.Python.ORDER_ATOMIC);
  var code = 'knx_plugin.trigger.dpt_updown.Opened.make(' + value_addresses + ', ' + myObject.home_events + '), ';
  return code;
};

Blockly.Python['knx_plugin_trigger_dpt_updown_closed'] = function(block) {
  var value_addresses = Blockly.Python.valueToCode(block, 'addresses', Blockly.Python.ORDER_ATOMIC);
  var code = 'knx_plugin.trigger.dpt_updown.Closed.make(' + value_addresses + ', ' + myObject.home_events + '), ';
  return code;
};

Blockly.Python['knx_plugin_trigger_dpt_value_lux_always'] = function(block) {
  var value_addresses = Blockly.Python.valueToCode(block, 'addresses', Blockly.Python.ORDER_ATOMIC);
  var code = 'knx_plugin.trigger.dpt_value_lux.Always.make(' + value_addresses + ', ' + myObject.home_events + '), ';
  return code;
};

Blockly.Python['knx_plugin_trigger_dpt_value_wsp_always'] = function(block) {
  var value_addresses = Blockly.Python.valueToCode(block, 'addresses', Blockly.Python.ORDER_ATOMIC);
  var code = 'knx_plugin.trigger.dpt_value_wsp.Always.make(' + value_addresses + ', ' + myObject.home_events + '), ';
  return code;
};

Blockly.Python['knx_plugin_trigger_dpt_value_wsp_strong'] = function(block) {
  var value_addresses = Blockly.Python.valueToCode(block, 'addresses', Blockly.Python.ORDER_ATOMIC);
  var code = 'knx_plugin.trigger.dpt_value_wsp.Strong.make(' + value_addresses + ', ' + myObject.home_events + '), ';
  return code;
};

Blockly.Python['knx_plugin_trigger_dpt_value_wsp_weak'] = function(block) {
  var value_addresses = Blockly.Python.valueToCode(block, 'addresses', Blockly.Python.ORDER_ATOMIC);
  var code = 'knx_plugin.trigger.dpt_value_wsp.Weak.make(' + value_addresses + ', ' + myObject.home_events + '), ';
  return code;
};

Blockly.Python['knx_plugin_trigger_dpt_value_lux_bright'] = function(block) {
  var number_value = block.getFieldValue('value');
  var number_samples = block.getFieldValue('samples');
  var value_addresses = Blockly.Python.valueToCode(block, 'addresses', Blockly.Python.ORDER_ATOMIC);
  var code = 'knx_plugin.trigger.dpt_value_lux.Bright.make(' + value_addresses + ', ' + myObject.home_events + ', ' + number_samples + ', ' + number_value + '), ';
  return code;
};

Blockly.Python['knx_plugin_trigger_dpt_value_lux_dark'] = function(block) {
  var number_value = block.getFieldValue('value');
  var number_range = block.getFieldValue('range');
  var number_samples = block.getFieldValue('samples');
  var value_addresses = Blockly.Python.valueToCode(block, 'addresses', Blockly.Python.ORDER_ATOMIC);
  var code = 'knx_plugin.trigger.dpt_value_lux.Dark.make(' + value_addresses + ', ' + myObject.home_events + ', ' + number_samples + ', ' + number_value + ', ' + number_range + '), ';
  return code;
};

Blockly.Python['knx_plugin_trigger_dpt_value_lux_deepdark'] = function(block) {
  var number_value = block.getFieldValue('value');
  var number_samples = block.getFieldValue('samples');
  var value_addresses = Blockly.Python.valueToCode(block, 'addresses', Blockly.Python.ORDER_ATOMIC);
  var code = 'knx_plugin.trigger.dpt_value_lux.DeepDark.make(' + value_addresses + ', ' + myObject.home_events + ', ' + number_samples + ', ' + number_value + '), ';
  return code;
};

Blockly.Python['knx_plugin_command_dpt_switch_onoff'] = function(block) {
  var value_addresses = Blockly.Python.valueToCode(block, 'addresses', Blockly.Python.ORDER_ATOMIC);
  var code = 'knx_plugin.command.dpt_switch.OnOff.make(' + value_addresses + '), ';
  return code;
};

Blockly.Python['knx_plugin_command_dpt_updown_updown'] = function(block) {
  var value_addresses = Blockly.Python.valueToCode(block, 'addresses', Blockly.Python.ORDER_ATOMIC);
  var code = 'knx_plugin.command.dpt_updown.UpDown.make(' + value_addresses + '), ';
  return code;
};

Blockly.Python['knx_plugin_command_dpt_updown_up'] = function(block) {
  var value_addresses = Blockly.Python.valueToCode(block, 'addresses', Blockly.Python.ORDER_ATOMIC);
  var code = 'knx_plugin.command.dpt_updown.Up.make(' + value_addresses + '), ';
  return code;
};
