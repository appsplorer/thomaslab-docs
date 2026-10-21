# Bleeding phenotypes and high-bleeding-risk research

This layer standardizes **research classification** after the underlying clinical facts have been extracted and reviewed.

## GUSTO

`classify_gusto_bleeding()` uses standardized indicators for bleeding, intracerebral hemorrhage, treated hemodynamic compromise, and transfusion. Severe/life-threatening takes precedence over moderate and mild.

## BARC

`classify_barc_bleeding()` implements hierarchical type 0, 1, 2, 3a, 3b, 3c, 4 and 5 research labels from standardized evidence. CABG-related type 4 is accepted as a pre-adjudicated flag because the complete type-4 definition contains procedure-specific requirements.

## ARC-HBR

`calculate_arc_hbr()` intentionally **does not derive** individual criteria from raw EHR data. The study must first construct reviewed boolean criterion columns using appropriate baseline windows. The function then applies the consensus aggregation rule: at least one major criterion or at least two minor criteria.

## Adjudication

`create_bleeding_adjudication_queue()` identifies candidate events missing fields needed for classification. This is designed to support chart review rather than silently filling missing clinical facts.

## Sources used by the bundled research-reference YAMLs

- Urban P, et al. *European Heart Journal*. 2019. DOI: `10.1093/eurheartj/ehz372`.
- Mehran R, et al. *Circulation*. 2011. DOI: `10.1161/CIRCULATIONAHA.110.009449`.

Review the primary publication and the study protocol before using these classifications in a manuscript.
