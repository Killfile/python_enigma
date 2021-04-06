import pytest
import wiring
from alphabet import Alphabet

def test_zero_offset_mapping():
    given = "A"
    expected = "E"
    rotorI = __getRotorIWiring()
    actual = rotorI.map(given)
    assert expected == actual

def test_reverse_mapping():
    given = "E"
    expected = "A"
    rotorI_wiring = __getRotorIWiring()
    actual = rotorI_wiring.reverseMap(given)
    assert expected == actual

def test_noop_with_zero_offset():
    given = "A"
    expected = "A"
    noopRotor = __getNoOpWiring()
    actual = noopRotor.map(given)
    assert expected == actual

def __getRotorIWiring():
    return wiring.WiringFactory.Wiring("RotorI")

def __getNoOpWiring():
    noopRotor = wiring.WiringFactory.Wiring("NoOp")
    return noopRotor
