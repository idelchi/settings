# go

![gopher](misc/gopher.png)

## Introduction

**Pipelines** consist of various toy commandline tools, in order to play around and get more familiar with:

- Go
- Task
- Azure DevOps Pipelines
- GitLab CI/CD Pipelines
- GitHub Actions
- Linters, Formatters, automated tooling

## Setup

This section is intended to help developers and contributors get a working copy of
_pipelines_ on their end

Clone the repository

    git clone https://github.com/idelchi/go.git

Install (preferably latest) [Go 1.19](https://go.dev/dl/)

See [Installing dependencies](#installing-dependencies) for a full list of dependencies.

### Installing dependencies

For a local development setup, the following tools are recommended:

- [taskfile](https://taskfile.dev/#/installation) for convenient build management
- [golangci-lint](https://golangci-lint.run/usage/install/) for code linting
- [godoc](https://pkg.go.dev/golang.org/x/tools/cmd/godoc) for viewing documentation

### Running the code

A [Taskfile][taskfile-file] is used to summarize and manage the different build system commands.

[taskfile-file]: ./Taskfile.yaml

To display available commands along with their descriptions, run

    task --list

To display a list of required tools to make full usage of the tasks available in the taskfiles, run

    task tools

### Contributing

- Go through [Tips](#tips)
- All checks from section [Tools](#tools) must pass.
- Coverage should not decrease.

Run

    task

periodically to format and lint all relevant sources.

### Tools

- Go
  - [gofmt](https://pkg.go.dev/cmd/gofmt)
  - [vet](https://pkg.go.dev/cmd/vet)
  - [golangci-lint](https://github.com/golangci/golangci-lint)
- Groovy
  - [npm-groovy-lint](https://github.com/nvuillam/npm-groovy-lint)
  - [jflint](https://github.com/miyajan/jflint)
- JSON/YAML
  - [prettier](https://github.com/prettier/prettier)
  - [jsonlint](https://github.com/zaach/jsonlint)
  - [yamllint](https://github.com/adrienverge/yamllint)
- shell/bash
  - [shfmt](https://github.com/mvdan/sh)
  - [shellcheck](https://github.com/koalaman/shellcheck)
- Dockerfile
  - [hadolint](https://github.com/hadolint/hadolint)
  - [dockerfilelint](https://github.com/replicatedhq/dockerfilelint)
- Markdown
  - [prettier](https://github.com/prettier/prettier)
  - [markdownlint](https://github.com/DavidAnson/markdownlint)
- Spelling
  - [misspell](https://github.com/client9/misspell)
  - [cspell](https://github.com/streetsidesoftware/cspell)
  - [codespell](https://github.com/codespell-project/codespell)
- Copy-Paste
  - [jscpd](https://github.com/kucherenko/jscpd)

### Using Docker

The accompanying docker image may be used to run native runs with full support of all commands listed in the _taskfile_.

To launch the container and mount the workspace, run

    docker compose run go

### Tips

Read

- [Effective Go](https://go.dev/doc/effective_go)
- [Go Code Review Comments](https://github.com/golang/go/wiki/CodeReviewComments)
- [Go Test Comments](https://github.com/golang/go/wiki/TestComments)
- [Go Style Guide](https://github.com/bahlo/go-styleguide)
- [Go Proverbs](https://go-proverbs.github.io/)
- [Uber Go Style Guide](https://github.com/uber-go/guide/blob/master/style.md)

Hints

- Generics should be used to _solve a problem_, and not as a general approach to every problem. These typically include, reducing boiler-plate, type-casts, reflection, and dynamic typing. See [Using Generics in Go](https://www.youtube.com/watch?v=nr8EpUO9jhw)
- [Accept interfaces, return structs](https://github.com/golang/go/wiki/CodeReviewComments#interfaces)
