import pytest

from src import main


@pytest.mark.only
def test_add():
    assert main.add(1, 2) == 3


@pytest.mark.skip(reason="Not implemented yet")
def test_subtract():
    assert main.add(1, -2) == -1
