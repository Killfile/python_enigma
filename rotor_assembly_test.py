import pytest
from rotor_assembly import RotorAssembly
import rotor
from alphabet import Alphabet

def test_getRotorPosition():
    rotors = [
        rotor.RotorFactory.Rotor("RotorIII"),
        rotor.RotorFactory.Rotor("RotorII"),
        rotor.RotorFactory.Rotor("RotorI")
    ]
    for i in range(0,3):
        rotors[i].offset = 0
    
    reflector = rotor.RotorFactory.Rotor("ReflectorA")
    rotorAssembly = RotorAssembly(rotors, reflector)

    positions = rotorAssembly.getRotorPosition()
    assert positions == [0,0,0]
    
position_data = [
    ([0,0,0],0,[0,0,0]), 
    ([0,0,0],1,[1,0,0]),
    ([21,0,0],1,[22,1,0]),
    ([21,4,0],1,[22,5,1])
    ]
@pytest.mark.parametrize("starting, advanceCount, expected", position_data)
def test_rotorAdvancement(starting, advanceCount, expected):
    rotors = [
        rotor.RotorFactory.Rotor("RotorIII"),
        rotor.RotorFactory.Rotor("RotorII"),
        rotor.RotorFactory.Rotor("RotorI")
    ]
    for i in range(0,3):
        rotors[i].offset = starting[i]
    
    reflector = rotor.RotorFactory.Rotor("ReflectorA")
    rotorAssembly = RotorAssembly(rotors, reflector)
    for i in range(advanceCount):
        rotorAssembly.crypt("A")

    positions = rotorAssembly.getRotorPosition()
    assert positions == expected

def test_crypt():
    rotors = [
        rotor.RotorFactory.Rotor("RotorIII"),
        rotor.RotorFactory.Rotor("RotorII"),
        rotor.RotorFactory.Rotor("RotorI")
    ]
    
    rotors[0].offset = 25
    rotors[1].offset = 0
    rotors[2].offset = 0
    
    reflector = rotor.RotorFactory.Rotor("ReflectorB")
    rotorAssembly = RotorAssembly(rotors, reflector)

    actual = rotorAssembly.crypt("A")

    assert "U" == actual