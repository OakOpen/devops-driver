![status sheild](https://img.shields.io/static/v1?label=status&message=starting...&color=inactive&style=plastic)
[![status sheild](https://img.shields.io/static/v1?label=released&message=v0.1.34&color=active&style=plastic)](https://pypi.org/project/devopsdriver/0.1.34/)
[![GitHub](https://img.shields.io/github/license/marcpage/devops-driver?style=plastic)](https://github.com/marcpage/devops-driver?tab=Unlicense-1-ov-file#readme)
[![commit sheild](https://img.shields.io/github/last-commit/marcpage/devops-driver?style=plastic)](https://github.com/marcpage/devops-driver/commits)
[![activity sheild](https://img.shields.io/github/commit-activity/m/marcpage/devops-driver?style=plastic)](https://github.com/marcpage/devops-driver/commits)
[![GitHub top language](https://img.shields.io/github/languages/top/marcpage/devops-driver?style=plastic)](https://github.com/marcpage/devops-driver)
[![size sheild](https://img.shields.io/github/languages/code-size/marcpage/devops-driver?style=plastic)](https://github.com/marcpage/devops-driver)

[![example workflow](https://github.com/marcpage/devops-driver/actions/workflows/pr.yml/badge.svg)](https://github.com/marcpage/devops-driver/actions/workflows/pr.yml)
[![status sheild](https://img.shields.io/static/v1?label=test+coverage&message=99%&color=active&style=plastic)](https://github.com/marcpage/devops-driver/blob/main/Makefile#L4)
[![issues sheild](https://img.shields.io/github/issues-raw/marcpage/devops-driver?style=plastic)](https://github.com/marcpage/devops-driver/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/marcpage/devops-driver?style=flat)](https://github.com/marcpage/devops-driver/pulls)
[![GitHub contributors](https://img.shields.io/github/contributors/marcpage/devops-driver?style=flat)](https://github.com/marcpage/devops-driver/graphs/contributors)
[![PR's Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com)

[![follow sheild](https://img.shields.io/github/followers/marcpage?label=Follow&style=social)](https://github.com/marcpage?tab=followers)
[![watch sheild](https://img.shields.io/github/watchers/marcpage/devops-driver?label=Watch&style=social)](https://github.com/marcpage/devops-driver/watchers)

# devops-driver

Devops-driver is a set of tools to help streamline developer's experience. It is a collection of tools to help gain insights into various processes.

## How to deploy

### System setup for deploying

```bash
$ make venv
$ source .venv/bin/activate
$ python -m devopsdriver.setings --set_secrets
pypi_test.password (pypi_test/token): *********
pypi_prod.password (pypi/token): *********
$ 
```

### Deploy

1. Make sure `__version__` is updated to a version that does not exist on the test or productin PyPI server
2. Update the versions in `README.md` (twice in `status sheild`)
3. Execute `make deploy`
4. Create a PR with your changes after a successful deployment
5. After the PR merges, create a new release in GitHub
