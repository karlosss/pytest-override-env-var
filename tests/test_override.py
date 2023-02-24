import os

import pytest


def test_default():
    assert os.environ["TEST_VAR"] == "default"
    assert os.environ["TEST_VAR_2"] == "default2"


@pytest.mark.env(TEST_VAR="overriden")
def test_override():
    assert os.environ["TEST_VAR"] == "overriden"
    assert os.environ["TEST_VAR_2"] == "default2"


def test_restore_default():
    assert os.environ["TEST_VAR"] == "default"
    assert os.environ["TEST_VAR_2"] == "default2"
