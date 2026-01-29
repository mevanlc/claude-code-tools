# Changelog

## [1.9.2] - 2026-01-29

### Added
- **UserPromptSubmit hook**: Injects voice summary instructions at the start of
  each turn, reminding Claude to add a `📢` spoken summary marker
- **PostToolUse hook**: Short reminder after each tool call to keep voice
  instructions fresh during long tool chains
- **voice_common.py**: Shared module for DRY code (config reading, reminder
  building, constants)
- **Silent hook injection**: Uses `additionalContext` instead of `systemMessage`
  to avoid noisy terminal output
- **MAX_SPOKEN_WORDS constant**: Configurable word limit (default 25) in
  `voice_common.py`
- **TTS benchmark script**: `scripts/benchmark_tts.py` for comparing KittenTTS
  vs pocket-tts performance

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
- **Flexible word limits**: Explicit summaries (📢 marker or headless Claude)
  use 1.5× the word limit, giving Claude flexibility while preventing runaway
  verbosity. Strict limit only applies to last-resort truncation.

### Improved
- **Tone matching**: Instructions now tell Claude to match user's tone and
  style (including colorful language)
- **Custom prompt support**: User's custom voice prompt (from config) is
  included and noted to override default instructions if conflicting

## [1.8.4] - 2026-01-26

### Initial release
- Stop hook with headless Claude summarization
- pocket-tts integration for voice synthesis
- Configurable voice selection
- Custom prompt support via `~/.claude/voice.local.md`
