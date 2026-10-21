# FHIR research interoperability

`thomaslab.interop` provides lightweight research extraction for FHIR Bundles.

## Validate Bundle structure

```python
from thomaslab.interop import validate_fhir_bundle

report = validate_fhir_bundle(bundle)
```

This checks the minimum structure needed to iterate Bundle entries safely. It is **not** a replacement for an official FHIR validator or implementation-guide/profile conformance test.

## Flatten resources

```python
from thomaslab.interop import flatten_fhir_bundle

resources = flatten_fhir_bundle(bundle, ["Observation", "MedicationRequest"])
```

Each row preserves the raw resource dictionary so no clinically relevant nested content is discarded by the convenience layer.

## Common research tables

```python
from thomaslab.interop import extract_fhir_observations, extract_fhir_medication_requests

observations = extract_fhir_observations(bundle)
medications = extract_fhir_medication_requests(bundle)
```

The helpers extract common identifiers, coding system/code/display, patient/encounter references, timestamps, values/units, and dosage text. They intentionally do not claim full semantic normalization; terminology mapping should be performed against validated vocabularies.
