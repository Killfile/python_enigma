import wiring
from offsetRotor import OffsetRotor
from alphabet import Alphabet

def test_offset_mapping():
    given = "A"
    expected = "J"
    rotorIwiring = wiring.WiringFactory.Wiring("RotorI")
    rotorI = OffsetRotor(rotorIwiring, "Z")
    rotorI.offset = 1
    actual = rotorI.map(given)
    assert expected == actual

def test_offset_reverse_mapping():
    given = "K"
    expected = "D"
    rotorIwiring = wiring.WiringFactory.Wiring("RotorI")
    rotorI = OffsetRotor(rotorIwiring, "Z")
    rotorI.offset = 1
    actual = rotorI.reverseMap(given)
    assert expected == actual

