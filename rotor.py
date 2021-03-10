from alphabet import Alphabet

class Rotor:
    def __init__(self, wiring, turnover):
        self.wiring = wiring
        self.turnover = turnover
        self.offset = 0
    
    def map(self, input):
        location = Alphabet.index(input)
        location = location + self.offset
        
        mappedLocation = self.wiring.map(location)

        offsetMappedLocation = mappedLocation - self.offset
        return Alphabet[offsetMappedLocation]

    def reverseMap(self, input):
        location = Alphabet.index(input)
        location = location + self.offset
        
        mappedLocation = self.wiring.reverseMap(location)

        offsetMappedLocation = mappedLocation - self.offset
        return Alphabet[offsetMappedLocation]

