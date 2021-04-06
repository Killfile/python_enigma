import abc

class RotorComponent(abc.ABC):
    def __init__(self, inner):
         self.inner = inner

    def map(self, input):
        inbound = self.mapIn(input)
        outbound = self.inner.map(inbound)
        output = self.mapOut(outbound)
        return output

    def reverseMap(self, input):
        inbound = self.reverseMapIn(input)
        outbound = self.inner.reverseMap(inbound)
        output = self.reverseMapOut(outbound)
        return output

    def advance(self):
        return self.inner.advance()

    def getRotorPosition(self):
        return self.inner.getRotorPosition()

    def setRingSetting(self, setting):
        return self.inner.setRingSetting(setting)

    def setOffSet(self, setting):
        return self.inner.setOffSet(setting)

    @abc.abstractmethod
    def mapIn(self, input):
        pass

    @abc.abstractmethod
    def mapOut(self, input):
        pass

    @abc.abstractmethod
    def reverseMapIn(self, input):
        pass

    @abc.abstractmethod
    def reverseMapOut(self, input):
        pass