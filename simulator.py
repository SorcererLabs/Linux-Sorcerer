import posixpath as p
import shlex
class Simulator:
    def __init__(self, lang="de"):
        self.lang=lang; self.user="apprentice" if lang=="en" else "lehrling"; self.host="academy" if lang=="en" else "akademie"
        self.home='/home/'+self.user; self.cwd=self.home
        self.dirs={'/','/home',self.home,self.home+('/Documents' if lang=='en' else '/Dokumente'),self.home+('/Pictures' if lang=='en' else '/Bilder')}
        self.files={self.home+('/note.txt' if lang=='en' else '/notiz.txt'):('Welcome to Linux!\nKnowledge is power.' if lang=='en' else 'Willkommen bei Linux!\nWissen ist Macht.'),self.home+('/.profile' if lang=='en' else '/.profil'):('# Virtual profile' if lang=='en' else '# Virtuelles Profil')}
    def translate(self,s):
        if self.lang=="en":
            for a,b in {'lehrling': 'apprentice', 'Webbrowser': 'Web browser', 'Beispieldaten': 'Sample data', 'Dateisystem  Größe  Belegt  Frei': 'Filesystem   Size  Used   Free', 'Keine Fehler im virtuellen Journal.': 'No errors in the virtual journal.', 'OPTIONEN': 'OPTIONS', 'PFAD': 'PATH', 'versteckte Dateien anzeigen': 'show hidden files', 'ausführliche Liste': 'detailed listing', 'Ausschalten in 10 Minuten geplant.': 'Shutdown scheduled in 10 minutes.', 'Ausschalten angefordert.': 'Shutdown requested.', 'Ausschaltvorgang abgebrochen.': 'Shutdown cancelled.', 'Neustart angefordert.': 'Restart requested.', 'Keine Fehler.': 'No errors.', 'Syntaxfehler: ': 'Syntax error: ', 'Verzeichnis nicht gefunden.': 'Directory not found.', 'Unterstützt: ls [-al] [Ordner]': 'Supported: ls [-al] [directory]', 'Nicht möglich: Pfad oder Dateityp prüfen.': 'Cannot complete: check path or file type.', 'Quelle oder Ziel ungültig.': 'Invalid source or destination.', 'Datei nicht gefunden.': 'File not found.', 'Dieser Befehl ist in der Akademie nicht verfügbar. Keine echten Befehle werden ausgeführt.': 'This command is unavailable in the Academy. No real commands are executed.'}.items():s=s.replace(a,b)
        return s
    def path(self,s):
        if s=='~' or s.startswith('~/'): s=self.home+s[1:]
        return p.normpath(p.join(self.cwd,s))
    def run(self,line):
        try:
            args=shlex.split(line);out,ok=self._run(args);return (self.translate(out) if not ok or (args and args[0] not in ("echo","cat","grep","ls","pwd")) else out),ok
        except ValueError as e: return self.translate('Syntaxfehler: '+str(e)),False
    def _run(self,a):
        if not a:return '',False
        c,*v=a; key=' '.join(a)
        fixed={'uname -s':'Linux','whoami':'lehrling','id':'uid=1000(lehrling) gid=1000(lehrling)','apt search firefox':'firefox – Webbrowser (Beispieldaten)','apt show firefox':'Package: firefox\nDescription: Webbrowser (Beispieldaten)','ps aux':'USER       PID  COMMAND\nlehrling  1024  mate-session\nlehrling  1100  pipewire','systemctl --user status pipewire':'pipewire.service – PipeWire\nActive: active (running)','df -h':'Dateisystem  Größe  Belegt  Frei\n/dev/sda1     100G    35G   65G','lsblk':'NAME   SIZE TYPE\nsda    100G disk\n└─sda1 100G part','ip addr':'1: lo: 127.0.0.1/8\n2: eth0: 192.168.1.20/24','ip a':'1: lo: 127.0.0.1/8\n2: eth0: 192.168.1.20/24','ip route':'default via 192.168.1.1 dev eth0','free -h':'       total  used  free\nMem:    16Gi   4Gi  12Gi','uptime':'up 2 hours, load average: 0.20, 0.15, 0.10','journalctl -p err':'Keine Fehler im virtuellen Journal.','man ls':'ls [OPTIONEN] [PFAD]\n-a: versteckte Dateien anzeigen\n-l: ausführliche Liste','ps':'PID COMMAND\n1100 pipewire'}
        fixed.update({'shutdown -h +10':'[Simulation] Ausschalten in 10 Minuten geplant.','shutdown -h now':'[Simulation] Ausschalten angefordert.','shutdown -c':'[Simulation] Ausschaltvorgang abgebrochen.','reboot':'[Simulation] Neustart angefordert.','systemd-analyze':'Startup finished in 3.2s (kernel) + 6.6s (userspace) = 9.8s','systemd-analyze blame':'4.0s NetworkManager-wait-online.service\n2.1s NetworkManager.service\n0.8s systemd-journald.service','systemd-analyze critical-chain':'graphical.target @6.6s\n└─multi-user.target @6.5s\n  └─NetworkManager.service @4.4s +2.1s','journalctl -b -p err':'[Beispieldaten] Keine Fehler.','lscpu':'Architecture: x86_64\nCPU(s): 8\nCore(s) per socket: 4\nThread(s) per core: 2','lspci -k':'01:00.0 VGA compatible controller: Example GPU\n  Kernel driver in use: amdgpu','lsusb':'Bus 001 Device 002: Example USB Keyboard','inxi -F':'System: Linux Mint (Beispieldaten)\nCPU: 4-core\nMemory: 16 GiB','sensors':'coretemp-isa-0000\nCore 0: +42.0°C'})
        if key in fixed:return fixed[key],True
        if c=='pwd' and not v:return self.cwd,True
        if c=='echo':return ' '.join(x.replace('$HOME',self.home) for x in v),True
        if c=='cd' and len(v)<=1:
            t=self.path(v[0]) if v else self.home
            if t in self.dirs:self.cwd=t;return '',True
            return 'Verzeichnis nicht gefunden.',False
        if c=='ls':
            flags=''.join(x[1:] for x in v if x.startswith('-')); args=[x for x in v if not x.startswith('-')]
            if any(x not in 'al' for x in flags) or len(args)>1:return 'Unterstützt: ls [-al] [Ordner]',False
            t=self.path(args[0]) if args else self.cwd
            if t not in self.dirs:return 'Verzeichnis nicht gefunden.',False
            names=sorted(x for x in self.dirs|self.files.keys() if x!=t and p.dirname(x)==t and ('a' in flags or not p.basename(x).startswith('.')))
            return '\n'.join(('d ' if x in self.dirs else '- ') + p.basename(x) if 'l' in flags else p.basename(x) for x in names),True
        if c in ('mkdir','touch','cat','rm','rmdir') and len(v)==1 and not v[0].startswith('-'):
            t=self.path(v[0]); exists=t in self.dirs or t in self.files
            if c=='cat' and t in self.files:return self.files[t],True
            if c=='rm' and t in self.files:del self.files[t];return '',True
            if c=='rmdir' and t in self.dirs and t not in ('/','/home',self.home,self.cwd) and not any(x.startswith(t+'/') for x in self.dirs|self.files.keys()):self.dirs.remove(t);return '',True
            if c in ('mkdir','touch') and not exists and p.dirname(t) in self.dirs:
                if c=='mkdir':self.dirs.add(t)
                else:self.files[t]=''
                return '',True
            if c=='touch' and t in self.files:return '',True
            return 'Nicht möglich: Pfad oder Dateityp prüfen.',False
        if c in ('cp','mv') and len(v)==2 and not any(x.startswith('-') for x in v):
            s,t=map(self.path,v)
            if t in self.dirs:t=p.join(t,p.basename(s))
            if s in self.files and p.dirname(t) in self.dirs and t not in self.dirs and s!=t:
                self.files[t]=self.files[s]
                if c=='mv':del self.files[s]
                return '',True
            return 'Quelle oder Ziel ungültig.',False
        if c=='grep' and len(v)==2:
            t=self.path(v[1]);return ('\n'.join(x for x in self.files[t].splitlines() if v[0] in x),True) if t in self.files else ('Datei nicht gefunden.',False)
        return 'Dieser Befehl ist in der Akademie nicht verfügbar. Keine echten Befehle werden ausgeführt.',False
