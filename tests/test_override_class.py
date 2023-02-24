import os

import pytest


def test_default():
    assert os.environ["TEST_VAR"] == "default"
    assert os.environ["TEST_VAR_2"] == "default2"


@pytest.mark.env(TEST_VAR="overriden")
class TestOverride:
    def test_no_change_1(self):
        assert os.environ["TEST_VAR"] == "overriden"
        assert os.environ["TEST_VAR_2"] == "default2"

    def test_no_change_2(self):
        assert os.environ["TEST_VAR"] == "overriden"
        assert os.environ["TEST_VAR_2"] == "default2"


def test_restore_default():
    assert os.environ["TEST_VAR"] == "default"
    assert os.environ["TEST_VAR_2"] == "default2"
