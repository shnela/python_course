# Testing

## [xUnit] approach

## [unittest — Unit testing framework]

### Basic example

```python
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
```

### [Test cases]

```python
def setUp(self):
    ...

@classmethod
def setUpClass(cls):
    ...
```

### [Command-Line Interface]

```shell
python -m unittest
```

## [pytest: helps you write better programs]

```shell
pip install pytest
pytest
```

### [Creating JUnitXML format files]

```shell
pytest --junitxml=path
```

### pytest vs unittest
[test_decoder_exercise.py](./test_decoder_exercise.py)
[test_decoder_exercise_pytest.py](./test_decoder_exercise_pytest.py)

## Features
* [yield fixtures]
* [How to parametrize fixtures and test functions] - look at `test_changing_channels` and `test_setting_negative_channel`

[xUnit]: https://en.wikipedia.org/wiki/XUnit
[unittest — Unit testing framework]: https://docs.python.org/3/library/unittest.html
[Test cases]: https://docs.python.org/3/library/unittest.html#test-cases
[Command-Line Interface]: https://docs.python.org/3/library/unittest.html#command-line-interface
[pytest: helps you write better programs]: https://docs.pytest.org/
[Creating JUnitXML format files]: https://docs.pytest.org/en/7.1.x/how-to/output.html#creating-junitxml-format-files
[yield fixtures]: https://docs.pytest.org/en/7.1.x/how-to/fixtures.html#yield-fixtures-recommended
[How to parametrize fixtures and test functions]: https://docs.pytest.org/en/7.1.x/how-to/parametrize.html#parametrize