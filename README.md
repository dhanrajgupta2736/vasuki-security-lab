# VASUKI Security Lab

An intentionally vulnerable Flask codebase for demonstrating an autonomous
security patch pipeline. **Use as a local test fixture only.**

The baseline contains three real flaws:
- CWE-89: SQL injection in login.
- CWE-22: directory traversal in document reads.
- CWE-639: missing authorization in user profile access.

Eleven automated tests cover normal logins, authorized profile and document
access, and five exploit checks. The vulnerable baseline is expected to have
6 passing tests and 5 failing security tests. A correct patch produces 11 passes
without deleting or modifying tests.

```sh
python -m pip install -r requirements.txt
python -m pytest -q
```

Submit this repository's URL to VASUKI, leave the branch and project directory
blank, and enable draft PR publication. The pipeline clones the actual default
branch, records baseline tests, patches source, repeats source checks, executes
the unchanged suite in Docker, and publishes only after all gates pass.

The vulnerabilities are deliberately present on `main` for repeated demos.
Inspect the generated draft pull requests for fixes and executed evidence.
