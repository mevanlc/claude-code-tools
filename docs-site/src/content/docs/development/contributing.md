---
title: "Contributing"
description: >
  How to contribute to claude-code-tools.
---

## Contributing

Contributions are welcome! Follow the standard
fork-and-PR workflow below.

1. **Fork** the repository on GitHub

2. **Create a feature branch:**

   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **Make your changes** -- see the
   [Development overview](../) for architecture and
   setup instructions

4. **Test thoroughly** -- see
   [Testing](../testing/) for how to verify changes
   across the Python, Rust, and Node.js layers

5. **Commit your changes** with a clear, descriptive
   message

6. **Push** to your fork:

   ```bash
   git push origin feature/amazing-feature
   ```

7. **Open a Pull Request** against the `main` branch

:::tip
Run the full test suite before opening a PR.
See [Testing](../testing/) for details on each
layer.
:::

## Code Style

- **Python** -- follows PEP 8 (88-char line limit),
  Google-style docstrings, fully type-annotated,
  files under 1000 lines
- **Rust** -- standard `cargo fmt` / `cargo clippy`
- **Node.js** -- standard formatting

## Questions?

Open an issue on GitHub if you have questions about
the codebase or want to discuss a feature before
starting work.
