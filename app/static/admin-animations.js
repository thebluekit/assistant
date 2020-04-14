let add_field = document.getElementById('add-content');
let add_field_button = document.getElementById('add-content-btn');
let add_field_style = add_field.style;

SERVER_URL = "";
ADD_COMMAND_URL = SERVER_URL + "addCommand?";

function popup() {
    add_field.style.bottom = "0%";
}

function popdown() {
    add_field.style = add_field_style;
}

function add_command() {
    let command_name = document.getElementById('name');
    let key_words = document.getElementById('key-words');
    let graph_value = `cname=${command_name.value}&kw=${key_words.value}&answers=345`

    let get_command_status = new XMLHttpRequest();
    get_command_status.open("GET", ADD_COMMAND_URL + graph_value, true);
    get_command_status.onload = function() {}
    get_command_status.send(null);
}

window.addEventListener('click', function(e) {
    if (add_field_button.contains(e.target)) {
        popdown();
    } else if (add_field.contains(e.target)) {
        popup();
    } else {
        popdown();
    }
});