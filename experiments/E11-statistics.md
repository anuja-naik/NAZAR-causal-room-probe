# E11 — Statistical detector behavior

**Status:** protocol drafted; included code has synthetic unit tests only.

## Question

Does the detector produce sensible results on controlled positive and null data, and does the multiple-flow procedure control false discoveries under the intended assumptions?

## Stages

1. Unit-test time alignment, lag construction, empirical p-value calculation, and FDR adjustment on deterministic fixtures.
2. Use synthetic nulls with drift, periodic traffic, bursts, and autocorrelation, then record false-positive behavior over seeded runs.
3. Use synthetic causal traces with known delay and effect strength to check whether the lagged model recovers the injected relationship.
4. After physical collection, test the frozen analysis on real positive/control data, including E02; separate exploratory tuning from confirmatory evaluation.

## Interpretation

Synthetic tests validate only code paths and assumptions built into the simulator. They do not validate camera traffic behavior or guarantee statistical calibration on real data. Any real analysis must predefine the surrogate procedure, candidate-flow family, lag grid, and thresholds; include all tested flows and runs; and report limitations. This repository contains no real E11 result.
