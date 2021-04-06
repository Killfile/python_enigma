from alphabet import Alphabet
from rotorComponent import RotorComponent

class Wiring(RotorComponent):
    def __init__(self, name, mapping):
        self.name = name
        self.mapping = mapping

    def map(self, input):
        return self.__mapCharacterAcrossSetsWithOffset(Alphabet.index(input), Alphabet.set, self.mapping)
    
    def mapIn(self, input):
        pass

    def mapOut(self, input):
        pass
    
    def reverseMap(self, input):
        return self.__mapCharacterAcrossSetsWithOffset(Alphabet.index(input), self.mapping, Alphabet.set)
    
    def reverseMapIn(self, input):
        pass

    def reverseMapOut(self, input):
        pass

    def advance(self):
        return

    def __mapCharacterAcrossSetsWithOffset(self, location, inputMap, outputMap):
        mappedCharacter = outputMap[location % len(Alphabet.set)]
        mappedLocation = inputMap.index(mappedCharacter)
        return Alphabet[mappedLocation]

    def __logMappingOnReturn(self, input, output):
        print("[%s] %s -> %s " %(self.name,input,output))
        return output

class WiringFactory:
    wirings = dict([
        ("RotorI", "EKMFLGDQVZNTOWYHXUSPAIBRCJ"),
        ("RotorII", "AJDKSIRUXBLHWTMCQGZNPYFVOE"),
        ("RotorIII", "BDFHJLCPRTXVZNYEIWGAKMUSQO"),
        ("ReflectorA","EJMZALYXVBWFCRQUONTSPIKHGD"),
        ("ReflectorB","YRUHQSLDPXNGOKMIEBFZCWVJAT"),
        ("NoOp", Alphabet.set)
    ])
    @staticmethod
    def Wiring(name):
        wiringConfiguration = WiringFactory.wirings[name]
        return Wiring(name, wiringConfiguration)

