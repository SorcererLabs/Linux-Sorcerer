#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox
from pathlib import Path
import json, shlex
from lessons import LESSONS as DE, LESSONS_EN as EN
LESSONS=DE
UI={'Linux Sorcerer – Die Akademie': 'Linux Sorcerer – The Academy', 'Das Wissensbuch': 'The Book of Knowledge', 'Übungsterminal – vollständig simuliert': 'Practice terminal – fully simulated', 'Ausführen': 'Run', 'Hinweis': 'Hint', 'Übung zurücksetzen': 'Reset exercise', 'Befehlslexikon': 'Command reference', 'Beenden': 'Exit', 'Weiter >': 'Next >', '< Zurück': '< Back', 'Prüfungsmodus': 'Exam mode', 'Fortschritt konnte nicht gespeichert werden: ': 'Could not save progress: ', 'Beispiel: ': 'Example: ', 'Prüfung: Löse die Aufgabe ohne Beispiel oder Hinweis.': 'Exam: solve the exercise without an example or hint.', 'Deine Aufgabe: ': 'Your task: ', 'Willkommen, Lehrling. Hier kannst du gefahrlos üben.\n': 'Welcome, apprentice. You can practice safely here.\n', 'Ausgezeichnet, Lehrling! Diese Aufgabe ist gemeistert.': 'Excellent, apprentice! You have mastered this exercise.', 'Der Befehl war gültig. Versuche nun die gestellte Aufgabe.': 'The command was valid. Now try the assigned exercise.', 'Prüfe den Befehl oder nutze den Hinweis.': 'Check the command or use the hint.', 'Im Prüfungsmodus gibt es keine Hinweise.': 'Hints are unavailable in exam mode.', 'Versuche: ': 'Try: ', 'Lexikon im Prüfungsmodus gesperrt.': 'Reference unavailable in exam mode.', 'Sorcerer – Befehlslexikon': 'Sorcerer – Command reference'}
LANG="de"
def tr(s): return UI.get(s,s) if LANG=="en" else s

from simulator import Simulator
BASE=Path(__file__).resolve().parent
SAVE=Path.home()/'.local/share/linux-sorcerer/progress.json'
GRAY='#c0c0c0'; BLUE='#000080'
def set_language(lang):
    global LANG, LESSONS
    LANG=lang; LESSONS=EN if lang=='en' else DE

