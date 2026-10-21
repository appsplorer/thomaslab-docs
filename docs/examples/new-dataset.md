# Example: unfamiliar dataset onboarding

~~~python
import pandas as pd

from thomaslab.onboard import generate_adapter_bundle, inspect_source

data = pd.DataFrame(
    {
        "PATIENT": ["P001", "P002", "P003"],
        "EVENT_DATE": ["2026-01-10", "2026-01-11", "2026-01-12"],
        "AGE": [64, 71, 58],
    }
)

inspection = inspect_source(data)
print(inspection["profile"])

bundle = generate_adapter_bundle(
    data,
    "work/adapters/example_site_v1",
    dataset_name="example_site_v1",
    required_columns=["PATIENT", "EVENT_DATE"],
)

print(bundle)
~~~

## Review before analysis

The generated adapter is a review artifact. Confirm identifier meaning, dates, units, vocabularies, missingness, and source provenance before freezing a canonical mapping.
