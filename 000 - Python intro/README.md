# Python introduction

## Python version
Check python version in shell.
```shell
python --version  # most often links to deprecated python2 or doesn't exist
python3 --version
python3 -V
```

### Currently used python versions ([source](https://www.python.org/downloads/))
<table>
    <tr>
        <th>Python version</th>
        <th>Maintenance status</th>
        <th>First released</th>
        <th>End of support</th>
        <th>Release schedule</th>
    </tr>
    <tr>
        <td>3.10</td>
        <td>bugfix</td>
        <td>2020-10-05</td>
        <td>2025-10</td>
        <td><a href="https://www.python.org/dev/peps/pep-0619">PEP 619</a></td>
    </tr>
    <tr>
        <td>3.9</td>
        <td>bugfix</td>
        <td>2020-10-05</td>
        <td>2025-10</td>
        <td><a href="https://www.python.org/dev/peps/pep-0596">PEP 596</a></td>
    </tr>
    <tr>
        <td>3.8</td>
        <td>security</td>
        <td>2019-10-14</td>
        <td>2024-10</td>
        <td><a href="https://www.python.org/dev/peps/pep-0569">PEP 569</a></td>
    </tr>
    <tr>
        <td>3.7</td>
        <td>security</td>
        <td>2018-06-27</td>
        <td>2023-06-27</td>
        <td><a href="https://www.python.org/dev/peps/pep-0537">PEP 537</a></td>
    </tr>
    <tr>
        <td>2.7</td>
        <td>end-of-life</td>
        <td>2010-07-03</td>
        <td>2020-01-01</td>
        <td><a href="https://www.python.org/dev/peps/pep-0373">PEP 373</a></td>
    </tr>
</table>

## Python vs ...
* [php vs Python][]
* [Ruby vs Python][]

Let's look at the code.
```shell
$ ls -1 ./python_vs
$ php ./python_vs/example.php  # try some PHP
> ...
$ ruby ./python_vs/example.php  # try some Ruby
> ...
$ python3 ./python_vs/example.py  # finally try some Python
> ...
```

## Run python code
### Interactive interpreter
Run interpreter in terminal by typing `python3`

1. Define two variables `x = 42` and `y = 2`
1. Print `x` and `y`
1. Print `x` `y` times in a loop.

### File
Open file [`base.py`](base.py)
1. Reproduce all steps from previous assignment

#### Run in terminal
Run in terminal:
```shell
python3 ./base.py
```
Now run files: [`import_datetime.py`](import_datetime.py) and [`import_faker.py`](import_faker.py).

### External dependencies
Let's use 3rd party [Faker][].
```shell
# Create new python environment in '~/.envs/test'
python3 -m venv ~/.envs/training_env
# Activate environment
source ~/.envs/training_env/bin/activate
# Now we can use 'python' instead of 'python3'
which python

# install dependencies
pip install faker
# check what's installed
pip freeze
# And run code containing 3rd party libraries
python ./import_faker.py
```

But, what's [PIP][]?
> The Python Package Index (PyPI) is a repository of software for the Python programming language.

Kind of like [composer][] (PHP) or [RubyGems][] (Ruby)?

More info about [Virtual Environments and Packages][]

And great podcast about [Tools for Setting Up Python on a New Machine][]

### Run in pyCharm
[Create and edit run/debug configurations][]

`Right Click on <file name>` &rarr; `Run <file name>`

To set custom environment used by pyCharm go to:
```
File | Settings | Project: python_course | Python Interpreter
```
`Right Click on gear` &rarr; `Add...` &rarr; `Existing environment` &rarr; `Path to python executable`

<!--- Links -->
[php vs Python]: https://kinsta.com/blog/php-vs-python/
[Ruby vs Python]: https://www.upguard.com/blog/python-vs-ruby
[Faker]: https://github.com/joke2k/faker
[PIP]: https://pypi.org/
[RubyGems]: https://rubygems.org/
[composer]: https://getcomposer.org/
[Virtual Environments and Packages]: https://docs.python.org/3/tutorial/venv.html
[Tools for Setting Up Python on a New Machine]: https://realpython.com/podcasts/rpp/101/
[Create and edit run/debug configurations]: https://www.jetbrains.com/help/pycharm/creating-and-editing-run-debug-configurations.html
