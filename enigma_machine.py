from plugboard import Plugboard
from rotor_assembly import RotorAssembly
import rotor

class EnigmaMachine:
    def __init__(self, rotorNames, reflectorName, plugboard):
        rotors = []
        for rotorName in rotorNames:
            rotors.append(rotor.RotorFactory.Rotor(rotorName))
        self.rotor_assembly = RotorAssembly(rotors, rotor.RotorFactory.Rotor(reflectorName))
        self.plugboard = plugboard
    
    def setRotorPosition(self, positions):
        self.rotor_assembly.setRotorPosition(positions)
    
    def crypt(self, input):
        output = ""
        for character in input:
            output+= self.rotor_assembly.crypt(character)
        
        return output
            
