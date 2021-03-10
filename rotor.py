from alphabet import Alphabet
from wiring import Wiring, WiringFactory

class Rotor:
    def __init__(self, wiring, turnover):
        self.wiring = wiring
        self.turnover = turnover
        self.offset = 0
    
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

class RotorFactory:
    turnovers = dict([
        ("RotorI", "Q"),
        ("NoOp", "")
    ])
    @staticmethod
    def Rotor(name):
        wiringConfiguration = WiringFactory.Wiring(name)
        turnover = RotorFactory.turnovers[name]
        return Rotor(wiringConfiguration, turnover)
