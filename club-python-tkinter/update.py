#! /usr/bin/env python3
# coding: utf-8

import tkinter as tk
import tkinter.ttk as ttk
from database import DataBase, verify


FT = ('', 14, 'bold')


class ServiceUpdate(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.geometry("420x362")
        self.resizable(0, 0)
        self.title("Modification | Supression de service")

        self.mydb = DataBase()
        services = self.mydb.getAll("service")
        services_liste = [service[1] for service in services]

        self.info = tk.Label(self, text="", font="Arial 12 bold")
        self.info.pack(expand=1, fill="x", ipady=5, padx=10)

        self.var_service = tk.StringVar()
        self.cham_serv = ttk.Combobox(self, state="readonly", justify="center", textvariable=self.var_service, values=services_liste, font=FT)
        self.cham_serv.pack(expand=1, fill="both", padx=10, pady=5, ipady=5, ipadx=5)
        self.var_service.trace("w", self.change)

        lb1 = tk.Label(self, text="Batiment", anchor="center", font=FT, bg="#c7e0f7", fg="#05f")
        lb1.pack(expand=1, fill="both", padx=5, pady="5 0", ipady=5, ipadx=5)
        self.batiment = tk.Entry(self, font=FT, bg="#fff", fg="grey", justify="center")
        self.batiment.pack(expand=1, fill="both", padx=5, ipady=5, ipadx=5)

        lb = tk.Label(self, text="Description", font=FT, bg="#c7e0f7", fg="#05f")
        lb.pack(expand=1, fill="both", ipady=5, padx=5, pady="5 0")
        self.description = tk.Text(self, font=('', 12), relief="flat", height=5, bd=5, bg="#fff", fg="grey")
        self.description.pack(expand=1, fill="both", padx=5)

        cader_btn = tk.Frame(self, relief="solid")
        cader_btn.pack(expand=1, fill="x", padx=5, ipady=5, ipadx=20)

        btn1 = tk.Button(cader_btn, text="Suprimer", font=FT, fg="grey", relief="flat", command=self.suprimer)
        btn1.pack(expand=1, fill="both", side="left", padx=10, pady=5)

        btn2 = tk.Button(cader_btn, text="Enregistrer", font=FT, fg="grey", relief="flat", command=self.enregistrer)
        btn2.pack(expand=1, fill="both", side="right", padx=10, pady=5)

        if len(services_liste) < 1:
            btn1["state"] = "disabled"
            btn2["state"] = "disabled"
        else:
            self.var_service.set(services_liste[0])

    def change(self, *_):
        choix = self.var_service.get()
        data = self.mydb.getOne("service", "nom", choix)
        self.description.delete("1.0", "end")
        self.description.insert("1.0", data[2])
        self.batiment.delete(0, "end")
        self.batiment.insert(0, data[3])
        self.info.config(bg="lightgrey", fg="lightgrey", text="")

    def enregistrer(self):
        valide = True
        nom = self.var_service.get()
        bat = self.batiment.get().strip().title().replace('"', '')
        desc = self.description.get("1.0", "end").strip().capitalize().replace('"', '')
        if not bat:
            self.batiment["bg"] = "red"
            valide = False
        else:
            self.batiment["bg"] = "#fff"

        if not desc:
            self.description["bg"] = "red"
            valide = False
        else:
            self.description["bg"] = "#fff"
        if valide:
            self.mydb.updateService(bat, desc, nom)
            self.info.config(bg="#0f5", fg="#fff", text="Modification effectue")
        else:
            self.info.config(bg="red", fg="#fff", text="Veuillez remplire touts les champs")

    def suprimer(self):
        nom = self.var_service.get()
        self.mydb.deleteService(nom)
        self.destroy()





class MedecinUpdate(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.title("Modification/Supression de medecin")
        self.resizable(0, 0)
        self.mydb = DataBase()
        self.medecins = self.mydb.getAll("medecin")
        self.medLst = ["Docteur: {0} {1}".format(medecin[1], medecin[2]) for medecin in self.medecins]

        self.info = tk.Label(self, text="", font="Arial 12 bold")
        self.info.grid(row=0, column=0, columnspan=2, sticky="ew", ipady=5, padx=10)

        self.var_medecin = tk.StringVar()
        self.cham_medi = ttk.Combobox(self, justify="center", textvariable=self.var_medecin, state="readonly", font="Arial 16", values=self.medLst)
        self.cham_medi.grid(row=1, column=0, columnspan=2, sticky="ew", ipadx=5, ipady=5, padx=10)
        self.var_medecin.trace("w", self.change)

        lb1 = tk.Label(self, text="Adresse", anchor="center", font=FT, bg="#c7e0f7", fg="#05f")
        lb1.grid(row=2, column=0, sticky="ew", padx=10, pady="15 0", ipady=5, ipadx=5)
        self.adresse = tk.Entry(self, font=FT, relief="sunken", bg="#fff", fg="grey", justify="center")
        self.adresse.grid(row=3, column=0, sticky="ew", padx=10, ipady=5, ipadx=5)

        lb = tk.Label(self, text="Contact", font=FT, bg="#c7e0f7", fg="#05f")
        lb.grid(row=2, column=1, sticky="ew", ipady=5, padx=10, pady="5 0")
        self.contact = tk.Entry(self, font=FT, relief="sunken", bg="#fff", fg="grey", justify="center")
        self.contact.grid(row=3, column=1, sticky="ew", padx=10, pady="0 5", ipady=5, ipadx=5)

        btn1 = tk.Button(self, text="Suprimer", font=FT, fg="grey", relief="groove", command=self.suprimer)
        btn1.grid(row=4, column=0, padx=10, pady="5 15")

        btn2 = tk.Button(self, text="Enregistrer", font=FT, fg="grey", relief="groove", command=self.enregistrer)
        btn2.grid(row=4, column=1, padx=10, pady="5 15")


        if len(self.medLst) < 1:
            btn1["state"] = "disabled"
            btn2["state"] = "disabled"
        else:
            self.var_medecin.set(self.medLst[0])


    def change(self, *_):
        med = self.medecins[self.medLst.index(self.var_medecin.get())]
        self.adresse.delete(0, "end")
        self.adresse.insert(0, med[-2])
        self.contact.delete(0, "end")
        self.contact.insert(0, med[-1])
        self.info.config(bg="lightgrey", fg="lightgrey", text="")


    def suprimer(self):
        id = self.medecins[self.medLst.index(self.var_medecin.get())][0]
        self.mydb.deleteMedecin(id)
        self.destroy()


    def enregistrer(self):
        id = self.medecins[self.medLst.index(self.var_medecin.get())][0]
        is_valide = verify([self.adresse, self.contact])
        if is_valide:
            self.mydb.updateMedecin(
                self.adresse.get().strip().replace('"', ''),
                self.contact.get().strip().replace('"', ''),
                id
                )
            self.info.config(bg="#0f5", fg="#fff", text="Modification effectue")
            self.medecins = self.mydb.getAll("medecin")
            self.medLst = ["Docteur: {0} {1}".format(medecin[1], medecin[2]) for medecin in self.medecins]
        else:
            self.info.config(bg="red", fg="#fff", text="Veuillez remplire touts les champs")



















if __name__ == "__main__":
    ServiceUpdate().mainloop()
    MedecinUpdate().mainloop()
