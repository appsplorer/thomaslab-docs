# Multi-treatment comparative effectiveness and individualized-strategy research

Version 0.26 extends the causal stack from binary treatment comparisons to three or more mutually exclusive treatment strategies.

The layer is designed for comparative-effectiveness research. It does not output a clinically endorsed "best treatment for this patient."

## Multi-arm identification problem

For treatment (Ain{a_1,ldots,a_K}), the average target quantities are the potential-outcome means

[
mu_a=E[Y(a)].
]

Pairwise average effects are

[
mu_a-mu_b.
]

For heterogeneous effects relative to a prespecified reference arm (r),

[
	au_{a:r}(x)=E[Y(a)-Y(r)mid X=x].
]

Causal interpretation requires the same core conditions as binary-treatment causal inference, generalized to all treatment arms:

- consistency;
- treatment exchangeability conditional on baseline covariates;
- positivity for every treatment strategy in the relevant covariate region;
- correct temporal ordering;
- comparable outcome definitions; and
- adequate nuisance/effect-model estimation.

## Input validation

validate_multi_treatment_inputs() requires:

- at least three observed treatment arms;
- at least two observations in every arm;
- one analysis row per unit;
- an explicit outcome type; and
- explicitly declared pre-treatment covariates.

Treatment and outcome columns cannot be included among the covariates.

## Multinomial treatment propensity

The v0.26 nuisance layer fits a multinomial logistic treatment model inside each cross-fitting training fold.

For held-out row (i), it estimates

[
hat e_a(X_i)=P(A_i=amid X_i)
]

for every treatment arm.

Raw probabilities are retained. A small lower bound can be applied for numerical stability in inverse-probability terms, after which the vector is renormalized to sum to one.

This numerical operation does not repair structural treatment-support failure.

## Arm-specific outcome regressions

For each treatment arm, v0.26 fits

[
hat m_a(X)=E[Ymid A=a,X].
]

Binary outcomes use logistic regression or random forests; continuous outcomes use linear regression or random forests.

Each held-out observation receives an outcome prediction under every treatment arm.

## Generalized overlap diagnostics

generalized_overlap_diagnostics() reports:

- propensity minimum and quantiles for every arm;
- fraction below an explicit support threshold;
- pairwise joint-support fractions;
- observed-arm generalized overlap weights;
- arm-specific effective sample size; and
- whether any row has a low probability for at least one treatment arm.

For (K) arms, the generalized overlap tilting function is

[
h(X)=left{sum_{a=1}^{K}rac{1}{e_a(X)}ight}^{-1},
]

and an observed subject assigned arm (a) receives the overlap weight

[
w_a(X)=rac{h(X)}{e_a(X)}.
]

The diagnostic is intended to expose poor common support rather than hide it.

## Cross-fitted multi-arm AIPW

estimate_multiarm_aipw() calculates a doubly robust pseudo-outcome for each arm:

[
phi_a =
hat m_a(X)
+
rac{I(A=a)}{hat e_a(X)}
{Y-hat m_a(X)}.
]

The arm-specific estimate is

[
hatmu_a=rac{1}{n}sum_i phi_{ia}.
]

Every unordered pair of treatment arms is then contrasted using paired influence contributions.

The output includes:

- one estimated potential-outcome mean for each arm;
- all pairwise effect differences;
- an explicit indication of which contrasts involve the prespecified reference arm;
- risk differences and risk ratios for binary outcomes when defined; and
- generalized overlap diagnostics.

The function does not rank treatment arms.

## Nested cross-fitted multi-arm DR learner

fit_multiarm_dr_learner() estimates heterogeneous effects relative to a prespecified reference arm.

Inside each outer training fold:

1. all multi-arm propensity and outcome nuisance models are cross-fitted again;
2. an arm-specific doubly robust pseudo-outcome is calculated;
3. the pseudo-contrast (phi_a-phi_r) is formed for every non-reference arm;
4. a second-stage effect model learns the conditional pseudo-contrast;
5. the second-stage model predicts the outer held-out rows.

The result is a set of out-of-fold reference-arm CATE predictions.

This nested architecture avoids fitting the second-stage effect model directly to pseudo-outcomes created by nuisance models that trained on the same row.

## Research-policy scores

For the held-out rows, the reference-arm outcome regression provides a baseline score.

For non-reference arm (a), v0.26 forms the research score

[
hat m_r(X)+hat	au_{a:r}(X).
]

