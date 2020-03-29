from flask import Flask, request, render_template
from dotenv import load_dotenv
import os

from assistant import Assistant

if __name__ == '__main__':
    load_dotenv()
    HOST_IP = os.getenv("HOST_IP")
    PORT = os.getenv("PORT")

    bot = Assistant()

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
        bot_message = bot.response(message)
        return bot_message

    app.run(debug=True, host=HOST_IP, port=PORT)
