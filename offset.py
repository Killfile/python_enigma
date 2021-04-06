from alphabet import Alphabet
from rotorComponent import RotorComponent

class Offset(RotorComponent):
    def __init__(self, inner: RotorComponent, offset):
        super().__init__(inner)
        self.setOffSet(offset)
    
    def advance(self):
        self.offset+=1
        self.offset = self.offset % Alphabet.length()
        return super().advance()

    def getRotorPosition(self):
        return Alphabet[self.offset]

    def mapIn(self, input):
        inputIndex = Alphabet.index(input)
        outputIndex = (inputIndex + self.offset) % Alphabet.length()
        return Alphabet[outputIndex]
    
    def mapOut(self, input):
        inputIndex = Alphabet.index(input)
        outputIndex = (inputIndex - self.offset) % Alphabet.length()
        return Alphabet[outputIndex]

    def reverseMapIn(self, input):
        return self.mapIn(input)

    def reverseMapOut(self, input):
        return self.mapOut(input)

    def setOffSet(self, setting):
        self.offset = Alphabet.index(setting)