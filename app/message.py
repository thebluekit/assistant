from string import Template
from fuzzywuzzy import fuzz
from copy import deepcopy
import re
import random


# TODO: abstract method of cypher commands
def get_key_words(cmd, graph):
    """
    get key words of commands
    :param cmd: command, which key words you need to get
    :type cmd: str
    :param graph: graph from db
    :type graph: py2neo.database.Graph
    :return: list of key words
    :rtype: list
    """
    command = "Command"
    word = "word"
    query_template = Template("MATCH (:$command {name: '$cmd'})-[r:$word]-(res) RETURN res")
    query = query_template.substitute(cmd=cmd, command=command, word=word)

    query_result = graph.run(query).data()

    words_li = []
    for element in query_result:
        words_li.append(element["res"]["name"])

    return words_li


def get_answers(cmd, graph):
    """
    get key words of commands
    :param cmd: command, which key words you need to get
    :type cmd: str
    :param graph: graph from db
    :type graph: py2neo.database.Graph
    :return: list of key words
    :rtype: list
    """
    command = "Command"
    answer = "answer"
    query_template = Template("MATCH (:$command {name: '$cmd'})-[r:answer]-(res) RETURN res")
    query = query_template.substitute(cmd=cmd, command=command, answer=answer)

    query_result = graph.run(query).data()

    answers_li = []
    for element in query_result:
        answers_li.append(element["res"]["name"])

    return random.choice(answers_li)


def get_commands(graph):
    """
    get all commands of bot
    :param graph: graph from db
    :type graph: py2neo.database.Graph
    :return: list of commands
    :rtype: list
    """
    command = "Command"
    query_template = Template("MATCH (n:$command) RETURN n")
    query = query_template.substitute(command=command)
    query_result = graph.run(query).data()

    commands_li = []
    for element in query_result:
        commands_li.append(element['n']["name"])
    return commands_li


def get_alias(graph):
    """
    get all alias of bot
    :param graph: graph from db
    :type graph: py2neo.database.Graph
    :return: list of alias
    :rtype: list
    """
    alias = "alias"
    word = "word"
    query_template = Template("MATCH (:$alias {name: '$alias'})-[r:$word]-(res) RETURN res")
    query = query_template.substitute(alias=alias, word=word)
    query_result = graph.run(query).data()
    alias_li = []
    for element in query_result:
        alias_li.append(element['res']["name"])
    return alias_li


def get_tbr(graph):
    """
    get all words, that will be removed in message
    :param graph: graph from db
    :type graph: py2neo.database.Graph
    :return: list of words
    :rtype: list
    """
    tbr = "tbr"
    tbr_name = "to_be_removed"
    word = "word"
    query_template = Template("MATCH (:$tbr {name: '$tbr_name'})-[r:$word]-(res) RETURN res")
    query = query_template.substitute(tbr=tbr, tbr_name=tbr_name, word=word)
    query_result = graph.run(query).data()

    tbr_li = []
    for element in query_result:
        tbr_li.append(element['res']["name"])
    return tbr_li


class Messages:
    # percent of recognized words in message
    RECOGNIZED_PERCENT = 2/3
    # boundary value for recognize one word
    WORD_THRESHOLD = 80

    def __init__(self, graph):
        """
        init graph, get alias and tbr lists
        :param graph: graph from db
        :type graph: py2neo.database.Graph
        """
        self.graph = graph
        self.alias_li = get_alias(self.graph)
        self.tbr_li = get_tbr(self.graph)

    def convert(self, text):
        """
        convert message text to list of words
        with the removal of unnecessary words
        :param text: message text
        :type text: str
        :return: list of words
        :rtype: list
        """
        text = text.lower()
        # remove special characters
        text = re.sub(r'[^A-zА-я0-9 ]', '', text)
        message_li = text.split(' ')

        # remove alias and tbr words from message
        for word in self.alias_li:
            message_li = list(filter(word.__ne__, message_li))
        for word in self.tbr_li:
            message_li = list(filter(word.__ne__, message_li))
        return message_li

    def recognize(self, text):
        """
        recognize commands from list of words
        by keys words
        :param text: text
        :type text: str
        :return: name of command
        :rtype: str
        """
        words_li = self.convert(text)

        if len(words_li) == 0:
            rc = {'cmd': 'error', "recognized_words": 0}
            return rc['cmd']

        rc = {'cmd': '', "recognized_words": 0}
        commands_li = get_commands(self.graph)
        for command in commands_li:
            rc_tmp = {"cmd": command, "recognized_words": 0}
            key_words = get_key_words(command, self.graph)
            for key_word in key_words:
                for word in words_li:
                    vrt = fuzz.ratio(word, key_word)
                    if vrt > self.WORD_THRESHOLD:
                        rc_tmp["recognized_words"] += 1
            if rc_tmp['recognized_words'] > rc["recognized_words"]:
                rc = deepcopy(rc_tmp)

        if rc["recognized_words"] / len(words_li) < self.RECOGNIZED_PERCENT:
            rc = {'cmd': 'error', "recognized_words": 0}
        return rc['cmd'], get_answers(rc["cmd"], self.graph)
