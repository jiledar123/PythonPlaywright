from ftplib import print_line

import pytest


@pytest.fixture(scope='function')
def function_ficture():
    print_line('\nFunction fixture called ')

@pytest.fixture(scope='module')
def module_fixture():
     print_line('\nModule fixture called ')

def test_first(function_ficture,module_fixture):
    assert True


def test_second(function_ficture,module_fixture):
    assert True
