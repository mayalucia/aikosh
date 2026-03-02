# aikosh — structured knowledge for agents
#
# Pipeline: source → validate → distill → schema-check → index → query
#
# validate.py  — source-level gate (is this indexable?)
# distill.py   — plugin registry (source → entries[], one plugin per collection)
# schema.py    — entry-level gate (does this entry conform to its collection?)
# query.py     — retrieval surface (find entries by attributes, token-aware)
