from alphabet import Alphabet
from wiring import Wiring, WiringFactory
from ringsetting import Ringsetting
from rotorComponent import RotorComponent
from offset import Offset

class Rotor(RotorComponent):
    def __init__(self, rotorComponent: RotorComponent, turnover):
        self.rotorStack = rotorComponent
        self.turnover = turnover
        self.offset = 0
    
    def setRingSetting(self, ringSetting):
        self.ringSetting.setting = ringSetting

    def advance(self):
        self.rotorStack.advance()
    
    def mapIn(self, input):
        pass

    def mapOut(self, input):
        pass

    def map(self, input):
        return self.rotorStack.map(input)

    def reverseMap(self, input):
        return self.rotorStack.reverseMap(input)
    
    def reverseMapIn(self, input):
        pass

    def reverseMapOut(self, input):
        pass
    
    def isInTurnoverPosition(self):
        return self.rotorStack.getRotorPosition() == Alphabet[self.turnover]

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
        offset = Offset(wiringConfiguration, "A")
        ringSetting = Ringsetting(offset, "A")
        
        turnover = RotorFactory.turnovers[name]
        return Rotor(ringSetting, turnover)
        
