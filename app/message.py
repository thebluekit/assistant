from fuzzywuzzy import fuzz
from copy import deepcopy
import json
import re


class Messages:
    RECOGNIZED_PERCENT = 2/3
    WORD_THRESHOLD = 90

    def __init__(self, package_path):
        self.opts = {}
        self.load_commands_pack(package_path)

    def load_commands_pack(self, path):
        with open(path) as json_file:
            self.opts = json.load(json_file)

    def convert(self, text):
        text = text.lower()
        text = re.sub(r'[^A-zА-я0-9 ]', '', text)
        message_li = text.split(' ')

        for word in self.opts["alias"]:
            message_li = list(filter(word.__ne__, message_li))
        for word in self.opts["tbr"]:
            message_li = list(filter(word.__ne__, message_li))
        return message_li

    def recognize(self, text):
        words_li = self.convert(text)

        if len(words_li) == 0:
            rc = {'cmd': 'Error', "recognized_words": 0}
            return rc['cmd']

        rc = {'cmd': '', "recognized_words": 0}
        for command, key_words in self.opts['commands'].items():
            rc_tmp = {"cmd": command, "recognized_words": 0}
            for key_word in key_words:
                for word in words_li:
                    vrt = fuzz.ratio(word, key_word)
                    if vrt > self.WORD_THRESHOLD:
                        rc_tmp["recognized_words"] += 1
            if rc_tmp['recognized_words'] > rc["recognized_words"]:
                rc = deepcopy(rc_tmp)

        if rc["recognized_words"] / len(words_li) < self.RECOGNIZED_PERCENT:
            rc = {'cmd': 'Error', "recognized_words": 0}
        return rc['cmd']

