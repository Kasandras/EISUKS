import json
from setup import path_to_project


class Data(object):

    def __init__(self, file_name):
        self._data = self.load(file_name)

    def load(self, file_name):
        filename = r"{0}\data\{1}.json".format(path_to_project, file_name)
        self._data = json.loads(open(filename, encoding="utf8").read())
        return self._data

    def load_by_value(self, parent, key, value):
        for i in self._data[parent]:
            if value == i[key]:
                return i
        return None

    def load_by_number(self, parent, number=0):
        return self._data[parent][number]
