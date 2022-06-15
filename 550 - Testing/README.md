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

[xUnit]: https://en.wikipedia.org/wiki/XUnit
[unittest — Unit testing framework]: https://docs.python.org/3/library/unittest.html
[Test cases]: https://docs.python.org/3/library/unittest.html#test-cases
[Command-Line Interface]: https://docs.python.org/3/library/unittest.html#command-line-interface
[pytest: helps you write better programs]: https://docs.pytest.org/
[Creating JUnitXML format files]: https://docs.pytest.org/en/7.1.x/how-to/output.html#creating-junitxml-format-files
