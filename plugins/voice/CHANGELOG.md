# Changelog

## [1.9.2] - 2026-01-28

### Added
- **UserPromptSubmit hook**: Injects voice summary instructions at the start of
  each turn, reminding Claude to add a `📢` spoken summary marker
- **PostToolUse hook**: Short reminder after each tool call to keep voice
  instructions fresh during long tool chains
- **voice_common.py**: Shared module for DRY code (config reading, reminder
  building)
- **Silent hook injection**: Uses `additionalContext` instead of `systemMessage`
  to avoid noisy terminal output

### Changed
- **Smarter summary extraction**: Extracts inline `📢` markers for instant
  summaries (no API call needed)
- **Word-based length detection**: Uses word count (≤25 words) instead of
  fragile sentence counting
- **Fallback only when needed**: Headless Claude summarization only triggers
  for responses >25 words without a marker
- **Text block joining**: Fixed joining with newlines (not spaces) so `📢`
  markers at start of text blocks are properly detected
- **Quiet Stop hook**: Only shows output when headless Claude generates a new
  summary; otherwise runs silently

### Improved
- **Tone matching**: Instructions now tell Claude to match user's tone and
  style (including colorful language)
- **Custom prompt support**: User's custom voice prompt (from config) is
  included and noted to override default instructions if conflicting
- **25-word limit**: All summaries enforced to max 25 words for concise voice
  output

## [1.8.4] - 2026-01-26

### Initial release
- Stop hook with headless Claude summarization
- pocket-tts integration for voice synthesis
- Configurable voice selection
- Custom prompt support via `~/.claude/voice.local.md`
