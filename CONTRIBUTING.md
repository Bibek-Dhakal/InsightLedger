# Contributing Guidelines

We welcome contributions to the InsightLedger project. Please follow these guidelines to ensure a smooth collaboration
process.

## Commit Standards (Conventional Commits)

This repository strictly enforces **Conventional Commits**. All commit messages must follow this structure:

```
<type>(<optional scope>): <description>
```

Your commit messages dictate how `release-please` manages semantic versioning and updates the `CHANGELOG.md`.

### Allowed Types:

- **`feat:`** A new feature (triggers a MINOR version bump).
- **`fix:`** A bug fix (triggers a PATCH version bump).
- **`feat!:`** or **`fix!:`** (with a `!` or `BREAKING CHANGE:` in the footer) indicates a breaking change (triggers a
  MAJOR version bump).
- **`docs:`** Documentation only changes.
- **`chore:`** Maintenance tasks, dependency updates, etc.
- **`test:`** Adding or fixing tests.
- **`refactor:`** Code changes that neither fix a bug nor add a feature.

### Example:

```
feat(analytics): add statistical power calculation to A/B test
```

## Pull Request Process

1. Fork the repository and create your branch from `main`.
2. Ensure you have installed the local pre-commit hooks (`pre-commit install`).
3. Make your changes and ensure tests pass.
4. Create a PR targeting the `main` branch.
5. Wait for CI checks to complete and secure a review.

## Code Quality

We use `ruff` for Python linting and formatting. Ensure your code passes all pre-commit checks before pushing.
