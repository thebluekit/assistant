from flask import Flask, request, render_template
from dotenv import load_dotenv
import os

from assistant import AssistantController
from db_controller import DBController
from dashboard import Dashboard

if __name__ == '__main__':
    # load and setting up dot env values
    load_dotenv()
    HOST_IP = os.getenv("HOST_IP")
    PORT = os.getenv("PORT")
    DB_LINK = os.getenv("DB_LINK")
    DB_PASSWORD = os.getenv("DB_PASSWORD")

    db_controller = DBController(DB_LINK, DB_PASSWORD)
    assistant_controller = AssistantController(db_controller)

    # bot = Assistant(db_controller.graph)
    dashboard = Dashboard(db_controller)

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


    @app.route('/dashboard')
    def admin():
        # displays dashboard page
        return render_template("admin.html")


    @app.route('/addCommand', methods=['GET'])
    def add_command():
        command_name = request.args.get("cname")
        key_words = request.args.get("kw")
        answers = request.args.get("answers")

        dashboard.add_command(command_name, key_words, answers)

        return "OK"

    @app.route('/deleteCommand', methods=['GET'])
    def delete_command():
        command_name = request.args.get("cname")

        dashboard.delete_command(command_name)

        return "OK"

    @app.route('/getMessage', methods=['GET'])
    def get_message():
        message = request.args.get("message")
        bot_message = assistant_controller.assistant.response(message)
        # bot_message = bot.response(message)
        return bot_message

    app.run(debug=True, host=HOST_IP, port=PORT)
