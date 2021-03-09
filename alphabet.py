class Alphabet:
    set = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    @staticmethod
    def index(character):
        return Alphabet.set.index(character)
    
    @staticmethod
    def __class_getitem__(key):
        return Alphabet.set[key]