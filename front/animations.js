function search(element) {
    let message_field = document.getElementById('message-field');
    if ((event.key === 'Enter') || (element.type == 'image')) {
        p(message_field.value);
        console.log(message_field.value);
        message_field.value = "";
    }
}
function p(m) {

    let message_field = document.getElementById('messages_field')

    let message_box = document.createElement('div');
    message_box.className = 'message-box';

    let user_message = document.createElement('div');
    user_message.className = 'user-message';

    let text = document.createElement('p');
    text.innerHTML = m;

    user_message.appendChild(text);
    message_box.appendChild(user_message);
    message_field.appendChild(message_box);

    var elem = document.getElementById('messages_field');
    elem.scrollTop = elem.scrollHeight;
}