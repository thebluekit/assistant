from pycbrf.toolbox import ExchangeRates
import datetime
from string import Template

ERROR = "Команда не распознана"


def error(answer_template):
    return ERROR


def time(answer_template):
    now = datetime.datetime.now()
    message = str(now.hour) + ":" + str(now.minute)
    return message


def dollar_rate(answer_template):
    now = datetime.datetime.now()
    rates = ExchangeRates(str(now.date()))
    message = str(round(float(rates['USD'].value), 2))
    return message


def weather(answer_template):
    answer = answer_template.format(0)
    return answer
