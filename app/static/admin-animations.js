let add_field = document.getElementById('add-content');
let add_field_button = document.getElementById('add-content-btn');

let add_field_style = add_field.style;
// let add_container = document.getElementById('add-container');
// console.log(add_container)

function popup() {
    add_field.style.bottom = "0%";
}

function popdown() {
    add_field.style = add_field_style;
}

function add_command() {
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