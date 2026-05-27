# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

A single-page mind mapping app — one `index.html` file with embedded CSS and JS. Uses [Mind Elixir](https://mind-elixir.com/) v5.11.2 (loaded from CDN) for the mind map rendering and interaction. All data is persisted in `localStorage` (no backend/server). No build tools, no package manager — just open `index.html` in a browser.

## Running/viewing

```bash
open index.html
```

Or use a local static server if CORS issues arise with CDN resources:

```bash
python3 -m http.server 8080
# then open http://localhost:8080
```

There are no tests, no linter, and no build step.

## Architecture

**Single-file IIFE module pattern.** The entire application lives in `index.html`. The `App` object (line 457) is an IIFE that returns the public API. All state is held in a single `state` object (`{ maps, currentMapId, theme }`) and persisted to `localStorage` under key `mindmap_app`.

**Data format.** Mind map data is stored as `{ nodeData: { topic, id, expanded, children: [...], direction? } }`. This matches Mind Elixir's `MindElixir.new()` output format. Import handles multiple source formats (wrapped, bare tree, array) and normalizes them via `normalizeNode()`.

**Storage keys:**
- `mindmap_app` — app state (map list, current map ID, theme)
- `mindmap_data_<id>` — per-map node data

**Auto-save** is debounced at 500ms on every Mind Elixir `operation` event. Manual save (`Ctrl+S`) skips the debounce.

**Key dependencies on globals:**
- `MindElixir` — the constructor, loaded via IIFE script tag; accessed via `MindElixir.default` fallback (line 506) for IIFE/ESM compatibility
- `MindElixir.SIDE`, `MindElixir.THEME`, `MindElixir.DARK_THEME` — constants for direction and theming

**Import normalisation** (`normalizeNode`, line 686) converts arbitrary JSON node trees into Mind Elixir format by mapping `topic/name/title/text` → `topic` and recursing into `children` arrays.

## Example data

`Simcenter_Amesim_ready.json` is a pre-built mind map for a "Simcenter Amesim simulation learning plan" (Chinese). It follows the `{ nodeData: {...} }` format and can be imported directly.

## CLI script

Running `./mindmap <file.json>` starts a local server and opens the browser with the mind map auto-loaded. The HTML fetches `auto-load.json` on startup via the `autoImport()` function.

When the user asks to "make a mind map" or "visualize as a mind map" about a topic:
1. Generate a JSON file with mind map structure (any supported format works: bare node tree with `name`/`topic` + `children`, `nodeData` wrapper, `nodes` array, etc.)
2. Save it as `<topic>.json` in the project directory
3. Run `./mindmap <topic>.json` to open it in the browser
