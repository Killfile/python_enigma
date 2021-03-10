import wiring
from rotor import Rotor, RotorFactory
from alphabet import Alphabet

def test_offset_mapping():
    given = "A"
    expected = "J"
    rotorI = RotorFactory.Rotor("RotorI")
    rotorI.offset = 1
    actual = rotorI.map(given)
    assert expected == actual

def test_offset_reverse_mapping():
    given = "K"
    expected = "D"
    rotorI = RotorFactory.Rotor("RotorI")
    rotorI.offset = 1
    actual = rotorI.reverseMap(given)
    assert expected == actual

