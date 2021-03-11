import pytest
from rotor_assembly import RotorAssembly
import rotor
from alphabet import Alphabet

position_data = [
    ([0,0,0],0,[0,0,0]), 
    ([0,0,0],1,[1,0,0]),
    ([21,0,0],1,[22,1,0]),
    ([21,4,0],1,[22,5,1])
    ]
@pytest.mark.parametrize("starting, advanceCount, expected", position_data)
def test_getRotorPosition(starting, advanceCount, expected):
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