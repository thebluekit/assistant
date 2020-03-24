// нахождение изначально пустых сообщений на странице сайта
let messages = document.getElementsByClassName("message-box");

// нахождение поля для вывода сообщений
let message_field = document.getElementById('messages_field');

// глубокое копирование боксов с сообщениями бота и пользователя
let blanked_bot_message = messages[0].cloneNode(true);
let blanked_user_message = messages[1].cloneNode(true);

// удаление пустых сообщений с поля ввода сообщений
message_field.innerHTML = "";

// установка видимости для боксов с сообщениями
blanked_bot_message.style.visibility = "visible";
blanked_user_message.style.visibility = "visible";

// константы адреса сервера и его API
SERVER_URL = "";
GET_MESSAGE_URL = SERVER_URL + "getMessage?message=";

/**
 * Функция отправки сообщений
 * По нажатию на иконку отправки или клавишу Enter отправляет запрос на сервер,
 * высвечивает сообщение пользователя на экран, а также сообщение-ответ от бота
 * @param {object} element - Элемент, от которого идет обращение об отправке сообщения
 */

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

/**
 * Функция вывода сообщения на экран от пользователя
 * @param {string} message - сообщение, которое необходимо высветить
 */
function show_user_message(message) {
    let tmp_blanked_user_message = blanked_user_message.cloneNode(true);
    let text = tmp_blanked_user_message.getElementsByTagName('p')[0]
    text.innerHTML = message;

    message_field.appendChild(tmp_blanked_user_message);

    let elem = document.getElementById('messages_field');
    elem.scrollTop = elem.scrollHeight;
}

/**
 * Функция вывода сообщения на экран от бота
 * @param {string} message - сообщение, которое необходимо высветить
 */
function show_bot_message(message) {
    let tmp_blanked_bot_message = blanked_bot_message.cloneNode(true);
    let text = tmp_blanked_bot_message.getElementsByTagName('p')[0]
    text.innerHTML = message;

    message_field.appendChild(tmp_blanked_bot_message);

    let elem = document.getElementById('messages_field');
    elem.scrollTop = elem.scrollHeight;
}