#! /usr/bin/env python3
# coding: utf-8

from tkinter.ttk import Combobox
import tkinter as tk
import time as tm
#----------------------|
from database import DataBase, verify
from consultation import Consultation


FONT = "Arial 14 bold"


class NewMedecin(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        x, y = int((self.winfo_screenwidth()/2)-183), int((self.winfo_screenheight()/2)-119)
        self.geometry("366x238+{0}+{1}".format(x, y))
        
        self.title("Ajouter Medecin")
        
        self.mydb = DataBase()
        self.services = self.mydb.getAll("service")
        services_liste = [service[1] for service in self.services]

        self.var_specialite = tk.StringVar()


        lb1 = tk.Label(self, text="Nom: ", anchor="w", font=FONT, fg="grey")
        lb1.grid(row=0, column=0, padx="15 20", pady=5, sticky="we")
        self.nom = tk.Entry(self, font=FONT, bg="#fff", fg="#000")
        self.nom.grid(row=0, column=1, padx="0 15", pady=5, sticky="we")


        lb1 = tk.Label(self, text="Prenom: ", anchor="w", font=FONT, fg="grey")
        lb1.grid(row=1, column=0, padx="15 20", pady=5, sticky="we")
        self.prenom = tk.Entry(self, font=FONT, bg="#fff", fg="#000")
        self.prenom.grid(row=1, column=1, padx="0 15", pady=5, sticky="we")


        lb1 = tk.Label(self, text="Specialite: ", anchor="w", font=FONT, fg="grey")
        lb1.grid(row=2, column=0, padx="15 20", pady=5, sticky="we")
        # Creation de liste deroulante
        selection = Combobox(self, justify="center", textvariable=self.var_specialite, state="readonly", font=FONT, values=services_liste)
        selection.grid(row=2, column=1, padx="0 15", pady=5, sticky="we")


        lb1 = tk.Label(self, text="Adresse: ", anchor="w", font=FONT, fg="grey")
        lb1.grid(row=3, column=0, padx="15 20", pady=5, sticky="we")
        self.adresse = tk.Entry(self, font=FONT, bg="#fff", fg="#000")
        self.adresse.grid(row=3, column=1, padx="0 15", pady=5, sticky="we")


        lb1 = tk.Label(self, text="Contact: ", anchor="w", font=FONT, fg="grey")
        lb1.grid(row=4, column=0, padx="15 20", pady=5, sticky="we")
        self.contact = tk.Entry(self, font=FONT, bg="#fff", fg="#000")
        self.contact.grid(row=4, column=1, padx="0 15", pady=5, sticky="we")

        btn = tk.Button(self, text="Continuer", font=FONT, fg="grey", relief="flat", command=self.enregistrer)
        btn.grid(row=5, column=0, columnspan=2, pady=10)
        
        self.var_specialite.set(services_liste[0])

        self.champs_list = [self.nom, self.prenom, self.adresse, self.contact]

    def enregistrer(self):
        specialite = self.var_specialite.get()
        liste = [item for item in self.services if specialite in item][0]
        service_id = liste[0]
        all_is_valide = verify(self.champs_list)
        if all_is_valide:
            values = [e for e in [self.nom.get().strip().upper(), self.prenom.get().strip().title(), service_id, self.adresse.get(), self.contact.get()]]
            [e.delete(0, "end") for e in self.champs_list]
            self.mydb.setMedecin(values)


def attribuerMedecin(destroyThis, compte, service):
    destroyThis.destroy()
    mydb = DataBase()
    medecin = mydb.getOneById("medecin", service, "specialite_id")
    Consultation(compte, medecin[0])





if __name__ == "__main__":
    NewMedecin().mainloop()