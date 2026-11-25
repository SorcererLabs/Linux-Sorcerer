# Testing

## RC2 — 2026-11-25

Project owner reported passing all ten manual checks: startup, portrait, German UI, English switch, English lesson, exam mode, reference, progress after restart, switch back to German, clean exit.

Static review found no real shell execution in the simulator. This is not a comprehensive security audit.

## Expanded reference

Pending: run `python3 -m unittest -v`, launch the GUI, verify search and both languages, and repeat the RC2 regression checks. The earlier manual acceptance does not cover this branch.
