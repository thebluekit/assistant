from flask import Flask, request, render_template
from dotenv import load_dotenv
import os

from assistant import Assistant
from admin import Admin

if __name__ == '__main__':

    # load and setting up dot env values
    load_dotenv()
    HOST_IP = os.getenv("HOST_IP")
    PORT = os.getenv("PORT")

    bot = Assistant()
    admin = Admin()

    app = Flask(__name__)

    @app.after_request
    def after_request(response):
        # fix access for javascript POST requests
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization')
        response.headers.add(
            'Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
        return response

    @app.route('/')
    def index():
        # displays the index page
        return render_template("index.html")


    @app.route('/admin')
    def admin():
        # displays admin page
        return render_template("admin.html")


    @app.route('/addCommand', methods=['GET'])
    def get_message():
        command_name = request.args.get("cname")
        key_words = request.args.get("kw")
        answers = request.args.get("answers")
        return "OK"

    @app.route('/getMessage', methods=['GET'])
    def get_message():
        message = request.args.get("message")
        bot_message = bot.response(message)
        return bot_message

    app.run(debug=True, host=HOST_IP, port=PORT)
