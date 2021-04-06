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
    
    reflector = rotor.RotorFactory.Rotor("ReflectorA")
    rotorAssembly = RotorAssembly(rotors, reflector)
    rotorAssembly.setRotorPosition("ABC")

    positions = rotorAssembly.getRotorPosition()
    assert positions == "ABC"
    
position_data = [
    ("AAA",0,"AAA"), 
    ("AAA",1,"AAB"),
    ("AAV",1,"ABW"),
    ("AEV",1,"BFW"),
    ("ADV",1,"AEW"),
    ("AEW",1,"BFX"), #doublestep
    ("BFX",1,"BFY")
    ]
@pytest.mark.parametrize("starting, advanceCount, expected", position_data)
def test_rotorAdvancement(starting, advanceCount, expected):
    rotors = [
        rotor.RotorFactory.Rotor("RotorIII"),
        rotor.RotorFactory.Rotor("RotorII"),
        rotor.RotorFactory.Rotor("RotorI")
    ]
        
    reflector = rotor.RotorFactory.Rotor("ReflectorA")
    rotorAssembly = RotorAssembly(rotors, reflector)

    rotorAssembly.setRotorPosition(starting)

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

    reflector = rotor.RotorFactory.Rotor("ReflectorB")
    rotorAssembly = RotorAssembly(rotors, reflector)
    rotorAssembly.setRotorPosition("AAZ")
    actual = rotorAssembly.crypt("A")

    assert "U" == actual