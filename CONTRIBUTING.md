Branch protection & CI requirements
=================================

Recommended branch protection rules (apply in GitHub repository Settings → Branches):

- Protect the default branch (e.g. `ci/pin-httpx-email-validator`).
- Require status checks to pass before merging. Add the following checks:
  - `test (ubuntu-latest, python 3.11)` (job `test` for Python 3.11)
  - `test (ubuntu-latest, python 3.10)` (job `test` for Python 3.10)
- Require pull request reviews before merging (1 or 2 approvers).
- Optionally require signed commits and linear history.

Apply rules via GitHub UI or `gh` CLI:

```bash
# protect branch via gh (requires repo admin)
gh api -X PUT \
  -H "Accept: application/vnd.github+json" \
  /repos/:owner/:repo/branches/:branch/protection \
  -f required_status_checks.contexts='["test (ubuntu-latest, python 3.11)", "test (ubuntu-latest, python 3.10)"]' \
  -f required_pull_request_reviews.dismiss_stale_reviews=false \
  -f enforce_admins=true
```

Note: replace `:owner`, `:repo`, and `:branch` with your repository owner, name, and target branch. Running the above requires an admin token.
