import pytest


@pytest.fixture(scope='session')
def session_fixture():
    print('session fixture called.')