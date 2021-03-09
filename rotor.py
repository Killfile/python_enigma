from alphabet import Alphabet

class Rotor:
    def __init__(self, name, mapping):
        self.name = name
        self.mapping = mapping

    def map(self, location):
        return self.__mapCharacterAcrossSetsWithOffset(location, Alphabet.set, self.mapping)
    
    def reverseMap(self, location):
        return self.__mapCharacterAcrossSetsWithOffset(location, self.mapping, Alphabet.set)
    
    def __mapCharacterAcrossSetsWithOffset(self, location, inputMap, outputMap):
        mappedCharacter = outputMap[location]
        mappedLocation = inputMap.index(mappedCharacter)
        return mappedLocation

    def __logMappingOnReturn(self, input, output):
        print("[%s] %s -> %s " %(self.name,input,output))
        return output


class RotorFactory:
    rotors = dict([
        ("RotorI", "EKMFLGDQVZNTOWYHXUSPAIBRCJ"),
        ("NoOp", Alphabet.set)
    ])
    @staticmethod
    def Rotor(name):
        return Rotor(name, RotorFactory.rotors[name])

