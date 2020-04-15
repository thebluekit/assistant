// Fields
let add_field = document.getElementById('add-content');
let add_field_style = add_field.style;
let add_field_dict = { "field": add_field, "style": add_field_style };

let delete_field = document.getElementById('delete-content');
let delete_field_style = delete_field.style;
let delete_field_dict = { "field": delete_field, "style": delete_field_style };

// Buttons
let add_field_button = document.getElementById('add-content-btn');
let delete_field_button = document.getElementById('delete-content-btn');

SERVER_URL = "";
ADD_COMMAND_URL = SERVER_URL + "addCommand?";
DELETE_COMMAND_URL = SERVER_URL + "deleteCommand?";

function popup(field_dict) {
    field_dict["field"].style.bottom = "0%";
}

function popdown(field_dict) {
    field_dict["field"].style = field_dict["style"];
}

function add_command() {
    let command_name = document.getElementById('add-command-name');
    let key_words = document.getElementById('key-words');
    let graph_value = `cname=${command_name.value}&kw=${key_words.value}&answers=None`

    let get_command_status = new XMLHttpRequest();
    get_command_status.open("GET", ADD_COMMAND_URL + graph_value, true);
    get_command_status.onload = function() {}
    get_command_status.send(null);
}

function delete_command() {
    let command_name = document.getElementById('delete-command-name');
    let graph_value = `cname=${command_name.value}`

    let get_command_status = new XMLHttpRequest();
    get_command_status.open("GET", DELETE_COMMAND_URL + graph_value, true);
    get_command_status.onload = function() {}
    get_command_status.send(null);
}

window.addEventListener('click', function(e) {
    if (add_field_button.contains(e.target)) {
        popdown(add_field_dict);
    } else if (add_field.contains(e.target)) {
        popup(add_field_dict);
    } else {
        popdown(add_field_dict);
    }
    
    if (delete_field_button.contains(e.target)) {
        popdown(delete_field_dict);
    } else if (delete_field.contains(e.target)) {
        popup(delete_field_dict);
    } else {
        popdown(delete_field_dict);
    }
});