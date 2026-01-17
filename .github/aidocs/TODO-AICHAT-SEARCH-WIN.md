# TODO: Make `aichat search` work on Windows (termios import crash)

## Problem

On Windows, `aichat search` (interactive mode) fails before it can launch the UI due to:

`ModuleNotFoundError: No module named 'termios'`

This is because `termios` is a POSIX-only stdlib module and is imported at module import time in several files.

### Repro (Windows)

- `python -c "import claude_code_tools.session_menu_cli"`
- `aichat search` (without `--json`)

Example traceback seen in this repo on Windows:

- `claude_code_tools/session_menu_cli.py` imports `extract_first_user_message` from `claude_code_tools/find_session.py`
- `claude_code_tools/find_session.py` imports `termios` at top-level → crash

## Why it breaks `aichat search`

`aichat search` has two modes:

- JSON mode: runs the Rust binary and exits early (`aichat.py` around the `if json_output:` block)
- Interactive mode: imports the Node UI and action execution glue, including:
  - `from claude_code_tools.session_menu_cli import execute_action` (`claude_code_tools/aichat.py:2099`)

`session_menu_cli.py` imports functions from:

- `claude_code_tools/find_session.py` (imports `termios`, `tty` at module scope)
- `claude_code_tools/find_claude_session.py` (also imports `termios`, `tty` at module scope)

Those modules only need `termios/tty` to implement “read a single keypress” for `prompt_post_action()`.
That keypress helper is not required just to *import* the modules and use shared helpers like
`extract_first_user_message()` or `get_session_start_timestamp()`.

## Goal

Make the Python import chain for interactive `aichat search` Windows-safe by removing the unconditional
`termios` dependency at import time, while retaining macOS/Linux behavior.

Non-goals for this TODO:

- Broader Windows compatibility audit for the rest of the repo (do later)
- Rust `aichat-search` Windows packaging (separate TODO if needed)

## Proposed approach (recommended)

Use `click.getchar()` for single-key reads. `click` is already a dependency and provides a
cross-platform implementation (Windows + POSIX), so we can remove all direct `termios`/`tty`
usage from this repo.

Key details:

- Replace the local `_read_key()` helpers to call `click.getchar()`
- Normalize Windows Enter (`"\r"`) to `"\n"` so existing Esc/Enter checks keep working
- Remove `import termios` / `import tty` entirely (not just “move off module scope”)

## Implementation checklist

- Replace `_read_key()` to use `click.getchar()` in:
  - `claude_code_tools/find_session.py`
  - `claude_code_tools/find_claude_session.py`
  - `claude_code_tools/find_codex_session.py`
- Remove all `termios` and `tty` imports from the codebase.
- Ensure `prompt_post_action()` still supports:
  - Esc → `"back"`
  - Enter → `"exit"`
- Verify import chain on Windows:
  - `python -c "import claude_code_tools.session_menu_cli"` succeeds
  - `python -c "from claude_code_tools.aichat import main"` succeeds
- Manual smoke test (Windows):
  - Run `aichat search` and confirm it reaches the UI (or at least errors on missing `aichat-search`
    binary rather than crashing on `termios`).

## Test plan (automatable)

Add a unit test that ensures no Python modules in `claude_code_tools/` import `termios` or `tty`
(AST-based check). This runs on any platform and prevents regressions.

## Notes / pitfalls

- `msvcrt.getwch()` returns `"\r"` for Enter; normalize to `"\n"` so existing comparisons keep working.
- Windows special keys may return a prefix (`"\x00"`/`"\xe0"`) followed by a second code; for this use
  case it’s fine to ignore those and continue reading until a non-prefix char is received.
- Avoid importing `termios`/`tty` directly in this repo; rely on `click.getchar()` instead.

## Status

Implemented in this repo:

- Removed all `termios`/`tty` imports and replaced keypress reads with `click.getchar()`.
- Added `tests/test_no_termios_imports.py` to prevent reintroducing POSIX-only imports.
