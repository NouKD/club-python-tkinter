#! /usr/bin/env python3
# coding: utf-8

import tkinter as tk
#----------------------|
from database import DataBase

FONT = "Arial 14 bold"


class Lister(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.title("Liste des patients")
        x, y = int((self.winfo_screenwidth()/2)-404), int((self.winfo_screenheight()/2)-200)
        self.geometry("808x400+{0}+{1}".format(x, y))
        self.resizable(0,0)
        self.mydb = DataBase()

        self.valeur = self.mydb.listPatients()

        cadre1 = tk.Frame(self)
        cadre1.pack(expand=1, fill="both", padx=10, pady=10)
        cadre2 = tk.Frame(self)
        cadre2.pack(expand=1, fill="both", padx=10, pady=10)

        self.listVar = tk.StringVar()
        self.liste = tk.Listbox(cadre1, cursor="hand2", font='Consolas 14', height=12, width=70,
                             listvariable=self.listVar, activestyle="dotbox")
        self.liste.grid(row=0, column=0, sticky="nsew")
        self.listVar.set(self.valeur)
        
        self.scY = tk.Scrollbar(cadre1, orient=tk.VERTICAL, command=self.liste.yview)
        self.scY.grid(row=0, column=1, sticky="ns")
        

        self.scX = tk.Scrollbar(cadre1, orient=tk.HORIZONTAL, command=self.liste.xview)
        self.scX.grid(row=1, column=0, columnspan=2, sticky="we")
        
        self.liste['xscrollcommand'] = self.scX.set
        self.liste['yscrollcommand'] = self.scY.set


        btn1 = tk.Button(cadre2, text="Consultation", font=FONT, relief="flat", command=self.InfoConsultation)
        btn1.pack(side="left", pady=5, ipadx=3, padx=10)

        btn2 = tk.Button(cadre2, text="Examen", font=FONT, relief="flat", command=self.InfoExamen)
        btn2.pack(side="left", pady=5, ipadx=3, padx=10)

        self.btnPlus = tk.Button(cadre2, text="* Plus *", font=FONT, relief="flat", command=Parcour)
        self.btnPlus.pack(side="right", pady=5, ipadx=3, padx=10)

        btn3 = tk.Button(cadre2, text="Ordonnance", font=FONT, relief="flat", command=self.InfoOrdonance)
        btn3.pack(side="right", pady=5, ipadx=3, padx=10)

        if not self.valeur:
            self.listVar.set("***----------Aucune_entree_trouves----------***")
            [btn.config(state="disabled") for btn in [btn1, btn2, btn3, self.btnPlus]]
        else:
            txt = '[Patient]: {0: <10} {1: <10}  [{2: ^15}]  Docteur: {3: <10} {4} '
            liste = [txt.format(item[0], item[1], item[2], item[3], item[4]) for item in self.valeur]
            self.listVar.set(liste)

    def InfoConsultation(self):
        index = self.liste.curselection()
        if not index: return
        idt = self.valeur[index[0]][-3]
        info = self.mydb.getOneById("consultation", "id", idt)

        txt = 'Date: {0}\nTaille: {1}\nTemperature: {2}\nGroup Sanguin: {3}\nDiagnostic: {4}'

        App = tk.Toplevel(self.master)
        App.title("Info consultation")
        lb = tk.Label(App, text=txt.format(info[3], info[4], info[5], info[6], info[7]), bg="#fff", justify="left")
        lb.pack(expand=1, fill="both", padx=10, pady=10, ipadx=10, ipady=10)


    def InfoExamen(self):
        index = self.liste.curselection()
        if not index: return
        idt = self.valeur[index[0]][-2]
        info = self.mydb.getOneById("examen", "consultation_id", idt)

        txt = 'Date: {0}\n\nType:\n{1}\n\nResultats:\n{2}'

        App = tk.Toplevel(self.master)
        App.title("Info Examen")
        lb = tk.Label(App, text=txt.format(info[4], info[3], info[2]), bg="#fff", justify="left")
        lb.pack(expand=1, fill="both", padx=10, pady=10, ipadx=10, ipady=10)

    def InfoOrdonance(self):
        index = self.liste.curselection()
        if not index: return
        idt = self.valeur[index[0]][-2]
        info = self.mydb.getOneById("ordonance", "consultation_id", idt)
        txt = 'Date: {0}\n\nPrescriptions:\n{1}'

        App = tk.Toplevel(self.master)
        App.title("Info Odonnance")
        lb = tk.Label(App, text=txt.format(info[3], info[2]), bg="#fff", justify="left")
        lb.pack(expand=1, fill="both", padx=10, pady=10, ipadx=10, ipady=10)


class Parcour(Lister):
    def __init__(self):
        Lister.__init__(self)
        self.title("Liste de toutes les visites")
        self.mydb = DataBase()
        self.valeur = self.mydb.listPatient()
        txt = " {0: <10} {1: <10} [{2: ^15}]  Docteur: {3: <10} {4: <10} | {5}  "
        values_list = [txt.format(e[0], e[1], e[2], e[3], e[4], e[5]) for e in self.valeur]
        self.listVar.set(values_list)
        self.btnPlus.destroy()





if __name__ == "__main__":
    Lister().mainloop()
    #Parcour().mainloop()