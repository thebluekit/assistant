let messages = document.getElementsByClassName("message-box");
let message_field = document.getElementById('messages_field');

let blanked_bot_message = messages[0].cloneNode(true);
let blanked_user_message = messages[1].cloneNode(true);

message_field.innerHTML = "";

blanked_bot_message.style.visibility = "visible";
blanked_user_message.style.visibility = "visible";

SERVER_URL = "";
GET_MESSAGE_URL = SERVER_URL + "getMessage?message=";

function send_message(element) {
    let message_field = document.getElementById('message-field');
    if ((event.key === 'Enter') || (element.type == 'image')) {
        show_user_message(message_field.value);

        let get_message = new XMLHttpRequest();
        get_message.open("GET", GET_MESSAGE_URL + message_field.value, true);
        get_message.onload = function() {
            show_bot_message(get_message.responseText);
        }
        get_message.send(null);

        message_field.value = "";
    }
}

function show_user_message(message) {
    let tmp_blanked_user_message = blanked_user_message.cloneNode(true);
    let text = tmp_blanked_user_message.getElementsByTagName('p')[0]
    text.innerHTML = message;

    message_field.appendChild(tmp_blanked_user_message);

    let elem = document.getElementById('messages_field');
    elem.scrollTop = elem.scrollHeight;
}

function show_bot_message(message) {
    let tmp_blanked_bot_message = blanked_bot_message.cloneNode(true);
    let text = tmp_blanked_bot_message.getElementsByTagName('p')[0]
    text.innerHTML = message;

    message_field.appendChild(tmp_blanked_bot_message);

    let elem = document.getElementById('messages_field');
    elem.scrollTop = elem.scrollHeight;
}