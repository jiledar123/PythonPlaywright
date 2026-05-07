import pytest


@pytest.fixture(scope='module')
def pre_setup():
    print('pre_setup called')
    return 'Pass'


@pytest.fixture(scope='function')
def post_setup():
    print('post_setup called')
    yield
    print('tear down call finished')


def test_validate(pre_setup,post_setup):
    print('test_validate called')
    assert pre_setup == 'Pass'
