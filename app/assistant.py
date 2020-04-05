from message import Messages
import commands


class Assistant:

    def __init__(self, session_id="default", sex="female"):
        self.session_id = session_id
        self.sex = sex

        self.message = Messages()

    def response(self, text):
        cmd = self.message.recognize(text)
        answer = self.execute_cmd(cmd)
        return answer

    @staticmethod
    def execute_cmd(cmd):
        executed_message = getattr(commands, cmd)()
        return executed_message
