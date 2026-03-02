# Aikosh — Claude Code Instructions

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
  CLAUDE.md                          # this file
  .gitignore
  src/aikosh/
    __init__.py                      # public API
    schema.py                        # entry validation (genus/species/instance)
    query.py                         # find entries by region, altitude, landscape
    validate.py                      # consistency checks (back-references, vocabulary)
  tests/
```

## Core Concepts

- **Schema validation**: entries follow a genus → species → instance hierarchy.
  Each level has required and optional fields. The schema is per-collection.
- **Query**: agents need to find entries by attributes (region, altitude,
  landscape type) without loading entire collections. Token cost matters.
- **Consistency checks**: back-references between entries must resolve.
  Controlled vocabulary terms must come from the declared vocabulary.

## Python Environment

- Python 3.11+
- Use `uv` for virtual environments and package management
- Run tests with: `uv run pytest`

## The Human (mu2tau)

PhD-level theoretical statistical physicist. Works from Emacs with org-babel.
Do not over-explain. Push back on flawed reasoning.

## Git

- Do not commit unless asked
- Do not push unless asked

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
