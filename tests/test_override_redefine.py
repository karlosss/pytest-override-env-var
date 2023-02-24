import os

import pytest


def test_default():
    assert os.environ["TEST_VAR"] == "default"
    assert os.environ["TEST_VAR_2"] == "default2"


@pytest.mark.env(TEST_VAR="overriden_outer")
@pytest.mark.env(TEST_VAR="overriden_inner")
def test_override_redefine():
    assert os.environ["TEST_VAR"] == "overriden_inner"


def test_restore_default():
    assert os.environ["TEST_VAR"] == "default"
    assert os.environ["TEST_VAR_2"] == "default2"
