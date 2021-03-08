import rotor

def test_rotor_mappings_are_set_on_init():
    mapping = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    testRotor = rotor.Rotor("test rotor", mapping, "A")
    assert testRotor.mapping == mapping

def test_zero_offset_mapping():
    given = "A"
    expected = "E"
    rotorI = __buildRotorI()
    actual = rotorI.map(given)
    assert expected == actual

def test_zero_offset_reverse_mapping():
    given = "E"
    expected = "A"
    rotorI = __buildRotorI()
    actual = rotorI.reverseMap(given)
    assert expected == actual

def test_one_offset_mapping():
    given = "A"
    expected = "J"
    rotorI = __buildRotorI()
    rotorI.offset = 1
    actual = rotorI.map(given)
    assert expected == actual

def test_offset_reverse_mapping():
    given = "K"
    expected = "D"
    rotorI = __buildRotorI()
    rotorI.offset = 1
    actual = rotorI.reverseMap(given)
    assert expected == actual

def test_noop_with_zero_offset():
    given = "A"
    expected = "A"
    noopRotor = __buildNoOpRotor()
    actual = noopRotor.map(given)
    assert expected == actual

def test_noop_with_one_offset():
    given = "A"
    expected = "A"
    noopRotor = __buildNoOpRotor()
    noopRotor.offset = 1
    actual = noopRotor.map(given)
    assert expected == actual

def __buildRotorI():
    rotorIMapping = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    rotorI = rotor.Rotor("Rotor I", rotorIMapping, "A")
    return rotorI

def __buildNoOpRotor():
    rotorMapping = rotor.Rotor.alphabet
    noopRotor = rotor.Rotor("No Op Rotor", rotorMapping, "A")
    return noopRotor
