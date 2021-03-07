class Rotor:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, name, mapping, turnover):
        self.name = name
        self.mapping = mapping

    def setOffset(self, offset):
        self.offset = offset

    def map(self, input):
        location = self.alphabet.index(input)
        mappingResult = self.mapping[location]
        return self.__logMappingOnReturn(input, mappingResult)
    
    def reverseMap(self, input):
        location = self.mapping.index(input)
        mappingResult = self.alphabet[location]
        return self.__logMappingOnReturn(input, mappingResult)

    def __logMappingOnReturn(self, input, output):
        print("[%s] %s -> %s " %(self.name,input,output))
        return output
