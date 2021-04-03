import enigma_machine
import plugboard

def test_offset_crypt():
    enigma = enigma_machine.EnigmaMachine(["RotorIII", "RotorII", "RotorI"], "ReflectorB", plugboard.Plugboard())
    enigma.setRotorPosition("AAA")    
    expected = "BDZGO"
    given = "AAAAA"
    actual = enigma.crypt(given)
    assert actual == expected

def test_long_crypt():
    enigma = enigma_machine.EnigmaMachine(["RotorIII", "RotorII", "RotorI"], "ReflectorB", plugboard.Plugboard())
    enigma.setRotorPosition("AAZ")
    input = "RBMLWDESXRUEPIWEDYLDZUKTTXGGKHLTFHKXLXFDJDMMI"
    expected = "MAYBEINVADINGRUSSIAINTHEWINTERWASNOTAGOODIDEA"
    assert expected == enigma.crypt(input)

def test_doublestep_crypt():
    enigma = enigma_machine.EnigmaMachine(["RotorIII", "RotorII", "RotorI"], "ReflectorB", plugboard.Plugboard())
    enigma.setRotorPosition("ADV")
    input = "UFSMHLYCAOFPCYDSBBVHLMNAWBXTSKANKGLZGBHIHAXIRU"
    expected = "IHEARTHEWEATHERINARGENTINAISNICETHISTIMEOFYEAR"
    assert expected == enigma.crypt(input)


def test_ringsetting_crypt():
    enigma = enigma_machine.EnigmaMachine(["RotorIII", "RotorII", "RotorI"], "ReflectorB", plugboard.Plugboard())
    enigma.rotor_assembly.rotors[0].setRingSetting(1)
    enigma.rotor_assembly.rotors[1].setRingSetting(1)
    enigma.rotor_assembly.rotors[2].setRingSetting(1)
    enigma.setRotorPosition("AAA")
    expected = "EWTYX"
    given = "AAAAA"
    actual = enigma.crypt(given)
    assert expected == actual

