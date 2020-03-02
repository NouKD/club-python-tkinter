#! /usr/bin/env python3
# coding: utf-8

import tkinter as tk
import time as tm
#----------------------|
from database import DataBase, verify
from service import SelectService, AddService
from medecin import NewMedecin
from liste import Lister


FONT = "Arial 14 bold"


class Index(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, bg="#eee")
        self.pack(expand=1, fill="both", ipady=5, ipadx=5)
        self.master.title("Logiciel Medicale")
        x, y = int((self.winfo_screenwidth()/2)-225), int((self.winfo_screenheight()/2)-175)
        self.master.geometry("450x350+{0}+{1}".format(x, y))
        self.master.resizable(0,0)
        
        self.mydb = DataBase()
        
        cadre1 = tk.LabelFrame(self, text=" NOUVEAU COMPTE ", bg="#eee", fg="red")
        cadre1.pack(expand=1, fill="both", padx=5, pady=10, ipady=5, ipadx=5)
        cadre2 = tk.LabelFrame(self, text=" J'AI DEJA UN COMPTE ", bg="#eee", fg="#0ac94a")
        cadre2.pack(expand=1, fill="both", padx=5, pady=10, ipady=5, ipadx=5)


        lb1 = tk.Label(cadre1, text="Nom: ",anchor="w", font=FONT, bg="#eee", fg="grey")
        lb1.grid(row=0, column=0, sticky="we", padx=5, pady="5 0")
        self.nom = tk.Entry(cadre1, font=FONT, bg="#fff", fg="#000")
        self.nom.grid(row=1, column=0, sticky="we", padx=5)

        lb1 = tk.Label(cadre1, text="Contact: ",anchor="w", font=FONT, bg="#eee", fg="grey")
        lb1.grid(row=0, column=1, sticky="we", padx=5, pady="5 0")
        self.contact = tk.Entry(cadre1, font=FONT, bg="#fff", fg="#000")
        self.contact.grid(row=1, column=1, sticky="we", padx=5)

        lb1 = tk.Label(cadre1, text="Prenom: ",anchor="w", font=FONT, bg="#eee", fg="grey")
        lb1.grid(row=2, column=0, sticky="we", padx=5, pady="5 0")
        self.prenom = tk.Entry(cadre1, font=FONT, bg="#fff", fg="#000")
        self.prenom.grid(row=3, column=0, sticky="we", padx=5)

        lb1 = tk.Label(cadre1, text="Adresse: ",anchor="w", font=FONT, bg="#eee", fg="grey")
        lb1.grid(row=2, column=1, sticky="we", padx=5, pady="5 0")
        self.adresse = tk.Entry(cadre1, font=FONT, bg="#fff", fg="#000")
        self.adresse.grid(row=3, column=1, sticky="we", padx=5)

        lb1 = tk.Label(cadre1, text="REFERENT (Contact):",anchor="w", font=FONT, bg="#eee", fg="grey")
        lb1.grid(row=4, column=0, sticky="we", padx=5, pady="10 0", ipady=1)
        self.referent = tk.Entry(cadre1, font=FONT, bg="#fff", fg="#000")
        self.referent.grid(row=4, column=1, sticky="we", padx=5, pady="10 0")
    
        btn = tk.Button(cadre1, text="Enregister et continuer", font=FONT, relief="flat", command=self.enregistrer)
        btn.grid(row=5, column=0, columnspan=2, ipadx=10, ipady=2, pady="20 0")


        lb1 = tk.Label(cadre2, text="Compte : ", relief="flat",anchor="w", font=FONT, bg="#eee", fg="grey")
        lb1.pack(side="left", pady=5, ipadx=3, ipady=3, padx="3 0")
        self.compte_id = tk.Entry(cadre2, font=FONT, bg="#fff", relief="flat", justify="center", fg="#000")
        self.compte_id.pack(side="left", pady=5, ipadx=3, ipady=3)
    
        btn2 = tk.Button(cadre2, text="Continuer", font=FONT, relief="flat", command=self.continuer)
        btn2.pack(side="left", pady=5, ipadx=3, padx="0 2")
        
        self.champs_list = [self.nom, self.prenom, self.contact, self.adresse, self.referent]

        self.menu()

    def enregistrer(self):
        all_is_valide = verify(self.champs_list)
        if all_is_valide:
            date_time = tm.strftime("%d/%m/%Y %H:%M:%S")
            
            liste = [self.nom.get().strip().upper(), self.prenom.get().strip().title(), self.contact.get().strip(), self.adresse.get().strip().title(), self.referent.get().strip(), date_time]
            values = tuple(liste)
            self.mydb.setPatient(values)
            
            patient = self.mydb.getOne("patient", "date", date_time)
            values = (patient[0], date_time, 1)
            self.mydb.setCompte(values)
            
            compte = self.mydb.getOne("compte", "date", date_time)
            [e.delete(0, "end") for e in self.champs_list]
            self.continuer(compte[0])

    def continuer(self, compte=None):
        idt = self.compte_id.get().strip() if not compte else compte
        if not idt or not str(idt).isdigit() or not self.mydb.getOneById("compte", idt):
            self.compte_id.config(bg="red")
            self.master.bell()
        else:
            cmpt = self.mydb.getOneById("compte", idt)
            self.compte_id.config(bg="#fff")
            self.compte_id.delete(0, "end")
            SelectService(compte=cmpt[1])

    def menu(self):
        principale = tk.Menu(self.master)
        
        ajouter = tk.Menu(principale, tearoff=0)
        ajouter.add_command(label="Nouveau Service", command=AddService)
        ajouter.add_command(label="Nouveau Medecin", command=NewMedecin)
        principale.add_cascade(label="Ajouter", menu=ajouter, font="Arial 10 bold")
        
        lister = tk.Menu(principale, tearoff=0)
        lister.add_command(label="Patients", command=Lister)
        principale.add_cascade(label="Liste", menu=lister, font="Arial 10 bold")
        
        self.master["menu"] = principale





Index().mainloop()