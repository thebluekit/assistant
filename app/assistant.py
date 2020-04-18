from db_controller import DBFinder
from message import Messages
from commands import CommandController


class AssistantController:
    def __init__(self, db_controller):
        finder = DBFinder(db_controller)

        self.messages = Messages(db_controller, finder)
        self.commands = CommandController()

        self.assistant = Assistant(self.messages, self.commands)


class Assistant:
    # TODO: generation of session_id
    def __init__(self, messages, commands, session_id="default", gender="female"):
        """
            constructor of assistant class
            :param session_id: id of session
            :param gender: gender of assistant
            :type session_id: str, unique generated key
            :type gender: str, "male" or "female"
        """
        self.session_id = session_id
        self.gender = gender

        # self.finder = DBFinder()
        # initialization of message
        # self.message = Messages(db_graph)
        self.message = messages
        self.commands = commands

    def response(self, text):
        """
            message processing: recognition of cmd and take a response
            :param text: text of user message
            :type text: str
            :return: text of response
            :rtype: str

        """
        cmd, answer_template = self.message.recognize(text)
        answer = self.execute_cmd(cmd, answer_template)
        return answer

    def execute_cmd(self, cmd, answer_template):
        """
            execute cmd from commands module
            :param cmd: name of method
            :type cmd: str
            :return: returned value of certain method
            :rtype: str

        """
        executed_message = self.commands.execute_cmd(cmd, answer_template)
        # executed_message = getattr(commands, cmd)(answer_template)
        return executed_message
