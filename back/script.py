from flask import Flask, request
import config


app = Flask(__name__)

@app.after_request
def after_request(response):
    r"""Fix access"""
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

@app.route('/getMessage', methods=['GET'])
def data_update():
    message = request.args.get("message")
    bot_message = message[::-1]

    return bot_message


app.run(debug=True, host=config.HOST_IP, port=config.PORT)
