# Python starter

Credit to https://github.com/pamelafox/python-project-template

This is a template repository for any Python project that comes with the following dev tools:

ruff: identifies many errors and style issues (flake8, isort, pyupgrade)
black: auto-formats code
Those checks are run as pre-commit hooks using the pre-commit library.

It includes pytest for testing plus the pytest-cov plugin to measure coverage.

The checks and tests are all run using Github actions on every pull request and merge to main.

## Development instructions

```
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements-dev.txt
pre-commit install # to setup git hook scripts
python3 -m pytest
```

## starter

- Run program
  ```console
  python src/main.py -h

  ```


## Test
```console
python -m pytest     # regular run
python -m pytest -v  # run verbose
python -m pytest --cov-src tests # run tests with coverage report

```


### Filters

- **Skip** a particular test by decorating the test with `@pytest.mark.skip(reason="...")` and then run `python -m pytest [-v]`
  ```python
  # mytest.py

  @pytest.mark.skip(reason="Not implemented yet")
  def test_booboo:
    assert True
  ```

  ```console
  $ pytest -m pytest [-v]

  ```


- **Only** Run one test by decorating the test with `@pytest.mark.only` and then run `python -m pytest -[v]k only`
  ```python
  @pytest.mark.only
  def test_booboo:
    assert True
  ```

  ```console
  $ pytest -m pytest -k only
  ```
