# Run BDD tests with **Behave**

## What is Behave and Gherkin?

**Behave** is a Behaviour-Driven Development (BDD) framework for Python. It allows you to write tests in a natural language style that can be understood by non-technical stakeholders, bridging the gap between business requirements and automated tests.

**Gherkin** is the language used to write BDD scenarios. It structures test cases as human-readable narratives using keywords like `Feature`, `Scenario`, `Given`, `When`, and `Then`, stored in `.feature` files. These files describe the expected behaviour of the system from the user's perspective.

Together, Behave and Gherkin enable teams to define acceptance criteria as executable specifications, ensuring that the software behaves as intended from the user's point of view.

---

## Installation

Install **Behave** using pip:

```bash
pip install behave
```
If pip is not in your path, use Python command to install behave:
```
python -m pip install behave
```
Test installation with:

```bash
behave --version
```

---

## To run all BDD tests in the bdd/ directory

```bash
behave bdd/
```
You might need to use ```python -m``` prefix...

***NOTE***: Run the command from the project root directory.

## To run a specific feature file

```bash
behave bdd/req_001_lista_titulos.feature
```

## To run tests with a specific tag

```bash
behave bdd/ --tags=REQ-001
```

## To run with verbose output

```bash
behave bdd/ --no-capture -v
```
