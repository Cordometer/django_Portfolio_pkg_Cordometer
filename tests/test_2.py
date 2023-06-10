import pytest

@pytest.fixture
def fixture_1():
    print('run-ficture-1')
    return 1

def test_example1(fixture_1):
    num = fixture_1
    assert num == 1

@pytest.fixture(scope="session")
def fixture_2():
    print('run-ficture-1')
    return 1

def test_example2(fixture_2):
    print('run-example-2')
    num = fixture_2
    assert num == 1

#Type pytest -rP to use the example below correctly
@pytest.fixture
def yield_fixture():
    print ('Start Test Phase')
    yield 6
    print('End Test Phase')

def test_example(yield_fixture):
    print('ru-example-1')
    assert yield_fixture == 6