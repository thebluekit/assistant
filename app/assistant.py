from message import Messages
import commands


class Assistant:
    FILES_PATH = "commands_packages/"

    def __init__(self, session_id="default", sex="female", language="RU"):
        self.session_id = session_id
        self.sex = sex

        self.message = Messages(package_path=self.FILES_PATH + language + ".json")

    def response(self, text):
        cmd = self.message.recognize(text)
        answer = self.execute_cmd(cmd)
        return answer

    @staticmethod
    def execute_cmd(cmd):
        executed_message = getattr(commands, cmd)()
        return executed_message
