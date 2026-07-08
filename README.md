# sample-lambda

A minimal AWS Lambda repo used to mimic a real work project structure, for
testing GitHub Actions / Dependabot behavior in isolation.

## Structure

```
.
├── .github/
│   ├── dependabot.yml        # Dependabot config (pip + github-actions ecosystems)
│   └── workflows/
│       └── ci.yml            # Lint/test workflow, also runs on Dependabot PRs
├── src/
│   └── lambda_function.py    # Lambda handler
├── tests/
│   └── test_lambda_function.py
├── fass-lambda.yml           # SAM-style deployment template
├── requirements.txt          # Runtime deps (pinned, so Dependabot has something to bump)
├── pyproject.toml            # Project metadata + dev tooling config
└── README.md
```

## Local dev

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e ".[dev]"
pytest
```

## Deploy (SAM)

```bash
sam build --template-file fass-lambda.yml
sam deploy --guided
```

## Testing Dependabot

This repo pins intentionally old versions in `requirements.txt` and uses an
old action version in `.github/workflows/ci.yml`, so once pushed to GitHub,
Dependabot should open PRs bumping both on its configured schedule (see
`.github/dependabot.yml`). You can also trigger a check manually from the
repo's **Insights → Dependency graph → Dependabot** tab, or via
**Settings → Code security → Dependabot** → "Check for updates".
