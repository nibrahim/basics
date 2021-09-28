import example

def test_single():
    assert example.capital("Noufal") == 1


def test_none():
    assert example.capital("noufal") == 0

def test_multiple():
    assert example.capital("Noufal Ibrahim") == 2


def test_transform_upper():
    assert example.transform("noufal", "upper") == "NOUFAL"

def test_transform_lower():
    assert example.transform("NOUFAL", "lower") == "noufal"

def test_prime():
    for i in [2,3,5,7,11,13]:
        assert example.isprime(i)
    for i in [4,6,8,12,14,16]:
        assert not example.isprime(i)

