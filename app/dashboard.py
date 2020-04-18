from db_controller import DBModifier, DBFinder


class Dashboard:
    # TODO: password check
    def __init__(self, db_controller, password=""):
        self.password = password

        self.modifier = DBModifier(db_controller)
        # self.finder = DBFinder(graph)

    # TODO: answers
    def add_command(self, command_name, key_words, answers):
        key_words_li = self.convert_by_commas(key_words)
        answers_li = self.convert_by_commas(answers)
        self.modifier.add_command(command_name, key_words_li, answers_li)

    def delete_command(self, command_name):
        self.modifier.delete_command(command_name)

    @staticmethod
    def convert_by_commas(text):
        text_li = text.split(',')
        converted_li = []
        for element in text_li:
            converted_element = element
            if len(element) == 0:
                continue
            if converted_element[0] == ' ':
                converted_element = converted_element[1:]
            if converted_element[len(converted_element) - 1] == ' ':
                converted_element = converted_element[:len(converted_element) - 1]
            converted_li.append(converted_element)
        return converted_li
