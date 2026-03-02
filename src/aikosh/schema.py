# schema.py — entry-level gate
#
# Validates that a distilled YAML entry conforms to its collection's schema.
# Each collection defines its own schema (required fields per level,
# controlled vocabulary, back-reference constraints). The genus → species →
# instance hierarchy means each level inherits and extends the parent's
# required fields.
#
# Schema definitions live alongside the collections they govern
# (e.g. domains/epistem/collections/himalayan-spirits/schema.yaml).
# This module loads and enforces them.
#
# Pipeline position:
#   source → validate → distill plugins → [schema-check] → index → query
