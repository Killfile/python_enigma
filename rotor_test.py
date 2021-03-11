import pytest
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

advance_data = [(0,1),(1,2),(24,25),(25,0)]
@pytest.mark.parametrize("given, expected",advance_data)
def test_advance(given, expected):
    rotor = RotorFactory.Rotor("RotorII")
    rotor.offset = given
    rotor.advance()
    assert expected == rotor.offset

turnover_test_data = [("A",False), ("B", False), ("C", True), ("D", False)]
@pytest.mark.parametrize("given, expected", turnover_test_data)
def test_turnover_detection(given, expected):
    noopRotor = RotorFactory.Rotor("NoOp")
    noopRotor.turnover = "C"
    noopRotor.offset = Alphabet.index(given)
    assert expected == noopRotor.isInTurnoverPosition()