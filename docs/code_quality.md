# Code Quality

Automated quality checks are enforced via `pre-commit` hooks. These checks run automatically when you run `git commit`.

## Environment Setup

Run the following to set up hooks locally:

```bash
pip install pre-commit
pre-commit install
```

## Manual Execution Commands

To run checks on all files (useful before opening a PR):

```bash
pre-commit run --all-files
```

To run checks only on staged files:

```bash
pre-commit run
```

## Bypassing

If a hotfix requires an emergency bypass, use the `--no-verify` flag. **Use this sparingly.**

```bash
git commit -m "fix: emergency hotfix" --no-verify
```
