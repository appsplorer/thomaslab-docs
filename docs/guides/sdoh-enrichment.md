# Governed SDOH enrichment

`thomaslab.sdoh` links already-authorized patient geography to reviewed ZIP→ZCTA crosswalks and area-level context tables.

The package intentionally does **not** geocode addresses or call external APIs. Geography mappings and index tables must be supplied by the study team so source/version/governance can be documented.

## Workflow

1. normalize the approved ZIP field;
2. map ZIP to ZCTA using an explicit crosswalk;
3. resolve one-to-many ZIP mappings only using a supplied weight or strict-unmapped behavior;
4. attach reviewed SDI/ADI/SVI or other area-level tables with provenance prefixes;
5. audit mapping completeness overall and by site;
6. optionally remove direct geography fields from the derived research table.

Dropping ZIP columns is not a de-identification guarantee. Institutional privacy and governance rules still apply.
