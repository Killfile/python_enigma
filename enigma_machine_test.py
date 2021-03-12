import enigma_machine
import plugboard

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