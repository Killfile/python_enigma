import rotor
from alphabet import Alphabet

class RotorAssembly:
    def __init__(self, rotors, reflector):
        self.rotors = rotors
        self.reflector = reflector

    def getRotorPosition(self):
        positions = ""
        for rotor in self.rotors:
            positions += rotor.rotorStack.getRotorPosition()
        positions = positions [::-1]
        return positions

    def setRotorPosition(self, position):
        for i, element in enumerate(position):
            self.rotors[2-i].rotorStack.setOffSet(element)
    
    def crypt(self, character):
        self.__advance_rotors()

        for rotor in self.rotors:
            character = rotor.map(character)
        
        character = self.reflector.map(character)

        for rotor in reversed(self.rotors):
            character = rotor.reverseMap(character)
        
        return character

    def __advance_rotors(self):
        for i in range(2,-1,-1):
            if i==0:
                self.rotors[i].advance()
            elif i==1 and self.rotors[i].isInTurnoverPosition():
                self.rotors[i].advance()
            else:
                next_turnover = self.rotors[i-1].turnover
                next_offset = self.rotors[i-1].offset
                if self.rotors[i-1].isInTurnoverPosition():
                    self.rotors[i].advance()

