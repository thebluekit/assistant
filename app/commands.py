from pycbrf.toolbox import ExchangeRates
import datetime


class CommandController:
    def __init__(self):
        self.all_commands = Commands()

    def execute_cmd(self, command_name, answer_template):
        args_li = self.__get_args(command_name)
        answer = self.__set_args(answer_template, args_li)
        return answer

    def __get_args(self, command_name):
        return getattr(self.all_commands, command_name)()

    @staticmethod
    def __set_args(answer_template, args_li):
        return answer_template % tuple(args_li)


class Commands:
    @staticmethod
    def time():
        now = datetime.datetime.now()
        if len(str(now.minute)) == 1:
            message = str(now.hour) + ":0" + str(now.minute)
        else:
            message = str(now.hour) + ":" + str(now.minute)
        return [message]

    @staticmethod
    def dollar_rate():
        now = datetime.datetime.now()
        rates = ExchangeRates(str(now.date()))
        message = str(round(float(rates['USD'].value), 2))
        return [message]

    @staticmethod
    def weather():
        return [0]

    @staticmethod
    def static_command():
        return []

    def __getattr__(self, item):
        return self.static_command
