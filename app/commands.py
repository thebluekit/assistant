from pycbrf.toolbox import ExchangeRates
import datetime

ERROR = "Команда не распознана"


def error():
    return ERROR


def time():
    now = datetime.datetime.now()
    message = str(now.hour) + ":" + str(now.minute)
    return message


def dollar_rate():
    now = datetime.datetime.now()
    rates = ExchangeRates(str(now.date()))
    message = str(round(float(rates['USD'].value), 2))
    return message


def weather():
    return "weather"
