# Linux Sorcerer – Die Akademie

*Altes Wissen für moderne Systeme.*

Deutsch | [English](README.md)

![Der Linux Sorcerer](sorcerer.png)

Linux Sorcerer ist ein kostenloses, interaktives Linux-Lernprogramm im Retro-Stil. Ein alter Magier begleitet dich durch die Grundlagen von Linux in einem simulierten Terminal, ohne echte Shellbefehle auszuführen.

## Funktionen

- 32 Lektionen zu Linux-Grundlagen und Systemverwaltung.
- Interaktives simuliertes Terminal, durchsuchbares Befehlslexikon mit 94 zusätzlichen Einträgen und Prüfungsmodus.
- Deutsche und englische Oberfläche und Lerninhalte.
- Offline lernen mit lokal gespeichertem Fortschritt.
- Gestaltung im Stil klassischer Desktop-Assistenten.

## Installation (Linux Mint, Debian, Ubuntu)

Lade das Repository herunter oder klone es und öffne ein Terminal im Programmordner.

```sh
sudo apt install python3-tk
python3 sorcerer.py
```

Wähle beim ersten Start Deutsch oder English. Über die Schaltfläche Deutsch / English kannst du später wechseln. Der gespeicherte Lern- und Prüfungsfortschritt bleibt erhalten; die aktuelle virtuelle Übung wird zurückgesetzt.

Der Fortschritt liegt unter `~/.local/share/linux-sorcerer/progress.json`. Bestehender Fortschritt aus Version 1.0 bleibt erhalten.

## Sicher lernen

Die Simulation unterstützt ausgewählte Befehle und Optionen. Ausgaben sind Beispieldaten, Prüfungen akzeptieren festgelegte Befehlsvarianten. Sie ist keine vollständige Linux-Shell. Der Installationsbefehl oben wird auf deinem echten System ausgeführt.

## Unsere Philosophie

Wissen soll allen zugänglich sein. Alle Lektionen sollen kostenlos, offline und ohne Werbung, Benutzerkonto oder Telemetrie bleiben. Unser Ziel ist Selbstständigkeit statt Abhängigkeit.

Das Projekt entstand an einem Novembermorgen 2026 bei einem Espresso und einem Gespräch über klassische Desktop-Assistenten.

## Entwicklung und Nutzerfeedback

Führe die Tests im Programmordner aus:

```sh
python3 -m unittest -v
```

Du kannst über GitHub Issues Fehler melden und neue Lektionen vorschlagen. Nenne bei Fehlern möglichst deine Linux-Distribution, Programmversion und die Schritte zur Reproduktion. Updates werden vor der Veröffentlichung gemeinsam getestet.

## Projektstatus und Lizenz

Version: v0.1.0. Die Ergebnisse der Praxis- und automatisierten Tests stehen in [TESTING.md](TESTING.md). Quellcode und Dokumentation stehen unter der [MIT-Lizenz](LICENSE); Bildrechte und Namensnennung sind in [ARTWORK.md](ARTWORK.md) dokumentiert.
