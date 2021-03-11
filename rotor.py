from alphabet import Alphabet
from wiring import Wiring, WiringFactory

class Rotor:
    def __init__(self, wiring, turnover):
        self.wiring = wiring
        self.turnover = turnover
        self.offset = 0

    def advance(self):
        self.offset+=1
        self.offset = self.offset % len(self.wiring.mapping)
    
    def map(self, input):
        location = Alphabet.index(input)
        location = location + self.offset
        
        mappedLocation = self.wiring.map(location)

        offsetMappedLocation = mappedLocation - self.offset
        return Alphabet[offsetMappedLocation]

    def reverseMap(self, input):
        location = Alphabet.index(input)
        location = location + self.offset
        
        mappedLocation = self.wiring.reverseMap(location)

        offsetMappedLocation = mappedLocation - self.offset
        return Alphabet[offsetMappedLocation]
    
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
