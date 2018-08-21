import pytest
from app.utilities import Constants

def test_constants():
    assert Constants.ADD == "+"
    assert Constants.SUBTRACT == "-"
    assert Constants.DIVIDE == "/"
    assert Constants.MULTIPLY == "*"
