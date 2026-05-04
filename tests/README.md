# Run unit tests with **pyTest**/pyUnit(**unittest**)

## To run all tests in the tests/ directory with **pyTest**

```bash
python -m pytest tests/teste_pt*.py -v
```

***NOTE***: Ensure that **pyTest** is installed in your Python environment. You can install it using pip if you haven't already<br>
Use full file name pattern to avoid running tests from other files that may not be intended for pyTest.

```bash
pip install pytest
```

Test installation with:

```bash
pytest --version
```

## To run all tests in the tests/ directory with **unittest**

```bash
python -m unittest discover -s tests -p "teste_pu_*.py" -v  
```

***NOTE***: **unittest** is part of Python's standard library, so you don't need to install anything extra to use it.

## differences between **pyTest** and **unittest**

- **pyTest** is more flexible and has a simpler syntax compared to **unittest**, which is part of the standard library and follows a more traditional approach to testing.
- **pyTest** supports fixtures, parameterized testing, and has a rich ecosystem of plugins, while **unittest** is more basic and may require more  code for similar functionality.
- **pyTest** is generally considered more user-friendly and is widely adopted in the Python community, while **unittest** is often used for simpler testing needs or when sticking to the standard library is preferred.
- **pyTest** can run **unittest** tests, but **unittest** cannot run **pyTest** tests without modification.
- **pyTest** provides better test discovery and reporting features compared to **unittest**, making it easier to identify and fix issues in your code.
- **pyTest** is more standard, so it compares better with other testing frameworks in different languages, while unittest is specific to Python and may not be as familiar to developers coming from other languages.<br><br>
In simple terms, **pyTest** is often preferred for its ease of use and powerful features, while **unittest** is a solid choice for those who want to stick to the standard library or have simpler testing needs.
