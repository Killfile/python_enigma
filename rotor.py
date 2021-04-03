from alphabet import Alphabet
from wiring import Wiring, WiringFactory
from ringsetting import Ringsetting

class Rotor:
    def __init__(self, wiring, turnover):
        self.wiring = wiring
        self.ringSetting = Ringsetting("A")
        self.turnover = turnover
        self.offset = 0
    
    def setRingSetting(self, ringSetting):
        self.ringSetting.setting = ringSetting

    def advance(self):
        self.offset+=1
        self.offset = self.offset % Alphabet.length()
    
    def map(self, input):
        inputAfterApplyingRingSetting = self.ringSetting.mapCharacterIn(input)
        location = Alphabet.index(inputAfterApplyingRingSetting)
        location = (location + self.offset ) % Alphabet.length()
        
        mappedLocation = self.wiring.map(location)

        offsetMappedLocation = (Alphabet.length() + mappedLocation - self.offset) % Alphabet.length()
       # offsetMappedLocation = self.ringSetting.mapInt(offsetMappedLocation)
        output = Alphabet[offsetMappedLocation]
        outputAfterApplyingRingSetting = self.ringSetting.mapCharacterOut(output)
        return outputAfterApplyingRingSetting

    def reverseMap(self, input):
        inputAfterApplyingRingSetting = self.ringSetting.mapCharacterIn(input)
        location = Alphabet.index(inputAfterApplyingRingSetting)
        location = (location + self.offset) % Alphabet.length()
        
        mappedLocation = self.wiring.reverseMap(location)

        offsetMappedLocation = (Alphabet.length() + mappedLocation - self.offset ) % Alphabet.length()
        output =  Alphabet[offsetMappedLocation]
        outputAfterApplyingRingSetting = self.ringSetting.mapCharacterOut(output)
        return outputAfterApplyingRingSetting
    
    def isInTurnoverPosition(self):
        return Alphabet[self.offset] == self.turnover

class RotorFactory:
    turnovers = dict([
        ("RotorI", 16),     #Q
        ("RotorII", 4),     #E
        ("RotorIII", 21),   #V
        ("ReflectorA",""),
        ("ReflectorB",""),
        ("NoOp", "")
    ])
    @staticmethod
    def Rotor(name):
        wiringConfiguration = WiringFactory.Wiring(name)
        turnover = RotorFactory.turnovers[name]
        return Rotor(wiringConfiguration, turnover)
        