These scores are useful for methodological policy evaluation. They can fall outside the natural outcome range in finite samples, especially for binary outcomes, because the DR effect learner is not constrained to a probability model.

They therefore must not be described as calibrated patient-level event probabilities unless separately validated.

## New-population prediction

predict_multiarm_effects() applies the fitted multi-arm DR learner to new baseline covariates.

It returns:

- the reference-arm CATE for every treatment arm; and
- the corresponding model research-policy score.

The reference arm always has CATE zero by definition.

## Pairwise and reference-arm CATEs

pairwise_cate_predictions() derives every unordered pairwise CATE from the common reference-arm representation.

If all treatment effects use the same reference arm r, then

[
	au_{a:b}(x)=	au_{a:r}(x)-	au_{b:r}(x).
]

The function returns all pairwise comparisons for every row and does not choose a preferred arm.

summarize_reference_cate() separately compares the mean predicted reference-arm CATE with the mean held-out DR pseudo-contrast for each non-reference arm.

It also reports uncertainty for the average DR pseudo-contrast.

These are model-based diagnostics. They are not evidence that individual CATE estimates are observed truths.

## Exploratory multi-arm research policies

derive_multiarm_research_policy() identifies the arm with the most favorable model research score after the analyst explicitly states whether higher or lower outcomes are desirable.

An optional minimum model-utility margin can force abstention when the two leading modeled strategies are too close.

The output calls the selected value:

research_policy_arm

rather than "recommended treatment."

If a row abstains, policy-value estimation fails closed until the analyst explicitly resolves that row.

## Doubly robust multi-arm policy value

evaluate_multiarm_research_policy() uses held-out nuisance estimates to evaluate a complete multi-arm research rule.

For selected arm (d(X)), the score is

[
hat m_{d(X)}(X)
+
rac{I{A=d(X)}}
{hat e_{d(X)}(X)}
{Y-hat m_{d(X)}(X)}.
]

The function also reports treat-all-arm comparators and the assignment distribution.

When the policy itself was not generated honestly or out of fold, the result is explicitly labeled as potentially optimistically biased.

Even with honest prediction, the output remains an observational causal research estimate rather than a clinical decision rule.

## Bootstrap model-order uncertainty

bootstrap_multiarm_model_order_uncertainty() repeatedly resamples the training cohort, refits the multi-arm DR learner, and predicts a target covariate table.

For every target row it reports:

- how often each arm receives the most favorable modeled score;
- bootstrap mean modeled score for each arm;
- bootstrap SD for each arm; and
- entropy of the model-selected-arm distribution.

These frequencies quantify model-order instability.

They must not be described as the probability that a treatment is clinically optimal for that patient.

## Site-specific comparative effects

site_multiarm_effects() reruns multi-arm AIPW separately by site.

Sites without all treatment arms or with insufficient treatment support are retained with an explicit failure status.

The output intentionally does not rank sites.

## Transporting comparative-effect distributions

transport_multiarm_effect_distribution() integrates v0.26 with the v0.24 source-to-target sampling model.

For each treatment arm, it compares:

- unweighted source mean research-policy score;
- sampling-weighted source mean research-policy score;
- target mean research-policy score;
- unweighted source mean CATE versus reference;
- sampling-weighted source mean CATE versus reference; and
- target mean CATE versus reference.

The external target requires baseline covariates only.

This is a transport diagnostic for a fitted comparative-effect model. It is not external validation of patient-level treatment effects when target outcomes are unavailable.

## Recommended workflow

A publication-quality multi-treatment study should:

1. define mutually exclusive treatment strategies and time zero before modeling;
2. freeze baseline covariates and exclude post-treatment features;
3. inspect arm counts and treatment availability across sites;
4. fit multinomial propensities and generalized-overlap diagnostics;
5. run multi-arm AIPW for average comparative effects;
6. inspect all pairwise effects without selecting only favorable comparisons;
7. prespecify a reference arm for heterogeneous-effect analysis;
8. fit the nested multi-arm DR learner;
9. inspect mean reference-arm CATE and DR pseudo-contrast agreement;
10. inspect model-order uncertainty rather than a single deterministic arm label;
11. evaluate exploratory policies honestly/out of fold;
12. rerun comparative effects by site;
13. transport effect distributions only when cross-population assumptions are scientifically justified;
14. preserve estimator disagreement and support failures in the final report.

The result is comparative-effectiveness research, not autonomous treatment selection.
