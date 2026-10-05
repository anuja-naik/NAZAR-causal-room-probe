# E04 — Traffic bin-size choice

**Status:** planned; not run.

## Question

Is approximately 100 ms an appropriate aggregation interval for the selected camera and challenge timing?

## Procedure outline

Capture a time-stamped metadata trace with sufficiently fine timing, then compare only preregistered aggregation widths around the proposed 100 ms setting. Keep the stimulus and camera/network conditions fixed across comparisons where possible. Report packet/byte loss, timing uncertainty, response score, lag stability, and sensitivity to bin alignment.

## Interpretation

Choose a bin width from measured stability and the intended challenge timing, not from whichever width gives the most favorable result after unrestricted searching. If multiple widths are explored, include that selection in the statistical plan. The supplied concept proposes approximately 100 ms; this experiment has not established that it is optimal or universally suitable.
