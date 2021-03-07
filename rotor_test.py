import rotor

def test_rotor_mappings_are_set_on_init():
    mapping = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    testRotor = rotor.Rotor("test rotor", mapping)
    assert testRotor.mapping == mapping