import ringsetting
import wiring

def test_mapIn_wrap():
    noop = wiring.WiringFactory.Wiring("NoOp")
    ring = ringsetting.Ringsetting(noop, "B")
    given = "A"
    expected = "Z"
    actual = ring.mapIn(given)
    assert actual == expected

def test_mapIn():
    noop = wiring.WiringFactory.Wiring("NoOp")
    ring = ringsetting.Ringsetting(noop, "B")
    given = "B"
    expected = "A"
    actual = ring.mapIn(given)
    assert actual == expected

def test_mapOut_wrap():
    noop = wiring.WiringFactory.Wiring("NoOp")
    ring = ringsetting.Ringsetting(noop, "B")
    given = "Z"
    expected = "A"
    actual = ring.mapOut(given)
    assert actual == expected

def test_mapOut():
    noop = wiring.WiringFactory.Wiring("NoOp")
    ring = ringsetting.Ringsetting(noop, "B")
    given = "B"
    expected = "C"
    actual = ring.mapOut(given)
    assert actual == expected


