import pytest
from plugboard import Plugboard
from alphabet import Alphabet

def test_nothingMapped():
    plugboard = Plugboard()
    for element in Alphabet.set:
        assert plugboard[element] == element

ab_testdata = [("A","B"), ("B", "A"),("C","C")]
@pytest.mark.parametrize("given, expected", ab_testdata)
def test_a_mapped_to_b(given, expected):
    plugboard = Plugboard()
    plugboard["A"] = "B"

