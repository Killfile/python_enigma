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

ringsetting_data = [
                        ("A",1,0,"K")
                        ,("A",6,24,"A")
                    ]
@pytest.mark.parametrize("given, ringSetting, offset, expected", ringsetting_data)
def test_ringsetting_mapping(given, ringSetting, offset, expected):
    rotorI = RotorFactory.Rotor("RotorI")
    rotorI.setRingSetting(ringSetting)
    rotorI.offset = offset
    actual = rotorI.map(given)
    assert expected == actual


def test_custom_wiring():
    rotorI = RotorFactory.Rotor("NoOp")
    rotorI.wiring.mapping = "BDAC"
    assert "D" == rotorI.map("B")

def test_custom_wiring_with_ringsetting():
    rotorI = RotorFactory.Rotor("NoOp")
    rotorI.wiring.mapping = "BDAC"
    rotorI.setRingSetting(1)
    assert "B" == rotorI.map("D")

def test_ringsetting_reversemapping():
    given = "K"
    expected = "A"
    offset = 0
    ringSetting = 1
    rotorI = RotorFactory.Rotor("RotorI")
    rotorI.setRingSetting(ringSetting)
    rotorI.offset = offset
    actual = rotorI.reverseMap(given)
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