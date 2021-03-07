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

def test_offset_setter():
    rotorI = __buildRotorI()
    expected = 1
    rotorI.setOffset(expected)
    assert rotorI.offset == expected

def __buildRotorI():
    rotorIMapping = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    rotorI = rotor.Rotor("Rotor I", rotorIMapping, "A")
    return rotorI
