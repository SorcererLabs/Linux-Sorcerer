# Linux Sorcerer – Die Akademie

*Altes Wissen für moderne Systeme.*

Deutsch | [English](README.md)

![Der Linux Sorcerer](sorcerer.png)

Linux Sorcerer ist ein kostenloses, interaktives Linux-Lernprogramm im Retro-Stil. Ein alter Magier begleitet dich durch die Grundlagen von Linux in einem simulierten Terminal, ohne echte Shellbefehle auszuführen.

## Funktionen

- 32 Lektionen zu Linux-Grundlagen und Systemverwaltung.
- Interaktives simuliertes Terminal, Befehlslexikon und Prüfungsmodus.
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

Nach der Veröffentlichung kannst du über GitHub Issues Fehler melden und neue Lektionen vorschlagen. Nenne bei Fehlern möglichst deine Linux-Distribution, Programmversion und die Schritte zur Reproduktion. Updates werden vor der Veröffentlichung gemeinsam getestet.

## Projektstatus und Lizenz

Aktuelle Version: v0.1.0-rc2 (Veröffentlichungskandidat). Weitere grafische Tests unter Linux Mint stehen aus. Das Magierbild wurde KI-generiert. Die Quellcodelizenz und die Verbreitungsbedingungen des Bildes müssen vor der öffentlichen Freigabe bestätigt werden. Unser Ziel ist ein kostenloses, quelloffenes Projekt.
