from alphabet import Alphabet
from rotorComponent import RotorComponent

class Ringsetting(RotorComponent):    
    def __init__(self, inner: RotorComponent, setting):
        super().__init__(inner)
        self.setRingSetting(setting)

    def mapIn(self, input):
        inputIndex = Alphabet.index(input)
        outputIndex = (inputIndex - self.setting) % Alphabet.length()
        return Alphabet[outputIndex]
    
    def mapOut(self, input):
        inputIndex = Alphabet.index(input)
        outputIndex = (inputIndex + self.setting) % Alphabet.length()
        return Alphabet[outputIndex]
    
    def reverseMapIn(self, input):
        return self.mapIn(input)
    
    def reverseMapOut(self, input):
        return self.mapOut(input)
    
    def setRingSetting(self, setting):
        self.setting = Alphabet.index(setting)