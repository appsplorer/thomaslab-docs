# Example: prediction metrics and validation

~~~python
import numpy as np

from thomaslab.eval import calculate_clinical_metrics

y_true = np.array([0, 1, 0, 1, 1, 0])
y_probability = np.array([0.10, 0.82, 0.25, 0.74, 0.67, 0.31])

metrics = calculate_clinical_metrics(
    y_true,
    y_probability,
    threshold=0.5,
)

print(metrics)
~~~

## Validation boundary

A metric computed on one dataset is not evidence of transportability. Preserve patient/site/time separation, avoid target/proxy leakage, assess calibration and uncertainty, evaluate relevant subgroups, and label genuinely independent external validation explicitly.
