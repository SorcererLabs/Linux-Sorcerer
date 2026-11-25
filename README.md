# Linux Sorcerer – Die Akademie

*Ancient Wisdom for Modern Systems.*

Ein offline nutzbares Linux-Lernprogramm im Stil klassischer Desktop-Assistenten. 32 Lektionen, ein simuliertes Terminal, Befehlslexikon und Prüfungsmodus. Keine echten Shellbefehle werden ausgeführt. Die Lernoberfläche ist derzeit deutsch.

## Installation (Linux Mint / Debian / Ubuntu)

```sh
sudo apt install python3-tk
python3 sorcerer.py
```

Entpacke das Archiv und führe den zweiten Befehl im Programmordner aus. Fortschritt wird lokal unter `~/.local/share/linux-sorcerer/progress.json` gespeichert. Bestehender Fortschritt aus 1.0 bleibt erhalten. Die Simulation unterstützt nur ausgewählte Befehle und Optionen; Ausgaben sind Beispieldaten. Prüfungen akzeptieren festgelegte Befehlsvarianten.

## English

A retro-styled, offline Linux learning application with 32 lessons, a safe simulated terminal, a command reference and an exam mode. The current application language is German. Install Python 3 and Tkinter using the commands above, then launch from the extracted directory. No real shell commands are executed by the simulator. Progress is stored locally. Contributions and translations are welcome once the project is published.

## Development

Run `python3 -m unittest -v` from the project directory. This is a release candidate, not a published release. The graphical interface needs further testing on Linux Mint. The artwork was AI-generated. License selection and artwork distribution terms must be confirmed by the project owner before public release.

### Sprache / Language (RC2)
Beim ersten Start Deutsch oder English auswählen. Über die Schaltfläche Deutsch / English kann die Sprache später geändert werden. Der gespeicherte Lern- und Prüfungsfortschritt bleibt erhalten; die aktuelle virtuelle Übung wird zurückgesetzt.

Choose Deutsch or English on first launch. Use the Deutsch / English button to switch later. Saved lesson and exam progress is retained; the current virtual exercise is reset.
