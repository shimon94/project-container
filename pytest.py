import pytest


@pytest.mark.parametrize('URL, is_ok', [('yad.com', True)])
def TestValidateEmail(URL, is_ok):
    assert URL(URL) == is_ok