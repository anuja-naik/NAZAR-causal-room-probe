# Experimental results status

**Status: no physical experimental results are included in this repository.**

The supplied NAZAR concept describes experiments that should be run, but it does not supply measured raw data, trial counts, effect sizes, camera models, plots, or outcomes. Accordingly, this file intentionally contains no claimed E01/E02/E03/E04/E06/E07/E08/E10/E11/E11e/E12 result.

The only current validation evidence is software-level testing of the reference scripts against generated synthetic data. That is recorded in the README and is not a physical sensor result.

When an experiment is actually run, add a dated, reviewable record with:

- experiment ID and preregistered protocol revision;
- date/time, operator role, setup, camera/device/hardware and software versions;
- condition, stimulus sequence identifier/hash, binning, trial duration, and number of runs;
- raw and processed data locations plus privacy/consent review;
- analysis method and parameters chosen before looking at the result;
- outcome, uncertainty, exclusions, deviations, and negative/control results;
- whether data are live, replayed, or synthetic.

Use `experiments/trial-log-template.csv` for a minimal index. Leave fields blank rather than guessing. Store sensitive/raw files outside Git unless release has been explicitly reviewed.
