import re
import pymorphy2

SPLIT_RGX = re.compile(r'\w+', re.U)


class NormalDict(dict):

    def __init__(self):
        super().__init__()
        self.morph = pymorphy2.MorphAnalyzer()

    def __getitem__(self, item):
        try:
            return super().__getitem__(item)
        except KeyError:
            self[item] = self.morph.normal_forms(item)[0]
            return self.morph.normal_forms(item)[0]


dct = NormalDict()


def normal(s):
    return dct[s]


def split(text):
    return re.findall(SPLIT_RGX, text)


def extract_words(words):
    return [dct[s] for s in words]
