#! /usr/bin/env python3
# coding: utf-8

import tkinter as tk
from tkinter.ttk import Combobox
#----------------------|
from database import DataBase, verify
from medecin import attribuerMedecin

FONT = "Arial 14 bold"


class AddService(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.title("Service")
        x, y = int((self.winfo_screenwidth()/2)-275), int((self.winfo_screenheight()/2)-120)
        self.geometry("550x240+{0}+{1}".format(x, y))
        self.resizable(0,0)
        
        self.mydb = DataBase()
        
        frm1 = tk.Frame(self)
        frm1.pack(expand=1, fill="both")
        
        frm2 = tk.Frame(self)
        frm2.pack(expand=1, fill="both")
        
        cadre1 = tk.Frame(frm1)
        cadre1.pack(expand=1, fill="both", side="left", padx="5 0", pady=5, ipadx=5, ipady=5)
        cadre2 = tk.Frame(frm1)
        cadre2.pack(expand=1, fill="both", side="right", padx="0 5", pady=5, ipadx=5, ipady=5)
        
        lb1 = tk.Label(cadre1, text="Nom: ",anchor="w", font=FONT, bg="#eee", fg="grey")
        lb1.pack(expand=1, fill="both", padx=5, pady="5 0", ipady=5, ipadx=5)
        self.nom = tk.Entry(cadre1, font=FONT, bg="#fff", fg="#000")
        self.nom.pack(expand=1, fill="both", padx=5, ipady=5, ipadx=5)

        lb1 = tk.Label(cadre1, text="Batiment: ",anchor="w", font=FONT, bg="#eee", fg="grey")
        lb1.pack(expand=1, fill="both", padx=5, pady="5 0", ipady=5, ipadx=5)
        self.batiment = tk.Entry(cadre1, font=FONT, bg="#fff", fg="#000")
        self.batiment.pack(expand=1, fill="both", padx=5, ipady=5, ipadx=5)

        lb = tk.Label(cadre2, text="Description:", font=FONT, bg="#eee", fg="grey")
        lb.pack(expand=1, fill="both", ipady=5, padx=5, pady="5 0")
        self.description = tk.Text(cadre2, font=FONT, relief="flat", height=5, bd=5, bg="#fff")
        self.description.pack(expand=1, fill="both", padx=5)

        btn_cadre = tk.Frame(frm2)
        btn_cadre.pack(expand=1, fill="both", ipadx=5, ipady=5)

        btn = tk.Button(btn_cadre, text="Annuler", font=FONT, fg="grey", relief="flat", command=self.destroy)
        btn.pack(expand=1, fill="both", side="left", padx=15, pady=15)

        btn = tk.Button(btn_cadre, text="Save", font=FONT, fg="grey", relief="flat", command=self.saveService)
        btn.pack(expand=1, fill="both", side="right", padx=15, pady=15)

        self.champs_list = [self.nom, self.batiment]

    def saveService(self):
        all_is_valide = verify(self.champs_list)
        if not self.description.get("1.0", "end").strip():
            self.description.config(bg="red")
            self.master.bell()
            all_is_valide = False
        else:
            self.description.config(bg="#fff")
        if all_is_valide:
            values = (self.nom.get().strip().upper(), self.description.get("1.0", "end").capitalize(), self.batiment.get().strip().title())
            self.mydb.setService(values)
            [e.delete(0, "end") for e in self.champs_list]
            self.description.delete("1.0", "end")


class SelectService(tk.Toplevel):
    def __init__(self, compte=None):
        tk.Toplevel.__init__(self)
        x, y = int((self.winfo_screenwidth()/2)-129), int((self.winfo_screenheight()/2)-111)
        self.geometry("310x222+{0}+{1}".format(x, y))
        
        self.compte = compte
        
        self.title("Service [Compte id: {}]".format(self.compte))

        self.mydb = DataBase()
        self.services = self.mydb.getAll("service")
        services_liste = [service[1] for service in self.services]

        self.var_nom = tk.StringVar()
        self.var_description = tk.StringVar()
        self.var_batiment = tk.StringVar()

        selection = Combobox(self, justify="center", textvariable=self.var_nom, state="readonly", font=FONT, values=services_liste)
        selection.pack(expand=1, fill="x", padx=5, pady="5 0", ipady=5, ipadx=5)
        self.var_nom.trace("w", self.change)
        self.var_nom.set(services_liste[0])
        

        lb1 = tk.Label(self, text="",anchor="w", wraplength=300, height=4, font="Arial 12 normal", bg="#fff", fg="grey", textvariable=self.var_description)
        lb1.pack(expand=1, fill="both", padx=5, pady="5 0", ipady=5, ipadx=5)

        lb = tk.Label(self, text="", font=FONT, bg="#fff", fg="grey", textvariable=self.var_batiment)
        lb.pack(expand=1, fill="x", ipady=5, padx=5, pady="2 5")

        btn = tk.Button(self, text="Continuer", font=FONT, fg="grey", relief="flat", command=self.continuer)
        btn.pack(expand=1, fill="both", side="right", padx=25, pady=5)

    def change(self, *_):
        choix = self.var_nom.get()
        liste = [item for item in self.services if choix in item][0]
        self.var_description.set(liste[2])
        self.var_batiment.set(liste[3])

    def continuer(self):
        choix = self.var_nom.get()
        liste = [item for item in self.services if choix in item][0]
        service = liste[0]
        attribuerMedecin(self, self.compte, service)





if __name__ == "__main__":
    AddService().mainloop()
    SelectService().mainloop()