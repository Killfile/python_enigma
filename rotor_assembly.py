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
        self.rotors[0].advance()
        for rotor in self.rotors:
            character = rotor.map(character)
        
        character = self.reflector.map(character)

        for rotor in reversed(self.rotors):
            character = rotor.reverseMap(character)
        
        return character

