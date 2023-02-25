# pytest-override-env-var
Pytest mark to override a value of an environment variable.

![Lint](https://github.com/karlosss/pytest-override-env-var/actions/workflows/lint.yml/badge.svg)
![Tests](https://github.com/karlosss/pytest-override-env-var/actions/workflows/test.yml/badge.svg)

## The problem

Suppose we have the following function:

```python
import os

def get_homedir() -> str:
    return os.environ["HOME"]
```

Now, we need to test it:

```python
def test_get_homedir():
    assert get_homedir() == "/home/my_user"
```

This test will, though, succeed only if the username of the user is `my_user`.
To make it succeed on all machines, we will need to patch the value of `HOME`
environment variable:

```python
import pytest

@pytest.mark.env(HOME="/home/test_user")
def test_get_homedir():
    assert get_homedir() == "/home/test_user"
```

Now, the test will pass, regardless of the username.

## Installation

```bash
pip install pytest-override-env-var
```
After that, `@pytest.mark.env(...)` will "just work".

Supports Python 3.7+ and pytest 7+.

## Examples

[pytest-override-env-var](https://github.com/karlosss/pytest-override-env-var) resets
the value of the variable after the test has finished:

```python
def test_before():
    assert os.environ["HOME"] == "/home/my_user"

@pytest.mark.env(HOME="/home/test_user")
def test():
    assert os.environ["HOME"] == "/home/test_user"

def test_after():
    assert os.environ["HOME"] == "/home/my_user"
```

Multiple variables in one mark are supported:
```python
@pytest.mark.env(A=1, B=2)
def test():
    assert os.environ["A"] == 1
    assert os.environ["B"] == 2
```

The `env` marks stack:
```python
@pytest.mark.env(A=1)
@pytest.mark.env(B=2)
def test():
    assert os.environ["A"] == 1
    assert os.environ["B"] == 2
```

Upon redefinition, the innermost value is used:
```python
@pytest.mark.env(A=1)
@pytest.mark.env(A=2)
def test():
    assert os.environ["A"] == 2
```

This can be useful in combination with classes:
```python
@pytest.mark.env(A=1)
class TestSuite:
    def test_1(self):
        assert os.environ["A"] == 1
        
    @pytest.mark.env(A=2)
    def test_2(self):
        assert os.environ["A"] == 2

    def test_3(self):
        assert os.environ["A"] == 1

def test_outside():
    ...
    # A has the original value here
```

If the environment variable that is being patched is undefined, 
[pytest-override-env-var](https://github.com/karlosss/pytest-override-env-var)
will define it just for the test, and then delete it from the env again.
