from flask import Flask, request
import config


app = Flask(__name__)


@app.route('/getMessage', methods=['GET'])
def data_update():
    message = request.args.get("message")
    bot_message = message[::-1]

    return bot_message


app.run(debug=True, host=config.HOST_IP, port=config.PORT)
