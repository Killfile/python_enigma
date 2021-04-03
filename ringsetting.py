from alphabet import Alphabet

class Ringsetting:
    def __init__(self, setting):
        self.setting = Alphabet.index(setting)

    def mapCharacterIn(self, input):
        inputIndex = Alphabet.index(input)
        outputIndex = (inputIndex - self.setting) % Alphabet.length()
        return Alphabet[outputIndex]
    
    def mapCharacterOut(self, input):
        inputIndex = Alphabet.index(input)
        outputIndex = (inputIndex + self.setting) % Alphabet.length()
        return Alphabet[outputIndex]