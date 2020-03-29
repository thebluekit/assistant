import datetime

ERROR = "Команда не распознана"


def error():
    return ERROR


def ctime():
    now = datetime.datetime.now()
    message = str(now.hour) + ":" + str(now.minute)
    return message


def dollar_rate():
    return "dollar_rate"


def weather():
    return "weather"
