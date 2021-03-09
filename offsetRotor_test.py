import rotor
from offsetRotor import OffsetRotor
from alphabet import Alphabet

def test_offset_mapping():
    given = "A"
    expected = "J"
    wiring = rotor.RotorFactory.Rotor("RotorI")
    rotorI = OffsetRotor(wiring, "Z")
    rotorI.offset = 1
    actual = rotorI.map(given)
    assert expected == actual

def test_offset_reverse_mapping():
    given = "K"
    expected = "D"
    wiring = rotor.RotorFactory.Rotor("RotorI")
    rotorI = OffsetRotor(wiring, "Z")
    rotorI.offset = 1
    actual = rotorI.reverseMap(given)
    assert expected == actual