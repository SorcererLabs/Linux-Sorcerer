# Testing

## RC2 — 2026-11-25

Project owner reported passing all ten manual checks: startup, portrait, German UI, English switch, English lesson, exam mode, reference, progress after restart, switch back to German, clean exit.

Static review found no real shell execution in the simulator. This is not a comprehensive security audit.

## Expanded reference

Project owner reported 10/10 manual checks passed on 2026-11-25: reference opens, searches for sudo, chmod, systemd-analyze, Kernel and an unknown term, English language switch and explanations, normal lesson completion, and progress persistence after restart.

Pending: confirm automated test output (`python3 -m unittest -v`). The earlier full RC2 acceptance applies to the original version; the expanded reference has its own targeted acceptance above.
