# Aikosh — Spirit Instructions

## What This Is

Aikosh is the computational engine for structured knowledge collections. It
provides tools for building, validating, and querying the YAML collections
that live in `domains/epistem`. Aikosh is the instrument; epistem is the
territory.

The name comes from the idea of a storehouse of knowledge — a kosh (कोश) of
insights gathered through systematic inquiry.

Part of the [MāyāLucIA](https://github.com/mayalucia) organisation.

## Directory Structure

```
modules/aikosh/
  system.md                          # this file (backend-neutral)
  CLAUDE.md                         # Claude Code adapter
  .gitignore
  src/aikosh/
    __init__.py                      # pipeline overview
    validate.py                      # source-level gate
    distill.py                       # plugin registry (source → entries[])
    schema.py                        # entry-level gate (per-collection schemas)
    query.py                         # retrieval surface (find entries by attributes)
  tests/
```

## Pipeline

```
source → validate → distill plugins → schema-check → index → query
                     ├─ plugin₁ → spirits[]
                     ├─ plugin₂ → sites[]
                     └─ plugin₃ → ...
```

- **Validate** (`validate.py`): source-level gate. Can aikosh work with this
  source? Any source that can be indexed passes. Knows nothing about schemas.
- **Distill** (`distill.py`): plugin registry. Each plugin extracts entries for
  a specific collection from a validated source. Same source, multiple plugins,
  different kinds of knowledge. The adapter pattern.
- **Schema** (`schema.py`): entry-level gate. Does a distilled YAML entry conform
  to its collection's schema? Genus → species → instance hierarchy with
  per-level required fields, controlled vocabulary, back-references.
- **Query** (`query.py`): retrieval surface. Find entries by attributes without
  loading entire collections. Token cost matters.

## Python Environment

- Python 3.11+
- Use `uv` for virtual environments and package management
- Run tests with: `uv run pytest`

## The Human (mu2tau)

PhD-level theoretical statistical physicist. Works from Emacs with org-babel.
Do not over-explain. Push back on flawed reasoning.

## Organisational Context

This module belongs to the **epistem** guild (structured knowledge for agents)
within the MāyāLucIA organisation. Its guardian spirit is `aikosh-guardian`
(see `aburaya/spirits/aikosh-guardian/` in the parent repo).

The collections this module validates and serves live in `domains/epistem/collections/`.

**Sūtra relay**: The organisational relay is `github.com/mayalucia/sutra`.
Clone locally to `.sutra/` (gitignored) if absent. Use the relay-read
skill to fetch and filter messages. The local HEAD in `.sutra/` is your
read cursor.

**The relay is heard.** If you have organisational needs — wishes about
how things should work, dependencies on other modules, questions for
other projects — write them into the sūtra with appropriate tags.
Messages go to the universe, not to a recipient. The organisation listens.
