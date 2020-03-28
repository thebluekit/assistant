from flask import Flask, request, render_template
from dotenv import load_dotenv
from fuzzywuzzy import fuzz
from copy import deepcopy
import datetime
import os

opts = {
    "cmds": {
    }
}


def recognize_cmd(message):
    message_li = converted_message(message)
    rc = {'cmd': '', "recognized_words": 0}
    for command, key_words in opts['cmds'].items():
        rc_tmp = {"cmd": command, "recognized_words": 0}
        for key_word in key_words:
            for word in message_li:
                vrt = fuzz.ratio(word, key_word)
                if vrt > 90:
                    rc_tmp["recognized_words"] += 1
        if rc_tmp['recognized_words'] > rc["recognized_words"]:
            rc = deepcopy(rc_tmp)

    if rc["recognized_words"] / len(message_li) < 0.6666:
        rc = {'cmd': '', "recognized_words": 0}
    return rc


def converted_message(message):
    message_li = message.split(' ')
    return message_li


def execute_cmd(cmd):
    return "command not found"


if __name__ == '__main__':
    load_dotenv()
    HOST_IP = os.getenv("HOST_IP")
    PORT = os.getenv("PORT")

    app = Flask(__name__)

    @app.after_request
    def after_request(response):
        r"""Fix access"""
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization')
        response.headers.add(
            'Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
        return response

    @app.route('/')
    def index():
        """ Displays the index page accessible at '/'
        """
        return render_template("index.html")

    @app.route('/getMessage', methods=['GET'])
    def get_message():
        message = request.args.get("message")
        cmd = recognize_cmd(message)
        bot_message = execute_cmd(cmd['cmd'])
        return bot_message

    app.run(debug=True, host=HOST_IP, port=PORT)
