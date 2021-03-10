import pytest
import wiring
from alphabet import Alphabet

def test_zero_offset_mapping():
    given = "A"
    expected = "E"
    rotorI = __getRotorIWiring()
    actual = rotorI.map(Alphabet.index(given))
    assert Alphabet.index(expected) == actual

def test_reverse_mapping():
    given = Alphabet.index("E")
    expected = Alphabet.index("A")
    rotorI_wiring = __getRotorIWiring()
    actual = rotorI_wiring.reverseMap(given)
    assert expected == actual

def test_noop_with_zero_offset():
    given = Alphabet.index("A")
    expected = Alphabet.index("A")
    noopRotor = __getNoOpWiring()
    actual = noopRotor.map(given)
    assert expected == actual

def __getRotorIWiring():
    return wiring.WiringFactory.Wiring("RotorI")

def __getNoOpWiring():
    noopRotor = wiring.WiringFactory.Wiring("NoOp")
    return noopRotor
