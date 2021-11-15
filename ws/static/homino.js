var socket = new WebSocket('ws://' + location.host + '/ws');

function id_from_name(name) {
 var id = name.replace(/ /g, '-' ).replace(/\(/g, '-' ).replace(/\)/g, '-' )
 return id;
}

function update_event(message) {
    console.log(message);
    var id = message.id;
    var id_enabled = message.id_enabled;
    var id_icon = message.id_icon;
    var id_label = message.id_label;
    $("#"+id).text(message.event);
    $("#"+id).prop('disabled', !message.enabled);
    $("#"+id_label).text(message.label);
    $("#"+id_enabled).prop('checked', message.enabled);
    $("#"+id_icon).attr("class", message.icon);
    if (message.displayed) {
        $("#form-"+id).show();
    }
    else {
        $("#form-"+id).hide();
    }
    //$("#"+id_description).text(message.description);
}

function update_appliance(message) {
    console.log(message);
    var id = id_from_name(message.appliance)
    $("#"+id).text(message.state);
    message.events.forEach(update_event)
}

socket.onmessage = function(event) {
    console.log(event.data);
    message = $.parseJSON(event.data);
    if (message.hasOwnProperty('appliance')) {
        update_appliance(message);
    }
    else {
        update_event(message);
    }
}

function ajaxPostValue(uri, module, klass, value) {
    $.post(uri,
    {module: module,
     klass: klass,
     value: value},
    function(message, status) {
        update_appliance(message)
    });
}

function ajaxPostSimple(uri, module, klass) {
    $.post(uri,
    {module: module,
     klass: klass},
    function(message, status) {
        update_appliance(message)
    });
}


// Blockly

Blockly.Generator.prototype.INDENT = ""

var myObject = {
    home_events: null,
    schedulers_for: null,
};

function showCode(editor_uri, workspace) {
    Blockly.Python.INFINITE_LOOP_TRAP = null;
    var code = Blockly.Python.workspaceToCode(workspace);
    $("#codeDiv").text(code);
    $.post(editor_uri,
    {code: code},
    function(status) {
        console.log(status);
    });
}

function saveWorkspace(editor_uri, workspace) {
    var xml = Blockly.Xml.workspaceToDom(workspace);
    var xml_text = Blockly.Xml.domToText(xml);
    $.post(editor_uri,
    {xml: xml_text},
    function(status) {
        console.log(status);
    });
}

function loadWorkspace(editor_uri, workspace) {
    $.post(editor_uri, function(xml) {
        var dom = Blockly.Xml.textToDom(xml);
        Blockly.Xml.domToWorkspace(dom, workspace);
    });
}

Blockly.HSV_SATURATION = 0.86;
Blockly.HSV_VALUE = 0.86;

