from message import Messages
import commands


class Assistant:
    # TODO: generation of session_id
    def __init__(self,  db_graph, session_id="default", gender="female"):
        """
            constructor of assistant class
            :param session_id: id of session
            :param gender: gender of assistant
            :type session_id: str, unique generated key
            :type gender: str, "male" or "female"
        """
        self.session_id = session_id
        self.gender = gender

        # initialization of message
        self.message = Messages(db_graph)

    def response(self, text):
        """
            message processing: recognition of cmd and take a response
            :param text: text of user message
            :type text: str
            :return: text of response
            :rtype: str

        """
        cmd = self.message.recognize(text)
        answer = self.execute_cmd(cmd)
        return answer

    @staticmethod
    def execute_cmd(cmd):
        """
            execute cmd from commands module
            :param cmd: name of method
            :type cmd: str
            :return: returned value of certain method
            :rtype: str

        """
        executed_message = getattr(commands, cmd)()
        return executed_message
