from string import Template


class Dashboard:
    # TODO: password check
    def __init__(self, graph, password=""):
        self.password = password
        self.graph = graph

    # TODO: answers
    def add_command(self, command_name, key_words, answers):
        key_words_li = self.convert_by_commas(key_words)
        answers_li = self.convert_by_commas(answers)

        command = "Command"
        word = "word"

        create_command = Template("CREATE (n: $command {name: '$command_name'}) RETURN n")
        create_key_word = Template("CREATE (n: $word {name: '$key_word'}) RETURN n")
        command_key_match = Template("MATCH (a:$command {name:'$command_name'}),"
                                     "(b:$word {name:'$key_word'}) MERGE (a)-[r:$word]->(b)")

        query = create_command.substitute(command=command, command_name=command_name)
        self.graph.run(query)

        for element in key_words_li:
            query = create_key_word.substitute(word=word, key_word=element)
            self.graph.run(query)

            query = command_key_match.substitute(command=command, command_name=command_name,
                                                 word=word, key_word=element)
            self.graph.run(query)

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
