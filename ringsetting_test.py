import ringsetting

def test_mapIn_wrap():
    ring = ringsetting.Ringsetting("B")
    given = "A"
    expected = "Z"
    actual = ring.mapCharacterIn(given)
    assert actual == expected

def test_mapIn():
    ring = ringsetting.Ringsetting("B")
    given = "B"
    expected = "A"
    actual = ring.mapCharacterIn(given)
    assert actual == expected

def test_mapOut_wrap():
    ring = ringsetting.Ringsetting("B")
    given = "Z"
    expected = "A"
    actual = ring.mapCharacterOut(given)
    assert actual == expected

def test_mapOut():
    ring = ringsetting.Ringsetting("B")
    given = "B"
    expected = "C"
    actual = ring.mapCharacterOut(given)
    assert actual == expected
