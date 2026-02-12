---
title: "Resources"
---

A curated collection of articles, videos, and tools
for advanced tmux + Claude Code integration.

## Official Documentation & Team Insights

**Claude Code Best Practices -- Anthropic**
<br/>
https://www.anthropic.com/engineering/claude-code-best-practices
<br/>
The official best practices document covers tmux
integration for managing multiple Claude Code sessions,
including workflow patterns for composing Claude Code
into broader workflows with tmux.

**Latent Space Podcast -- Claude Code Team Interview**
<br/>
https://www.latent.space/p/claude-code
<br/>
Direct insights from Boris Cherny and Cat Wu (Claude
Code creators) discussing how "a lot of people use Code
with tmux to manage a bunch of windows and sessions
happening in parallel."

## Advanced Technical Tutorials

**"Vibe Coding Anytime, Anywhere with tmux, Tailscale,
and Claude Code"** -- Nuttakit Kundum (July 2025)
<br/>
https://nuttakitkundum.medium.com/vibe-coding-anytime-anywhere-with-tmux-tailscale-and-claude-code-fda01f3c5cd2
<br/>
Sophisticated session persistence workflows: maintain
Claude Code sessions across devices using tmux. Covers
mobile development, SSH workflows, and tmux pane
management for remote coding.

**"LLM Codegen go Brrr -- Parallelization with Git
Worktrees and Tmux"** -- DEV Community
<br/>
https://dev.to/skeptrune/llm-codegen-go-brrr-parallelization-with-git-worktrees-and-tmux-2gop
<br/>
Comprehensive guide on advanced parallelization using
Git worktrees and tmux to manage multiple Claude Code
instances simultaneously.

**"How to automate development journaling with Claude
Code"** -- Takuya/Devas (June 2025)
<br/>
https://www.devas.life/how-to-automate-development-journaling-with-claude-code/
<br/>
In-depth integration guide combining Claude Code with
tmux and neovim, including MCP integration and automated
workflows.

## Japanese Developer Resources (Zenn)

**"Claude Codeを並列組織化してClaude Code 'Company'にする
tmuxコマンド集"** -- Kazuph
<br/>
https://zenn.dev/kazuph/articles/beb87d102bd4f5
<br/>
Advanced tmux command collection for organizing multiple
Claude Code instances into a "company" structure with
boss-worker relationships using tmux panes.

**"Claude Code Maxで実現する完全自動並列開発システム"**
-- Studio Prairie
<br/>
https://zenn.dev/studio_prairie/articles/90f5fc48a6dea7
<br/>
Fully automated parallel development system using Claude
Code Max with tmux orchestration.

## Video Resources

**"Claude Code / OpenCode + T-Mux + Worktrees: This
SELF-SPAWNING AI Coder TEAM is INSANITY!"**
<br/>
https://www.youtube.com/watch?v=bWKHPelgNgs
<br/>
11-minute demonstration combining Claude Code with tmux
and Git Worktrees to create a self-spawning AI coder
team, covering task claiming systems and agent-spawn
workflow automation.

**"【AI組織実現!! Claude Code Organization】現役エンジニア
が「5人のAIが勝手に開発する会社」の作り方を解説！"**
<br/>
https://www.youtube.com/watch?v=Qxus36eijkM
<br/>
Japanese tutorial demonstrating advanced AI organization
with hierarchical agent structures (President -> Manager
-> Worker) using tmux session management.

## Production-Ready Tools

### Claude Squad

https://github.com/smtg-ai/claude-squad
<br/>
The most mature solution for managing multiple Claude
Code agents. Uses tmux for isolated terminal sessions
with git worktrees for separate codebases. Features a
TUI interface, auto-accept mode, and support for
multiple AI agents (Claude Code, Aider, Codex).

### tmux-mcp

https://github.com/nickgnd/tmux-mcp
<br/>
Model Context Protocol server that enables Claude
Desktop to interact programmatically with tmux sessions.
Features include listing/searching sessions, viewing
and navigating windows/panes, executing commands, and
creating new sessions.

### Task Master Agent Spawner

https://gist.github.com/worksfornow/df0cb6c4f6fd4966cd17133bc711fd20
<br/>
Sophisticated Claude Code slash command for parallel
task delegation. Creates multiple worktrees and launches
Claude agents in tmux sessions with automated status
tracking and branch management.

## Key Integration Patterns

- **Multi-Agent Parallelization** -- Use git worktrees +
  tmux sessions for parallel agent execution. Each agent
  gets an isolated directory and tmux session.
- **Terminal Orchestration** -- Pair a Claude Code pane
  with a separate pane for Git commands and other shell
  work, using a big scrollback buffer.
- **Session Persistence** -- Implement persistent tmux
  sessions for Claude Code context preservation across
  disconnections.
- **MCP Integration** -- Use Model Context Protocol
  servers for programmatic tmux control, allowing AI
  assistants to observe and interact with terminal
  sessions.
