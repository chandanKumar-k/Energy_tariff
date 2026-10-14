# Static Code Analysis

## 1. Pylint Findings

Original Pylint score: 6.14/10

| Issue | Location | Description | Fix |
|---|---|---|---|
| Missing docstrings | Multiple lines | Module/functions lack documentation | Add docstrings |
| Mutable default argument | Line 12 | Default list may be shared across calls | Use None and initialise inside |
| Unnecessary elif | Line 19 | elif follows return | Replace with if |
| Global statements | Lines 27, 40 | Functions modify global variables | Refactor where practical |
| Bare exception | Line 44 | Exception handling is too broad | Catch specific exceptions |
| File handling | Lines 42, 48 | Encoding/context managers not specified | Use with open and encoding |
| Unnecessary f-strings | Lines 59, 60, 66 | Formatting is unnecessary | Use regular strings |
| Unsafe eval | Line 63 | Evaluates input as Python code | Use safe parsing |
| Unused import | Line 2 | sys is not used | Remove import |

## 2. Bandit Findings

| Issue | Severity | Location | Fix |
|---|---|---|---|
| B307: eval usage | Medium | Line 63 | Replace with safe parsing and validation |

## 3. Flake8 Findings

| Issue | Location | Description |
|---|---|---|
| F401 | Line 2 | Unused sys import |
| E302 | Lines 12, 17, 26, 32, 39, 47, 52 | Blank-line formatting |
| E501 | Lines 24, 62 | Lines exceed 79 characters |
| E722 | Line 44 | Bare except |
| E305 | Line 68 | Missing blank lines after definition |

## 4. Verification

The original reports were generated before making any changes.

After fixing the issues, all three tools will be run again
to verify the results.
