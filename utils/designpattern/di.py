class DI:
    def __init__(self):
        self.dictionary = {}

    def get_ins(self, key):
        return self.dictionary[key]

    def set_ins(self, key, ins):
        self.dictionary[key] = ins