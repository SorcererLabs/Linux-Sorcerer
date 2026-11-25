# Linux Sorcerer

*Ancient Wisdom for Modern Systems.*

[Deutsch](README.de.md) | English

![The Linux Sorcerer](sorcerer.png)

Linux Sorcerer is a free, retro-styled interactive Linux learning application. An ancient sorcerer guides you through the fundamentals of Linux in a simulated terminal, without executing real shell commands.

## Features

- 32 lessons covering Linux fundamentals and system administration.
- Interactive terminal simulator, searchable reference with 94 additional entries, and exam mode.
- English and German interfaces and learning materials.
- Offline learning with locally saved progress.
- Classic desktop-assistant design.

## Getting started (Linux Mint, Debian, Ubuntu)

Download or clone the repository, then open a terminal in the project directory.

```sh
sudo apt install python3-tk
python3 sorcerer.py
```

Choose English or Deutsch on first launch. You can switch languages later using the Deutsch / English button. Saved lesson and exam progress is retained; the current virtual exercise resets.

Progress is stored in `~/.local/share/linux-sorcerer/progress.json`. Existing progress from version 1.0 is retained.

## Learning safely

The simulator supports selected commands and options only. Its outputs are illustrative, and exams accept predefined command variants. It is not a full Linux shell. The installation command above runs on your real system.

## Our philosophy

Knowledge should be accessible to everyone. We aim to keep every lesson free, offline and free of advertising, accounts and telemetry. The goal is to teach independence, not dependence.

The project began on a November morning in 2026 with an espresso and a conversation about classic desktop assistants.

## Development and feedback

Run the tests from the project directory:

```sh
python3 -m unittest -v
```

Use GitHub Issues to report bugs or suggest lessons. Please include your Linux distribution, application version and steps to reproduce any problem. Updates are tested together before release.

## Project status and licensing

Version: v0.1.0. Manual acceptance and automated test results are documented in [TESTING.md](TESTING.md). Source code and documentation are licensed under [MIT](LICENSE); artwork terms and attribution are in [ARTWORK.md](ARTWORK.md).
