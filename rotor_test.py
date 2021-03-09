import rotor
from alphabet import Alphabet

def test_rotor_mappings_are_set_on_init():
    mapping = Alphabet.set
    testRotor = rotor.Rotor("test rotor", mapping)
    assert testRotor.mapping == mapping

def test_zero_offset_mapping():
    given = "A"
    expected = "E"
    rotorI = __buildRotorI()
    actual = rotorI.map(Alphabet.index(given))
    assert Alphabet.index(expected) == actual

def test_reverse_mapping():
    given = Alphabet.index("E")
    expected = Alphabet.index("A")
    rotorI = __buildRotorI()
    actual = rotorI.reverseMap(given)
    assert expected == actual

def test_noop_with_zero_offset():
    given = Alphabet.index("A")
    expected = Alphabet.index("A")
    noopRotor = __buildNoOpRotor()
    actual = noopRotor.map(given)
    assert expected == actual

def __buildRotorI():
    return rotor.RotorFactory.Rotor("RotorI")

def __buildNoOpRotor():
    noopRotor = rotor.RotorFactory.Rotor("NoOp")
    return noopRotor
