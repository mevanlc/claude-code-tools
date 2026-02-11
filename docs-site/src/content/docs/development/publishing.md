---
title: "Publishing"
description: >
  How to publish Python packages to PyPI and Rust
  binaries to crates.io.
---

## Python Package (PyPI)

Use the `all-*` Make commands to prepare a release,
then publish:

```bash
make all-patch   # or all-minor, all-major
uv publish
```

### What the Commands Do

Each `all-*` command automatically:

1. Runs `make prep-node` to ensure
   `node_ui/node_modules/` is up-to-date
2. Bumps the version (patch, minor, or major)
3. Pushes to GitHub and pushes tags
4. Creates a GitHub release
5. Cleans old builds and builds the package

The built package includes `node_modules/` so end
users do **not** need `npm install` -- they only
need Node.js 16+ installed.

After the build completes, run `uv publish` to
upload to PyPI.

## Rust Binaries (crates.io)

### aichat-search

```bash
make aichat-search-publish
```

This command:

1. Bumps the version (default: patch; override with
   `BUMP=minor` or `BUMP=major`)
2. Creates a `rust-v*` git tag
3. Pushes to GitHub (triggers CI for binary releases)
4. Publishes to crates.io

After publishing, users can install with:

```bash
cargo install aichat-search
```

Or via Homebrew:

```bash
brew install pchalasani/tap/aichat-search
```

### lmsh

```bash
make lmsh-publish
```

This command:

1. Bumps the patch version
2. Publishes to crates.io

After publishing, users can install with:

```bash
cargo install lmsh
```

## See Also

- [Make Commands](../make-commands/) -- full list of
  all available Make targets
- [Testing](../testing/) -- verify changes before
  publishing
