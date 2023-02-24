import os

import pytest


def pytest_configure(config: pytest.Config) -> None:
    config.addinivalue_line(
        "markers",
        "env(VARIABLE_NAME='new_value'): overrides the value of "
        "environment variable VARIABLE_NAME with new_value",
    )


def pytest_runtest_setup(item: pytest.Item) -> None:
    # GitHub pipeline for some reason runs the setup twice, therefore we want to do nothing on consecutive runs
    if "debounce" in item.stash:
        return
    item.stash["debounce"] = True

    old_values = {}
    for mark in reversed(list(item.iter_markers(name="env"))):
        for var_name, new_value in mark.kwargs.items():
            if var_name not in old_values:
                old_values[var_name] = os.environ.get(var_name)
            os.environ[var_name] = new_value
    item.stash["old_env"] = old_values


def pytest_runtest_teardown(item: pytest.Item) -> None:
    for var_name, old_value in item.stash["old_env"].items():
        # again, due to multiple runs of teardown, we need to not try to delete twice
        if var_name not in os.environ:
            continue

        if old_value is None:
            del os.environ[var_name]
        else:
            os.environ[var_name] = old_value
