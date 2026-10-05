# Experiment plan and status

The experiments below translate the supplied NAZAR validation checklist into reviewable protocols. They are plans, not findings. No physical data, trial log, or result is included.

## Current status

| ID | Question | Status in this repository |
|---|---|---|
| E01 | Does encrypted camera traffic respond to the measured light stimulus? | Protocol drafted; not run |
| E02 | With traffic continuing, does covering the lens reduce the stimulus-linked relationship? | Protocol drafted; not run |
| E03 | Does the selected camera exhibit variable-bitrate response to scene changes? | Protocol drafted; not run |
| E04 | Is approximately 100 ms a useful bin size for the selected camera? | Protocol drafted; not run |
| E06 | Does flash ON/OFF differencing isolate candidate reflections? | Protocol drafted; not run |
| E07 | Can a lens-vs-clutter dataset support a local candidate classifier? | Protocol drafted; no dataset/model |
| E08 | Does a real lens candidate persist geometrically across views better than ordinary reflections? | Protocol drafted; not run |
| E10 | Is phone–ear USB-C OTG communication stable enough for a probe? | Protocol drafted; no hardware |
| E11 | Does the statistical detector behave appropriately on positive and null data? | Protocol drafted; synthetic code checks only |
| E11e | Does a one-byte evidence edit cause verification failure? | Protocol drafted; hash-chain utility unit test only; no signature test |
| E12 | Can a judge/manual light change act as a measured stimulus? | Protocol drafted; not run |

The experiment identifiers follow the supplied checklist; unused identifiers are not filled in or inferred.

## Before a physical run

- Obtain authorization and complete the review in `../ethics/LEGAL_NOTES.md`.
- Record protocol revision, setup, camera, network condition, stimulus settings, sample/bin timing, trial count, and analysis method before viewing outcomes.
- Include negative/null controls and preserve unexpected outcomes.
- Keep raw captures local and out of Git until reviewed; do not collect payloads, credentials, probe requests, faces, or unnecessary room video.
- Mark every trace as `LIVE`, `REPLAY`, or `SYNTHETIC`.
- Use `trial-log-template.csv` for the experiment index; leave unknown fields blank.

## Reporting rules

Report measurement conditions, number of trials/samples, effect sizes, uncertainty, exclusions, and deviations. Do not invent pass thresholds after seeing the data. Do not convert a synthetic output into a physical result. See `RESULTS.md` for the current no-results disclosure.
