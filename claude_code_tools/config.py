"""
Centralized configuration for claude-code-tools.

Defaults are defined here. Users can override by creating ~/.cctools/config.json
"""

import json
from pathlib import Path
from typing import Any, Optional

# Default configuration values
DEFAULTS = {
    # Model for Claude sub-agents during context rollover
    "claude_subagent_model": "haiku",
    # Model for Codex context rollover (analysis step - cheaper/faster)
    "codex_rollover_model": "gpt-5.1-codex-mini",
    # Model for Codex interactive session after rollover (full capability)
    # Empty string means use codex's default model
    "codex_default_model": "",
    # Command to launch Claude (binary name or path)
    "claude_command": "claude",
    # Command to launch Codex (binary name or path)
    "codex_command": "codex",
    # Extra arguments to pass when resuming a Claude session (before the session ID)
    "claude_resume_extra_args": [],
    # Extra arguments to pass when resuming a Codex session (before the session ID)
    "codex_resume_extra_args": [],
}

_config_cache: Optional[dict[str, Any]] = None


def _load_user_config() -> dict[str, Any]:
    """Load user config from ~/.cctools/config.json if it exists."""
    config_path = Path.home() / ".cctools" / "config.json"
    if config_path.exists():
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}
    return {}


def get_config() -> dict[str, Any]:
    """
    Get merged configuration (defaults + user overrides).

    Returns:
        Dict with all config values
    """
    global _config_cache
    if _config_cache is None:
        _config_cache = {**DEFAULTS, **_load_user_config()}
    return _config_cache


def get(key: str, default: Any = None) -> Any:
    """
    Get a specific config value.

    Args:
        key: Config key name
        default: Default if key not found (falls back to DEFAULTS first)

    Returns:
        Config value
    """
    config = get_config()
    return config.get(key, default)


def reload_config() -> dict[str, Any]:
    """
    Reload configuration from disk (clears cache).

    Returns:
        Fresh merged config
    """
    global _config_cache
    _config_cache = None
    return get_config()


# Convenience accessors for common settings
def claude_subagent_model() -> str:
    """Get model name for Claude sub-agents during context rollover."""
    return get("claude_subagent_model", DEFAULTS["claude_subagent_model"])


def codex_rollover_model() -> str:
    """Get model name for Codex context rollover (analysis step)."""
    return get("codex_rollover_model", DEFAULTS["codex_rollover_model"])


def codex_default_model() -> str:
    """Get model name for Codex interactive session after rollover.

    Returns empty string to use codex's default model.
    """
    return get("codex_default_model", DEFAULTS["codex_default_model"])


def claude_command() -> str:
    """Get the command/binary name used to launch Claude."""
    return get("claude_command", DEFAULTS["claude_command"])


def codex_command() -> str:
    """Get the command/binary name used to launch Codex."""
    return get("codex_command", DEFAULTS["codex_command"])


def claude_resume_extra_args() -> list[str]:
    """Get extra arguments passed when resuming a Claude session."""
    val = get("claude_resume_extra_args", DEFAULTS["claude_resume_extra_args"])
    return list(val) if val else []


def codex_resume_extra_args() -> list[str]:
    """Get extra arguments passed when resuming a Codex session."""
    val = get("codex_resume_extra_args", DEFAULTS["codex_resume_extra_args"])
    return list(val) if val else []


def claude_resume_cmd(session_id: str) -> tuple[str, list[str]]:
    """Build the full command to resume a Claude session.

    Returns (binary, [binary, ...args, -r, session_id]).
    """
    cmd = claude_command()
    args = [cmd] + claude_resume_extra_args() + ["-r", session_id]
    return cmd, args


def codex_resume_cmd(session_id: str) -> tuple[str, list[str]]:
    """Build the full command to resume a Codex session.

    Returns (binary, [binary, ...args, resume, session_id]).
    """
    cmd = codex_command()
    args = [cmd] + codex_resume_extra_args() + ["resume", session_id]
    return cmd, args
