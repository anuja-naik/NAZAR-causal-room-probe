# Causal RF detector — proposed method and reference boundary

**Purpose:** distinguish a stimulus-linked response from a flow that merely looks busy or unusual.  
**Status:** the concept proposes this detector. The included Python code is a small synthetic reference, not a production detector and not a result from a physical camera.

## Signals

For flow `f` and regular bin index `t`:

- `s(t)`: measured light level from the phone’s ambient-light sensor (or a separately defined measured manual-light stimulus).
- `|Δs(t)|`: magnitude of the change in measured light.
- `x_f(t)`: traffic volume for flow `f` in the corresponding bin; the concept suggests approximately 100 ms bins.

The detector should use measured light, not simply the requested torch/display command. A camera may respond after sensor exposure, frame production, encoding, packetization, and transmission, so zero-lag correlation is not a sufficient assumption.

## Proposed response model

The supplied concept describes a model of the form:

```text
x_f(t) = β₁ (|Δs| * h)(t) + β₂ (s * h)(t) + drift(t) + ε(t)
```

Here `h` is a response kernel over approximately 0–3 seconds. The transition term represents scene-change effects; the level term can represent brightness-dependent behavior such as auto-exposure or IR-cut changes. A ridge-regression fit is proposed so a distributed delay can be estimated rather than requiring an exact lag.

The reference script implements a deliberately transparent approximation: it forms lagged transition and level predictors at the supplied bin resolution, includes an intercept and linear drift baseline, fits ridge regression, and scores improvement over the baseline using in-sample partial R². It does not implement a calibrated count likelihood, online streaming, time synchronization, or final detector decision policy. A physical study may justify a different traffic model.

## Surrogate-code comparison

A response score alone can be high by chance because of periodic traffic, bursts, encoder behavior, or a poor stimulus/traffic alignment. The proposed check compares the actual challenge’s score with scores from surrogate codes that were not presented to the camera.

For `m` supplied surrogate codes, the reference utility reports a one-sided empirical value:

```text
p = (1 + number of surrogate scores >= observed score) / (m + 1)
```

The concept proposes roughly 200 surrogate codes. With 200 surrogates, the smallest attainable empirical p-value is `1/201`; this is a resolution limit, not a guarantee of validity. The surrogate-generation procedure must be chosen before inspecting outcomes and should account for code duration, duty cycle, autocorrelation, and any sensor-measurement process. The synthetic demo’s independent held random codes are only an illustration; they are not a validated experimental null.

## Multiple flows and repeated challenge

Testing many flows increases the chance of at least one apparently strong result. The proposed architecture applies a false-discovery-rate correction (for example, Benjamini–Hochberg) across tested flows. The reference utility returns adjusted q-values; choosing the operational threshold is a pre-registration decision, not a threshold learned from this synthetic demo.

A candidate should then be challenged with a **second fresh code**. Repeated response to a code not known in advance is part of the concept’s confirmation logic. The final app must define how a flow is matched across rounds, what happens when channels change, and how a failed/ambiguous round is reported. Those policies are not implemented here.

The concept also proposes a sequential probability ratio test (SPRT) to stop early when evidence is decisive. No SPRT code or stopping thresholds are included in this repository.

## The covered-lens null control

The high-value physical control is to keep the camera’s traffic stream active while physically covering its lens. The stimulus still runs. If the uncovered scene produced a stimulus-linked traffic change, the response relationship should weaken or disappear when the camera cannot see the changing scene. This is an experimental hypothesis to test (E02), **not an observed result**.

A traffic drop alone is not the desired outcome: the useful control is continued traffic with loss of the stimulus-linked relationship. Record both total traffic and the causal statistic, along with any changes in network state.

## Assumptions and confounds to measure

- The selected camera actually encodes scene changes into observable traffic volume/metadata.
- The camera is transmitting on a channel and in a direction observable by the ear.
- The measured light trace and RF bins share sufficiently accurate timing.
- The stimulus is not confounded with another changing source (operator movement, network intervention, device state, or unrelated room activity).
- The selected surrogate procedure represents a meaningful null and is not selected after viewing results.
- Multiple-flow testing and any repeated rounds are included in the analysis plan.
- Traffic metadata are an indirect proxy, not decrypted video content.

## Included reference implementation

`tools/causal_reference.py` supplies:

- lagged level and transition features;
- a linear-drift baseline and ridge fit;
- score comparison against caller-supplied surrogates;
- Benjamini–Hochberg adjusted q-values.

`tools/synthetic_demo.py` constructs artificial responsive and uncoupled traces. It is explicitly synthetic. The scripts do not capture packets, identify cameras, classify devices, or validate any physical claim.

## Parameters that must be fixed for real trials

Before a physical experiment, document: bin width; stimulus bit/chip duration; sensor calibration and timestamp method; candidate-flow inclusion; channel dwell/lock policy; kernel lag grid and regularization; traffic metric; surrogate construction and count; multiple-testing family; trial stopping rule; repeat count; primary effect statistic; exclusions; null controls; and how negative/ambiguous outcomes are reported. No numerical pass thresholds are supplied by the concept brief, so this repository does not invent them.
