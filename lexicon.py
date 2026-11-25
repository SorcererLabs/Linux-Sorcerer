# Independent reference: term, German explanation, English explanation, example
ENTRIES = [
  [
    "sudo",
    "Befehl mit Rechten eines anderen Benutzers ausführen, meist root. Nur vertrauenswürdige Befehle verwenden.",
    "Run a command as another user, usually root. Only run trusted commands.",
    "sudo -l"
  ],
  [
    "su",
    "Benutzer wechseln; ohne Namen meist root.",
    "Switch user; without a name usually root.",
    "su - username"
  ],
  [
    "root",
    "Administratorkonto mit weitreichenden Rechten.",
    "Administrator account with extensive privileges.",
    "id"
  ],
  [
    "Kernel",
    "Kern des Betriebssystems, verwaltet Hardware und Ressourcen.",
    "Operating system core managing hardware and resources.",
    "uname -r"
  ],
  [
    "Shell",
    "Befehlsinterpreter, etwa Bash.",
    "Command interpreter, such as Bash.",
    "echo $SHELL"
  ],
  [
    "Bash",
    "Eine verbreitete Shell.",
    "A widely used shell.",
    "bash --version"
  ],
  [
    "Terminal",
    "Oberfläche zur Interaktion mit einer Shell.",
    "Interface for interacting with a shell.",
    "pwd"
  ],
  [
    "Distribution",
    "Zusammenstellung von Linux-Kernel und Software.",
    "Collection of Linux kernel and software.",
    "cat /etc/os-release"
  ],
  [
    "Desktop",
    "Grafische Arbeitsumgebung, etwa MATE.",
    "Graphical desktop environment, such as MATE.",
    "echo $XDG_CURRENT_DESKTOP"
  ],
  [
    "cd",
    "Arbeitsverzeichnis wechseln.",
    "Change working directory.",
    "cd .."
  ],
  [
    "pwd",
    "Aktuelles Arbeitsverzeichnis anzeigen.",
    "Print current working directory.",
    "pwd"
  ],
  [
    "ls",
    "Verzeichnisinhalt anzeigen; -a auch versteckte Dateien, -l Details.",
    "List directory contents; -a includes hidden files, -l shows details.",
    "ls -la"
  ],
  [
    "tree",
    "Verzeichnisbaum anzeigen; eventuell nachinstallieren.",
    "Display directory tree; may require installation.",
    "tree -L 2"
  ],
  [
    "touch",
    "Leere Datei erzeugen oder Zeitstempel aktualisieren.",
    "Create an empty file or update timestamps.",
    "touch test.txt"
  ],
  [
    "mkdir",
    "Ordner erstellen; -p erstellt fehlende Elternordner.",
    "Create directories; -p creates missing parents.",
    "mkdir -p Labor"
  ],
  [
    "cp",
    "Dateien kopieren; -i fragt vor Überschreiben.",
    "Copy files; -i prompts before overwriting.",
    "cp -i a.txt b.txt"
  ],
  [
    "mv",
    "Dateien verschieben oder umbenennen; -i fragt vor Überschreiben.",
    "Move or rename files; -i prompts before overwriting.",
    "mv -i a.txt b.txt"
  ],
  [
    "rm",
    "Dateien ohne Papierkorb löschen. Pfad sorgfältig prüfen.",
    "Delete files without trash. Check the path carefully.",
    "rm -i test.txt"
  ],
  [
    "rmdir",
    "Leere Ordner entfernen.",
    "Remove empty directories.",
    "rmdir Labor"
  ],
  [
    "file",
    "Dateityp anhand des Inhalts bestimmen.",
    "Identify file type from content.",
    "file test.txt"
  ],
  [
    "stat",
    "Dateimetadaten anzeigen.",
    "Display file metadata.",
    "stat test.txt"
  ],
  [
    "chmod",
    "Zugriffsrechte ändern; 600 erlaubt nur dem Eigentümer Lesen und Schreiben.",
    "Change permissions; 600 grants only owner read and write access.",
    "chmod 600 test.txt"
  ],
  [
    "chown",
    "Eigentümer einer Datei ändern; oft Administratorrechte nötig.",
    "Change file ownership; often requires administrator privileges.",
    "man chown"
  ],
  [
    "whoami",
    "Effektiven Benutzernamen anzeigen.",
    "Show effective username.",
    "whoami"
  ],
  [
    "id",
    "Benutzer- und Gruppenkennungen anzeigen.",
    "Show user and group IDs.",
    "id"
  ],
  [
    "groups",
    "Gruppenmitgliedschaften anzeigen.",
    "Show group memberships.",
    "groups"
  ],
  [
    "cat",
    "Dateiinhalt ausgeben.",
    "Print file contents.",
    "cat test.txt"
  ],
  [
    "less",
    "Text seitenweise lesen; q beendet.",
    "Read text page by page; q quits.",
    "less test.txt"
  ],
  [
    "head",
    "Erste Zeilen anzeigen.",
    "Show first lines.",
    "head -n 5 test.txt"
  ],
  [
    "tail",
    "Letzte Zeilen anzeigen; -f verfolgt Änderungen.",
    "Show last lines; -f follows changes.",
    "tail -n 5 test.txt"
  ],
  [
    "grep",
    "Text nach Mustern durchsuchen; -i ignoriert Großschreibung.",
    "Search text for patterns; -i ignores case.",
    "grep -i linux test.txt"
  ],
  [
    "nano",
    "Einfacher Texteditor; Strg+O speichert, Strg+X beendet.",
    "Simple text editor; Ctrl+O saves, Ctrl+X exits.",
    "nano test.txt"
  ],
  [
    "wc",
    "Zeilen, Wörter und Bytes zählen.",
    "Count lines, words and bytes.",
    "wc -l test.txt"
  ],
  [
    "apt",
    "Paketverwaltung für Debian und Mint; search sucht, update erneuert Paketlisten, upgrade aktualisiert Pakete.",
    "Package manager for Debian and Mint; search finds packages, update refreshes lists, upgrade updates packages.",
    "apt search firefox"
  ],
  [
    "dpkg",
    "Debian-Pakete verwalten und auflisten.",
    "Manage and list Debian packages.",
    "dpkg -l"
  ],
  [
    "flatpak",
    "Anwendungen und Laufzeitumgebungen verwalten.",
    "Manage applications and runtimes.",
    "flatpak list"
  ],
  [
    "Paketquellen / Repositories",
    "Bezugsquellen für Software; nur vertrauenswürdige Quellen nutzen.",
    "Software sources; use only trusted repositories.",
    "apt policy"
  ],
  [
    "Abhängigkeiten / Dependencies",
    "Software, die ein anderes Programm benötigt.",
    "Software required by another program.",
    "apt depends firefox"
  ],
  [
    "shutdown",
    "System herunterfahren oder zeitgesteuert ausschalten; -c bricht geplantes Herunterfahren ab. Arbeit vorher speichern.",
    "Shut down or schedule shutdown; -c cancels scheduled shutdown. Save work first.",
    "shutdown -h +10"
  ],
  [
    "reboot",
    "System neu starten; vorher Arbeit speichern.",
    "Restart system; save work first.",
    "reboot"
  ],
  [
    "poweroff",
    "System ausschalten; vorher Arbeit speichern.",
    "Power off system; save work first.",
    "poweroff"
  ],
  [
    "systemctl",
    "Systemd-Dienste verwalten; status zeigt Zustand, Änderungen können Dienste unterbrechen.",
    "Manage systemd services; status shows state, changes may interrupt services.",
    "systemctl status"
  ],
  [
    "journalctl",
    "Systemd-Protokolle lesen.",
    "Read systemd logs.",
    "journalctl -b -p err"
  ],
  [
    "dmesg",
    "Kernelmeldungen anzeigen; Zugriff kann beschränkt sein.",
    "Show kernel messages; access may be restricted.",
    "dmesg"
  ],
  [
    "systemd-analyze",
    "Startdauer untersuchen; blame zeigt Aktivierungszeiten, nicht zwingend Verzögerungen des gesamten Starts.",
    "Inspect boot timing; blame shows activation times, not necessarily total boot delays.",
    "systemd-analyze blame"
  ],
  [
    "uptime",
    "Laufzeit und Systemlast anzeigen.",
    "Show uptime and load averages.",
    "uptime"
  ],
  [
    "lscpu",
    "CPU-Informationen anzeigen.",
    "Show CPU information.",
    "lscpu"
  ],
  [
    "lspci",
    "PCI-Geräte und mit -k Treiber anzeigen.",
    "Show PCI devices and drivers with -k.",
    "lspci -k"
  ],
  [
    "lsusb",
    "USB-Geräte anzeigen.",
    "Show USB devices.",
    "lsusb"
  ],
  [
    "inxi",
    "Systemübersicht; eventuell nachinstallieren.",
    "System overview; may require installation.",
    "inxi -F"
  ],
  [
    "sensors",
    "Temperaturen und weitere Sensorwerte anzeigen; benötigt passende Unterstützung.",
    "Show temperatures and other sensor readings; requires support.",
    "sensors"
  ],
  [
    "df",
    "Freien und belegten Platz auf Dateisystemen anzeigen.",
    "Show free and used filesystem space.",
    "df -h"
  ],
  [
    "du",
    "Speicherverbrauch von Dateien und Ordnern ermitteln.",
    "Estimate disk usage of files and directories.",
    "du -sh ."
  ],
  [
    "lsblk",
    "Blockgeräte und Partitionen auflisten.",
    "List block devices and partitions.",
    "lsblk"
  ],
  [
    "free",
    "Arbeitsspeicher und Swap anzeigen; available beachten.",
    "Show RAM and swap; note available memory.",
    "free -h"
  ],
  [
    "mount",
    "Dateisysteme einhängen oder Einhängungen anzeigen.",
    "Mount filesystems or list mounts.",
    "mount"
  ],
  [
    "umount",
    "Dateisystem aushängen; vorher offene Dateien schließen.",
    "Unmount filesystem; close open files first.",
    "man umount"
  ],
  [
    "ps",
    "Momentaufnahme laufender Prozesse anzeigen.",
    "Show a snapshot of running processes.",
    "ps aux"
  ],
  [
    "top",
    "Interaktive Prozess- und Ressourcenübersicht; q beendet.",
    "Interactive process and resource overview; q quits.",
    "top"
  ],
  [
    "htop",
    "Alternative zu top; eventuell nachinstallieren.",
    "Alternative to top; may require installation.",
    "htop"
  ],
  [
    "kill",
    "Signal an Prozess-ID senden; standardmäßig TERM.",
    "Send a signal to a process ID; defaults to TERM.",
    "man kill"
  ],
  [
    "killall",
    "Signal an Prozesse anhand ihres Namens senden; kann mehrere treffen.",
    "Signal processes by name; may affect multiple processes.",
    "man killall"
  ],
  [
    "ip",
    "Netzwerkschnittstellen und Routen anzeigen oder ändern.",
    "Inspect or change network interfaces and routes.",
    "ip addr"
  ],
  [
    "ping",
    "Erreichbarkeit testen; fehlende Antwort beweist keinen Ausfall.",
    "Test reachability; no reply does not prove an outage.",
    "ping -c 4 example.org"
  ],
  [
    "ss",
    "Netzwerkverbindungen und lauschende Ports anzeigen.",
    "Show network connections and listening ports.",
    "ss -tuln"
  ],
  [
    "wget",
    "Dateien herunterladen; Quelle prüfen.",
    "Download files; verify source.",
    "wget --help"
  ],
  [
    "curl",
    "Daten über URLs übertragen; fremde Skripte nicht blind ausführen.",
    "Transfer data via URLs; do not blindly execute remote scripts.",
    "curl --help"
  ],
  [
    "ssh",
    "Verschlüsselte Verbindung zu einem entfernten Rechner; Hostschlüssel prüfen.",
    "Encrypted connection to a remote computer; verify host key.",
    "ssh -V"
  ],
  [
    "tar",
    "Archive erstellen oder lesen; Inhalt vor Entpacken prüfen.",
    "Create or read archives; inspect contents before extraction.",
    "tar -tf archiv.tar"
  ],
  [
    "gzip",
    "Dateien komprimieren; ersetzt standardmäßig die Originaldatei.",
    "Compress files; replaces original by default.",
    "gzip -k test.txt"
  ],
  [
    "zip",
    "ZIP-Archive erstellen.",
    "Create ZIP archives.",
    "zip archiv.zip test.txt"
  ],
  [
    "unzip",
    "ZIP-Archive entpacken oder auflisten.",
    "Extract or list ZIP archives.",
    "unzip -l archiv.zip"
  ],
  [
    "man",
    "Handbuchseite lesen; q beendet.",
    "Read manual page; q quits.",
    "man ls"
  ],
  [
    "--help",
    "Bei vielen Befehlen kurze Hilfe anzeigen.",
    "Show short help for many commands.",
    "ls --help"
  ],
  [
    "whatis",
    "Kurze Beschreibung einer Handbuchseite.",
    "Short description of a manual page.",
    "whatis ls"
  ],
  [
    "apropos",
    "Handbuchseiten nach Stichwort suchen.",
    "Search manual pages by keyword.",
    "apropos network"
  ],
  [
    "$HOME",
    "Umgebungsvariable für das Heimatverzeichnis.",
    "Environment variable for home directory.",
    "echo $HOME"
  ],
  [
    "PATH",
    "Suchpfade für ausführbare Programme.",
    "Search paths for executable programs.",
    "echo $PATH"
  ],
  [
    "~",
    "Shell-Kurzform für das Heimatverzeichnis.",
    "Shell shorthand for home directory.",
    "cd ~"
  ],
  [
    "Pipe (|)",
    "Ausgabe eines Befehls an den nächsten weiterreichen.",
    "Pass output of one command to the next.",
    "ls | less"
  ],
  [
    "Umleitung / Redirection",
    "> überschreibt eine Ausgabedatei, >> hängt an; Vorsicht vor Datenverlust.",
    "> overwrites an output file, >> appends; beware of data loss.",
    "echo Hallo >> test.txt"
  ],
  [
    "Wildcard",
    "Platzhalter wie * und ? werden von der Shell expandiert.",
    "Patterns such as * and ? are expanded by the shell.",
    "ls *.txt"
  ],
  [
    "history",
    "Bisherige Shellbefehle anzeigen; kann sensible Eingaben enthalten.",
    "Show shell command history; may contain sensitive input.",
    "history"
  ],
  [
    "clear",
    "Terminalanzeige leeren.",
    "Clear terminal display.",
    "clear"
  ],
  [
    "exit",
    "Shell oder Sitzung verlassen.",
    "Leave shell or session.",
    "exit"
  ],
  [
    "find",
    "Dateien nach Kriterien suchen.",
    "Search for files by criteria.",
    "find . -name '*.txt'"
  ],
  [
    "which",
    "Pfad eines ausführbaren Programms suchen.",
    "Locate an executable in PATH.",
    "which python3"
  ],
  [
    "alias",
    "Kurzname für einen Shellbefehl.",
    "Define a shortcut for a shell command.",
    "alias"
  ],
  [
    "env",
    "Umgebungsvariablen anzeigen oder Programm mit geänderter Umgebung starten.",
    "Show environment variables or run with a modified environment.",
    "env"
  ],
  [
    "Swap",
    "Auslagerungsspeicher zur Ergänzung des RAM.",
    "Swap space supplementing RAM.",
    "free -h"
  ],
  [
    "systemd",
    "Dienst- und Systemmanager vieler Linux-Distributionen.",
    "Service and system manager used by many Linux distributions.",
    "systemctl --version"
  ],
  [
    "Dateisystem / Filesystem",
    "Struktur zur Speicherung von Dateien und Ordnern.",
    "Structure used to store files and directories.",
    "df -T"
  ],
  [
    "Prozess / Process",
    "Laufende Instanz eines Programms mit Prozess-ID.",
    "Running instance of a program with a process ID.",
    "ps"
  ],
  [
    "Dienst / Service",
    "Meist im Hintergrund laufende Systemfunktion.",
    "System function usually running in the background.",
    "systemctl list-units --type=service"
  ]
]
