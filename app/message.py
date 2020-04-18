from fuzzywuzzy import fuzz
from copy import deepcopy
import re
import random


class Messages:
    # percent of recognized words in message
    RECOGNIZED_PERCENT = 2/3
    # boundary value for recognize one word
    WORD_THRESHOLD = 80

    def __init__(self, db_controller, finder):
        """
        init graph, get alias and tbr lists
        :param graph: graph from db
        :type graph: py2neo.database.Graph
        """
        self.graph = db_controller.graph
        self.finder = finder

        self.alias_li = self.get_alias()
        self.tbr_li = self.get_tbr()

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
            rc = {'cmd': 'not_recognized', "recognized_words": 0}
            return rc['cmd']

        rc = {'cmd': '', "recognized_words": 0}
        commands_li = self.get_all_commands()
        for command in commands_li:
            rc_tmp = {"cmd": command, "recognized_words": 0}
            key_words = self.get_key_words_of_command(command)
            for key_word in key_words:
                for word in words_li:
                    vrt = fuzz.ratio(word, key_word)
                    if vrt > self.WORD_THRESHOLD:
                        rc_tmp["recognized_words"] += 1
            if rc_tmp['recognized_words'] > rc["recognized_words"]:
                rc = deepcopy(rc_tmp)

        if rc["recognized_words"] / len(words_li) < self.RECOGNIZED_PERCENT:
            rc = {'cmd': 'not_recognized', "recognized_words": 0}
        return rc['cmd'], self.get_answer(rc["cmd"])

    def get_alias(self):
        return self.finder.get_related_nodes("alias", "alias", "word")

    def get_tbr(self):
        return self.finder.get_related_nodes("to_be_removed", "tbr", "word")

    def get_all_commands(self):
        return self.finder.get_all_nodes("Command")

    def get_key_words_of_command(self, command):
        return self.finder.get_related_nodes(command, "Command", "word")

    def get_answer(self, command):
        all_answers_templates = self.finder.get_related_nodes(command, "Command", "answer")
        if len(all_answers_templates) == 0:
            return all_answers_templates
        else:
            return random.choice(all_answers_templates)
