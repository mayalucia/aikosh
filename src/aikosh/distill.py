# distill.py — plugin registry for knowledge extraction
#
# A validated source can yield multiple kinds of knowledge. Each distill
# plugin knows how to extract entries for a specific collection from a
# source. The same source might yield spirit entries AND tourist site
# entries through different plugins.
#
# Plugins are the adapter pattern: they bridge a source format to a
# collection schema. The aikosh-guardian builds the framework; the
# epistem-guardian writes plugins for specific collections.
#
# Pipeline position:
#   source → validate → [distill plugins] → schema-check → index → query
#                         ├─ plugin₁ → spirits[]
#                         ├─ plugin₂ → sites[]
#                         └─ plugin₃ → ...
