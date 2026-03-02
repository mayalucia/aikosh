# validate.py — source-level gate
#
# The single entry point: can aikosh work with this source?
# A source is any raw material (org survey, web page, field note, PDF).
# Validation answers: does it have enough structure, citation, and signal
# to be worth distilling? This is source-level, not entry-level — it
# knows nothing about collection schemas.
#
# Pipeline position:
#   source → [validate] → distill plugins → schema-check → index → query
