
check-cloudformation
=========

A tool (and pre-commit hook) to automatically parse cloudformation scripts.

## Installation

`pip install check-cloudformation`


## As a pre-commit hook

See [pre-commit](https://github.com/pre-commit/pre-commit) for instructions

Sample `.pre-commit-config.yaml`:

```yaml
-   repo: https://github.com/danschaffer/check-cloudformation
    sha: v0.0.1
    hooks:
    -   id: check-cloudformation
```

