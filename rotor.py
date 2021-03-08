class Rotor:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, name, mapping, turnover):
        self.name = name
        self.mapping = mapping
        self.offset = 0

    def map(self, input):
        return self.__mapCharacterAcrossSetsWithOffset(input, self.alphabet, self.mapping)
    
    def reverseMap(self, input):
        return self.__mapCharacterAcrossSetsWithOffset(input, self.mapping, self.alphabet)
    
    def __mapCharacterAcrossSetsWithOffset(self, input, inputMap, outputMap):
        location = self.alphabet.index(input)
        #apply inbound offset
        location = location + self.offset
        #perform mapping
        mappedCharacter = outputMap[location]
        mappedLocation = inputMap.index(mappedCharacter)
        #apply outbound offset
        offsetMappedLocation = mappedLocation - self.offset
        return self.alphabet[offsetMappedLocation]

    def __logMappingOnReturn(self, input, output):
        print("[%s] %s -> %s " %(self.name,input,output))
        return output
    
    def __getCharacterFromMap(self, map, location):
        return map[(location-self.offset + len(map)) %len(map)]
