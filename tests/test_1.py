import pytest

def test_example():
    print("test1")
    assert 1 == 1

# Type pytest -m "slow" to only test this example below
@pytest.mark.slow
def test_example1():
    assert 1 == 1

@pytest.mark.skip
def test_example2():
    assert 3 == 3

@pytest.mark.xfail
def test_example3():
    assert 4 == 3