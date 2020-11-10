import pytest


@pytest.mark.parametrize('URL, is_ok', [('yad.com', True)])
def TestValidateEmail(URL, is_ok):
    assert validateUrl(URL) == is_ok