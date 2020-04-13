let add_field = document.getElementById('add-content');
let add_field_button = document.getElementById('add-content-btn');

let add_field_style = add_field.style;
// let add_container = document.getElementById('add-container');
// console.log(add_container)

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

	a = command_name.value;
	b = key_words.value;
	t = ADD_COMMAND_URL + `cname=${a}&kw=${b}&answers=none`
	console.log(t);
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