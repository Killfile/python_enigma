import rotor

class RotorAssembly:
    def __init__(self, rotors, reflector):
        self.rotors = rotors
        self.reflector = reflector

    def getRotorPosition(self):
        positions = []
        for rotor in self.rotors:
            positions.append(rotor.offset)
        return positions
    
    def crypt(self, character):
        for i in range(2,-1,-1):
            if i==0:
                self.rotors[i].advance()
            else:
                next_turnover = self.rotors[i-1].turnover
                next_offset = self.rotors[i-1].offset
                if next_turnover == next_offset:
                    self.rotors[i].advance()

        for rotor in self.rotors:
            character = rotor.map(character)
        
        character = self.reflector.map(character)

        for rotor in reversed(self.rotors):
            character = rotor.reverseMap(character)
        
        return character

