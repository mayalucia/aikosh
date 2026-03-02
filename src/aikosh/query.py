# query.py — retrieval surface
#
# Find entries across collections by attributes (region, altitude,
# landscape type, genus, ...) without loading entire collections.
# Token cost matters — an agent should get the entries it needs
# and nothing more.
#
# Pipeline position:
#   source → validate → distill plugins → schema-check → index → [query]
