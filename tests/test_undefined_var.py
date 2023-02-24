import os

import pytest


def test_default():
    assert os.environ["TEST_VAR"] == "default"
    assert os.environ["TEST_VAR_2"] == "default2"
    assert "UNDEFINED" not in os.environ


@pytest.mark.env(UNDEFINED="undefined")
def test_override():
    assert os.environ["TEST_VAR"] == "default"
    assert os.environ["TEST_VAR_2"] == "default2"
    assert os.environ["UNDEFINED"] == "undefined"


def test_restore_default():
    assert os.environ["TEST_VAR"] == "default"
    assert os.environ["TEST_VAR_2"] == "default2"
    assert "UNDEFINED" not in os.environ