def choose_language(root):
    w=tk.Toplevel(root);w.title('Linux Sorcerer – Sprache / Language');w.configure(bg=GRAY);w.resizable(False,False)
    result=[None]
    tk.Label(w,text='Sprache wählen / Choose your language',bg=BLUE,fg='white',padx=20,pady=12).pack(fill='x')
    def select(lang):result[0]=lang;w.destroy()
    for lang,label in [('de','Deutsch'),('en','English')]:
        tk.Button(w,text=label,width=28,command=lambda l=lang:select(l)).pack(padx=24,pady=8)
    w.update_idletasks();w.geometry('+%d+%d'%((w.winfo_screenwidth()-w.winfo_reqwidth())//2,(w.winfo_screenheight()-w.winfo_reqheight())//2));w.grab_set();root.wait_window(w);return result[0]

class Academy:
    def __init__(self,root):
        self.root=root; root.title(tr('Linux Sorcerer – Die Akademie'));root.geometry('940x700');root.minsize(760,600);root.configure(bg=GRAY)
        root.option_add('*Font','TkDefaultFont 11');root.option_add('*Background',GRAY);root.option_add('*Foreground','black')
        self.done=set(); self.index=0; self.exam_done=set(); self.exam=tk.BooleanVar(value=False)
        try:
            d=json.loads(SAVE.read_text());self.exam_done={i for i in d.get('exam_done',[]) if type(i)==int and 0<=i<len(LESSONS)};self.done={i for i in d['done'] if type(i)==int and 0<=i<len(LESSONS)};self.index=max(0,min(len(LESSONS)-1,int(d['index'])))
        except (OSError,ValueError,KeyError,TypeError):pass
        tk.Label(root,text='  Linux Sorcerer   |   Ancient Wisdom for Modern Systems',bg=BLUE,fg='white',anchor='w',font=('TkDefaultFont',13,'bold')).pack(fill='x',padx=4,pady=4)
        body=tk.Frame(root);body.pack(fill='both',expand=True,padx=8,pady=4)
        left=tk.Frame(body,width=220,relief='sunken',bd=2);left.pack(side='left',fill='y');left.pack_propagate(False)
        try:
            self.pic=tk.PhotoImage(file=BASE/'sorcerer.png');tk.Label(left,image=self.pic).pack(pady=5)
        except tk.TclError:pass
        tk.Label(left,text=tr('Das Wissensbuch'),font=('TkDefaultFont',12,'bold')).pack()
        lf=tk.Frame(left);lf.pack(fill='both',expand=True);scroll=tk.Scrollbar(lf);scroll.pack(side='right',fill='y');self.list=tk.Listbox(lf,bg='white',exportselection=False,yscrollcommand=scroll.set,font=('TkDefaultFont',10));self.list.pack(fill='both',expand=True);scroll.config(command=self.list.yview);self.list.bind('<<ListboxSelect>>',self.select)
        right=tk.Frame(body);right.pack(side='left',fill='both',expand=True,padx=10)
        self.title=tk.Label(right,anchor='w',font=('TkDefaultFont',17,'bold'));self.title.pack(fill='x')
        self.explain=tk.Text(right,height=7,wrap='word',bg='white',relief='sunken',padx=8,pady=8);self.explain.pack(fill='x',pady=6)
        self.example=tk.Label(right,anchor='w',font=('TkFixedFont',11),justify='left');self.example.pack(fill='x')
        self.task=tk.Label(right,anchor='w',justify='left',wraplength=500,font=('TkDefaultFont',11,'bold'));self.task.pack(fill='x',pady=6)
        tk.Label(right,text=tr('Übungsterminal – vollständig simuliert'),anchor='w').pack(fill='x')
        self.term=tk.Text(right,bg='#101810',fg='#a8e5a8',font=('TkFixedFont',11),height=9,wrap='word',state='disabled');self.term.pack(fill='both',expand=True)
        line=tk.Frame(right);line.pack(fill='x',pady=4);self.entry=tk.Entry(line,bg='white',font=('TkFixedFont',12));self.entry.pack(side='left',fill='x',expand=True);self.entry.bind('<Return>',lambda e:self.execute());tk.Button(line,text=tr('Ausführen'),command=self.execute).pack(side='right')
        self.feedback=tk.Label(right,anchor='w',justify='left',wraplength=500);self.feedback.pack(fill='x',pady=3)
        tools=tk.Frame(right);tools.pack(fill='x');tk.Button(tools,text=tr('Hinweis'),command=self.hint).pack(side='left');tk.Button(tools,text=tr('Übung zurücksetzen'),command=self.load).pack(side='left',padx=4);tk.Button(tools,text=tr('Befehlslexikon'),command=self.lexicon).pack(side='right')
        bottom=tk.Frame(root,relief='groove',bd=2);bottom.pack(fill='x',padx=8,pady=6);self.progress=tk.Label(bottom);self.progress.pack(side='left',padx=8);tk.Button(bottom,text=tr('Beenden'),command=root.destroy).pack(side='right',padx=4,pady=5);tk.Button(bottom,text=tr('Weiter >'),command=lambda:self.move(1)).pack(side='right',padx=4);tk.Button(bottom,text=tr('< Zurück'),command=lambda:self.move(-1)).pack(side='right',padx=4)
        tk.Checkbutton(tools,text=tr('Prüfungsmodus'),variable=self.exam,command=self.load).pack(side='left');tk.Button(bottom,text='Deutsch / English',command=self.change_language).pack(side='right',padx=4);self.refresh();self.load()
    def change_language(self):
        chosen=choose_language(self.root)
        if chosen and chosen!=LANG:
            self.save();set_language(chosen)
            for child in self.root.winfo_children():child.destroy()
            self.__init__(self.root);self.save()
    def save(self):
        try:
            SAVE.parent.mkdir(parents=True,exist_ok=True);tmp=SAVE.with_suffix('.tmp');tmp.write_text(json.dumps({'done':sorted(self.done),'index':self.index,'exam_done':sorted(self.exam_done),'language':LANG}));tmp.replace(SAVE)
        except OSError as e:self.feedback.config(text=tr('Fortschritt konnte nicht gespeichert werden: ')+str(e))
    def refresh(self):
        self.list.delete(0,'end')
        for i,l in enumerate(LESSONS):self.list.insert('end',('✓ ' if i in self.done else '   ')+str(i+1)+'. '+l[0])
        self.list.selection_set(self.index);self.list.see(self.index);self.progress.config(text=f'{len(self.done)}/{len(LESSONS)} '+('Lessons | Exam: ' if LANG=='en' else 'Lektionen | Prüfung: ')+f'{len(self.exam_done)}/{len(LESSONS)}')
    def select(self,event):
        s=self.list.curselection()
        if s and s[0]!=self.index:self.index=s[0];self.load();self.save()
    def move(self,n):
        self.index=max(0,min(len(LESSONS)-1,self.index+n));self.refresh();self.load();self.save()
    def output(self,s,clear=False):
        self.term.config(state='normal')
        if clear:self.term.delete('1.0','end')
        self.term.insert('end',s);self.term.see('end');self.term.config(state='disabled')
    def load(self):
        self.sim=Simulator(LANG);title,ex,example,task,answers=LESSONS[self.index];self.title.config(text=f'{self.index+1}. {title}');self.explain.config(state='normal');self.explain.delete('1.0','end');self.explain.insert('1.0',ex);self.explain.config(state='disabled');self.example.config(text='' if self.exam.get() else tr('Beispiel: ')+example);
        if self.exam.get():
            self.explain.config(state='normal');self.explain.delete('1.0','end');self.explain.insert('1.0',tr('Prüfung: Löse die Aufgabe ohne Beispiel oder Hinweis.'));self.explain.config(state='disabled')
        self.task.config(text=tr('Deine Aufgabe: ')+task);self.output(tr('Willkommen, Lehrling. Hier kannst du gefahrlos üben.\n'),True);self.feedback.config(text='');self.entry.delete(0,'end');self.entry.focus_set()
    def execute(self):
        line=self.entry.get().strip()
        if not line:return
        self.entry.delete(0,'end');cwd=self.sim.cwd;out,ok=self.sim.run(line);self.output(f'{self.sim.user}@{self.sim.host}:{cwd}$ {line}\n'+(out+'\n' if out else ''))
        try:normalized=' '.join(shlex.split(line))
        except ValueError:normalized=''
        if ok and normalized in LESSONS[self.index][4].split('|'):
            self.done.add(self.index);
            if self.exam.get():self.exam_done.add(self.index)
            self.feedback.config(text=tr('Ausgezeichnet, Lehrling! Diese Aufgabe ist gemeistert.'),fg='#005500');self.refresh();self.save()
        else:self.feedback.config(text=tr('Der Befehl war gültig. Versuche nun die gestellte Aufgabe.') if ok else tr('Prüfe den Befehl oder nutze den Hinweis.'),fg='black')
    def hint(self):self.feedback.config(text=tr('Im Prüfungsmodus gibt es keine Hinweise.') if self.exam.get() else tr('Versuche: ')+LESSONS[self.index][2],fg='black')
    def lexicon(self):
        if self.exam.get():self.feedback.config(text=tr('Lexikon im Prüfungsmodus gesperrt.'));return
        w=tk.Toplevel(self.root);w.title(tr('Sorcerer – Befehlslexikon'));w.geometry('650x500');q=tk.Entry(w,bg='white');q.pack(fill='x',padx=8,pady=8);t=tk.Text(w,bg='white',wrap='word',padx=8,pady=8);t.pack(fill='both',expand=True,padx=8,pady=8)
        def update(*_):
            needle=q.get().lower();t.config(state='normal');t.delete('1.0','end')
            for title,ex,example,_,_ in LESSONS:
                if needle in (title+' '+ex+' '+example).lower():t.insert('end',title+' — '+example+'\n'+ex+'\n\n')
            t.config(state='disabled')
        q.bind('<KeyRelease>',update);update();q.focus_set()
if __name__=='__main__':
    root=tk.Tk();root.withdraw()
    try: lang=json.loads(SAVE.read_text()).get('language')
    except (OSError,ValueError,AttributeError):lang=None
    if lang not in ('de','en'):lang=choose_language(root)
    if lang:
        set_language(lang);app=Academy(root);app.save();root.deiconify();root.mainloop()
    else:root.destroy()
