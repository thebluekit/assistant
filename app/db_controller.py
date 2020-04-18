from py2neo import Graph
from string import Template

# TODO: load dotenv class


class DBController:
    graph = None

    def __init__(self, ip_address, password):
        self.__connect(ip_address, password)

    def __connect(self, ip_address, password):
        self.graph = Graph(ip_address, password=password)

    def check_connection(self):
        # TODO: connection refused of db
        pass


class DBFinder:
    def __init__(self, db_controller):
        self.graph = db_controller.graph

    def get_all_nodes(self, node_type):
        query_template = Template("MATCH (n:$node_type) RETURN n")
        query = query_template.substitute(node_type=node_type)
        query_result = self.graph.run(query).data()

        nodes = [element['n']['name'] for element in query_result]
        return nodes

    def get_related_nodes(self, node_name, node_type, relation_type):
        query_template = Template("MATCH (:$node_type {name: '$node_name'})-[r:$relation_type]-(n) RETURN n")
        query = query_template.substitute(node_name=node_name,
                                          node_type=node_type,
                                          relation_type=relation_type)
        query_result = self.graph.run(query).data()

        nodes = [element['n']['name'] for element in query_result]
        return nodes


class DBModifier:
    def __init__(self, db_controller):
        self.graph = db_controller.graph

    # TODO: edit_command
    # TODO: answers

    def add_command(self, command_name, key_words_li, answers_li):
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

    def delete_command(self, command_name):
        command = "Command"
        word = "word"

        delete_command = Template("MATCH(a: $command{name: '$command_name'})"
                                  "OPTIONAL MATCH() - [rx] - (a)"
                                  "OPTIONAL MATCH(a) - [r: $word]->(m)"
                                  "OPTIONAL MATCH(m) - [ry] - ()"
                                  "DELETE rx, ry, r, a, m;")

        query = delete_command.substitute(command=command, command_name=command_name, word=word)
        self.graph.run(query)
