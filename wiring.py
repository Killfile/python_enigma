from alphabet import Alphabet

class Wiring:
    def __init__(self, name, mapping):
        self.name = name
        self.mapping = mapping

    def map(self, location):
        return self.__mapCharacterAcrossSetsWithOffset(location, Alphabet.set, self.mapping)
    
    def reverseMap(self, location):
        return self.__mapCharacterAcrossSetsWithOffset(location, self.mapping, Alphabet.set)
    
    def __mapCharacterAcrossSetsWithOffset(self, location, inputMap, outputMap):
        mappedCharacter = outputMap[location % len(Alphabet.set)]
        mappedLocation = inputMap.index(mappedCharacter)
        return mappedLocation

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

