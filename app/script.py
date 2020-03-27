from flask import Flask, request, render_template
from dotenv import load_dotenv
import os


def distance(a, b):
    n, m = len(a), len(b)
    if n > m:
        a, b = b, a
        n, m = m, n

    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if a[j - 1] != b[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]

if __name__ == '__main__':
	load_dotenv()
	HOST_IP = os.getenv("HOST_IP")
	PORT = os.getenv("PORT")

	app = Flask(__name__)

	@app.after_request
	def after_request(response):
	    r"""Fix access"""
	    response.headers.add('Access-Control-Allow-Origin', '*')
	    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
	    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
	    return response

	@app.route('/')
	def index():
	    """ Displays the index page accessible at '/'
	    """
	    return render_template("index.html")


	@app.route('/getMessage', methods=['GET'])
	def get_message():
	    message = request.args.get("message")

	    bot_message = message[::-1]

	    return bot_message


	app.run(debug=True, host=HOST_IP, port=PORT)
