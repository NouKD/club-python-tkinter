#! /usr/bin/env python3
# coding: utf-8

from tkinter import *
import time
from tkinter import ttk

from database import DataBase, verify
from liste import Lister
from medecin import new_medecin, attribuerMedecin
from update import ServiceUpdate, MedecinUpdate
from password import Password


FONT = "Arial 14 bold"

class MyWindow:
    def __init__(self, dest=None):
        
        self.master = dest
        if self.master: self.master.iconify()

        self.root = Tk()
        self.root.title("Gestion d'Hopital")
        self.mydb = DataBase()

        self.root.geometry("1150x450")
        self.root.resizable(0, 0)
        self.services = self.mydb.getAll("service")

        self.frame_principale = Frame(self.root)
        self.frame_principale.pack(expand=1)

        self.info = Label(self.frame_principale, font="Arial 16 bold", fg="red", text="")
        self.info.grid(row=0, padx=20, ipadx=5, ipady=5)
        
        # formulaire d'accueil
        self.frame_home = Frame(self.frame_principale)
        self.frame_home.grid(row=1, pady=20, padx=20)

        # frame secondaire pour les patient ayant un compte
        self.frame_account = Frame(self.frame_principale, pady=10, width=200, height=200)
        self.frame_account.grid(row=1, column=1)

        label_nom = Label(self.frame_home, text="nom", font=FONT,
        relief="flat", bg="powderblue", fg="black")

        self.entry_nom = Entry(self.frame_home,font=FONT,
        relief="flat", bd=5, bg="#eee", )

        label_prenom = Label(self.frame_home, text="prenom",
        font=FONT, relief="flat", bg="powderblue", fg="black")

        self.entry_prenom = Entry(self.frame_home,  font=FONT, relief="flat", bd=5, bg="#eee")

        label_age = Label(self.frame_home, text="age", font=FONT, relief="flat", bg="powderblue", fg="black")
        self.entry_age = Entry(self.frame_home,  font=FONT, relief="flat", bd=5, bg="#eee")

        label_contact = Label(self.frame_home, text="contact", font=FONT, relief="flat", bg="powderblue", fg="black")
        self.entry_contact = Entry(self.frame_home,  font=FONT, relief="flat", bd=5, bg="#eee")

        # address
        label_address = Label(self.frame_home, text="address", font=FONT, relief="flat", bg="powderblue", fg="black")
        self.entry_address = Entry(self.frame_home,  font=FONT, relief="flat", bd=5, bg="#eee")

        # reference
        label_reference = Label(self.frame_home, text="En cas d'urgence", font=FONT, relief="flat", bg="powderblue", fg="black")
        self.entry_reference = Entry(self.frame_home,  font=FONT, relief="flat", bd=5, bg="#eee")

        # envoyer
        envoyer_btn = Button(self.frame_home, text="Envoyer",  font=FONT, relief="flat", bd=5, bg="#eee", command=self.insert_db)

        # label_compte
        label_compte = Label(self.frame_account, text="Déjà un compte?  Entrez votre id", fg="#000", font=('', 14))

        self.entry_cree = Entry(self.frame_account, text="compte", font=FONT, relief="flat", bg="#eee", fg="black")
        self.label_id_var = StringVar()
        self.label_id_var.trace("w", self.fetch_id)
        label_id = Label(self.frame_account, textvariable=self.label_id_var, fg="#000", font=('', 14), wraplength=200)

        button_ok = Button(self.frame_account, text="OK", command=self.fetch_id, font=FONT, relief="flat", bd=5, bg="#eee", width=10)
        recuv = Button(self.frame_account, relief="flat", text="Mot de passe oublie ?", font="Arial 9 bold", fg="#05f", command=Password)
        # affichage
        label_nom.grid(row=0, column=0, sticky="nsew", padx=10, pady=5)
        self.entry_nom.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)

        label_prenom.grid(row=0, column=1, sticky="nsew", padx=10, pady=5)
        self.entry_prenom.grid(row=1, column=1, sticky="nsew", padx=10, pady=5)

        label_age.grid(row=0, column=2, sticky="nsew", padx=10, pady=5)
        self.entry_age.grid(row=1, column=2, sticky="nsew", padx=10, pady=5)

        label_contact.grid(row=2, column=0, sticky="nsew", padx=10, pady=5)
        self.entry_contact.grid(
            row=3, column=0, sticky="nsew", padx=10, pady=5)

        label_address.grid(row=2, column=1, sticky="nsew", padx=10, pady=5)
        self.entry_address.grid(
            row=3, column=1, sticky="nsew", padx=10, pady=5)

        label_reference.grid(row=2, column=2, sticky="nsew", padx=10, pady=5)
        self.entry_reference.grid(
            row=3, column=2, sticky="nsew", padx=10, pady=5)

        envoyer_btn.grid(row=4, column=1,  sticky="nsew", padx=10, pady=5)

        label_compte.grid(row=0, column=1, sticky="nsew", padx=10, pady=5)

        self.entry_cree.grid(row=1, column=1, sticky="nsew", padx=10, pady=5)
        button_ok.grid(row=2, column=1, sticky="nsew", padx=10, pady=5)
        recuv.grid(row=4, column=1, ipadx=5, ipady=5)
        label_id.grid(row=3, column=1, sticky="nsew", padx=10, pady=5)

        self.menu()
        self.root.mainloop()

    def insert_db(self):
        date = time.strftime("%d/%m/%Y %H:%M:%S")
        
        self.liste_entr = [self.entry_nom, self.entry_prenom, self.entry_age, self.entry_contact, self.entry_address, self.entry_reference]
        validate = verify(self.liste_entr)
        if not self.entry_age.get().strip().isdigit():
            validate = False
            self.entry_age["bg"] = "red"
            self.root.after(2000, lambda col="#fff": self.entry_age.config(bg=col))

        if validate:
            idt = "med@{0}{1}{2}{3}".format(time.strftime("%H%M%Y%S"), self.entry_nom.get().strip()[0], time.strftime("%d%m"), self.entry_prenom.get()[0])
            
            values = [idt, 
                    self.entry_nom.get().strip().upper(), 
                    self.entry_prenom.get().strip().title(), 
                    self.entry_age.get().strip(),
                    self.entry_contact.get().strip(), 
                    self.entry_address.get().strip(), 
                    self.entry_reference.get().strip(),
                    date
            ]
            
            self.mydb.setPatient(tuple(values))
            for i in self.liste_entr:
                i.delete("0", "end")

            values = (idt, date, 1)
            self.mydb.setCompte(values)
            self.info.config(fg="green", text="Enregistrement effectue !")
            self.info.after(3000, lambda: self.info.config(text=""))
            self.services_desc(idt)
        else:
            self.info.config(fg="red", text="L'enregistrement a echoue !")
            self.info.after(3000, lambda: self.info.config(text=""))



    def fetch_id(self, *args):
        idt = self.entry_cree.get()
        id_patient_existant = self.mydb.getOne("patient", "id", idt)
        if not id_patient_existant:
            self.label_id_var.set("Erreur: Veuillez reverifiez votre identifiants !!!")
            self.entry_cree["bg"] = "red"
            self.root.after(2000, lambda col="#fff": self.entry_cree.config(bg=col))
        else:
            self.services_desc(idt)

    def change(self, *_):
        choix = self.service_var.get()
        liste = [item for item in self.services if choix in item][0]
        self.batiment["text"] = liste[3]
        self.desc["text"] = liste[2]

    def services_desc(self, cmpt):
        self.nos_service = Toplevel(self.root)
        self.nos_service.title("Service | id: {}".format(cmpt))
        x, y = int((self.root.winfo_screenwidth()/2) - 216), int((self.root.winfo_screenheight()/2)-127)
        self.nos_service.geometry("432x280+{0}+{1}".format(x, y))
        self.nos_service.config(relief="flat", bd=5, bg="#eee")
        self.frame_service = Frame(self.nos_service, relief="flat", bd=5, bg="#888")
        self.frame_service.pack(expand=1, fill="both", pady=10)

        FONT2 = "Arial 12 normal"

        serv = Label(self.frame_service, text="service", bg="powderblue", font=FONT, width=20)
        serv.pack(expand=1, fill="x", pady="15 0")

        self.service_var = StringVar()
        self.cham_serv = ttk.Combobox(self.frame_service, state="readonly", justify="center", textvariable=self.service_var, font=FONT2)
        self.cham_serv.pack(expand=1, fill="x")
        
        self.services = self.mydb.getAll("service")
        valeurs = [item[1] for item in self.services]
        self.cham_serv['values'] = valeurs
        self.service_var.trace("w", self.change)
        

        batiment = Label(self.frame_service, text="Batiment", bg="powderblue", font=FONT)
        batiment.pack(expand=1, fill="x", pady="15 0")

        self.batiment = Label(self.frame_service, text="", bg="#fff", font=FONT2)
        self.batiment.pack(expand=1, fill="x", ipady=3, ipadx=3)
        
        label_service = Label(self.frame_service, text="Description", bg="powderblue", font=FONT)
        label_service.pack(expand=1, fill="x", pady="15 0")
        
        self.desc = Label(self.frame_service, bg="#fff", font=FONT2)
        self.desc.pack(expand=1, fill="x", pady="0 5", ipady=3, ipadx=3)
        
        btn = Button(self.frame_service, text="Continuer", font=FONT, relief="flat", command=lambda a=cmpt, b=self.nos_service: self.continuer(cmpt, b))
        btn.pack(ipady=5, ipadx=5)
        self.service_var.set(valeurs[0])


    def continuer(self, comp, b):
        choix = self.service_var.get()
        self.services = self.mydb.getAll("service")
        liste = [item for item in self.services if choix in item][0]
        service = liste[0]
        attribuerMedecin(b, comp, service)


    def menu(self):
        # Menu principale
        principale = Menu(self.root)

        # Menu Ajouter
        menu_add = Menu(principale, tearoff=0)
        menu_add.add_command(label="Lister Patients", command=Lister)
        menu_add.add_command(label="Quitter", command=self.root.destroy)
        principale.add_cascade(label="Admin", menu=menu_add)

        # Menu Service
        menu_serv = Menu(principale, tearoff=0)
        menu_serv.add_command(label="Nouveau Service", command=AddService)
        menu_serv.add_command(label="Modifier | Suprimer", command=ServiceUpdate)
        principale.add_cascade(label="Service", menu=menu_serv)

        # Menu Medecin
        menu_mede = Menu(principale, tearoff=0)
        menu_mede.add_command(label="Nouveau Medecin", command=new_medecin)
        menu_mede.add_command(label="Modifier | Suprimer", command=MedecinUpdate)
        principale.add_cascade(label="Medecin", menu=menu_mede)

        self.root["menu"] = principale





class AddService(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.title("Service")
        x, y = int((self.winfo_screenwidth()/2)-275), int((self.winfo_screenheight()/2)-120)
        self.geometry("550x240+{0}+{1}".format(x, y))
        self.resizable(0,0)

        self.mydb = DataBase()

        frm1 = Frame(self)
        frm1.pack(expand=1, fill="both")

        frm2 = Frame(self)
        frm2.pack(expand=1, fill="both")

        cadre1 = Frame(frm1)
        cadre1.pack(expand=1, fill="both", side="left", padx="5 0", pady=5, ipadx=5, ipady=5)
        cadre2 = Frame(frm1)
        cadre2.pack(expand=1, fill="both", side="right", padx="0 5", pady=5, ipadx=5, ipady=5)

        lb1 = Label(cadre1, text="Nom: ",anchor="w", font=FONT, bg="#eee", fg="grey")
        lb1.pack(expand=1, fill="both", padx=5, pady="5 0", ipady=5, ipadx=5)
        self.nom = Entry(cadre1, font=FONT, bg="#fff", fg="#000")
        self.nom.pack(expand=1, fill="both", padx=5, ipady=5, ipadx=5)

        lb1 = Label(cadre1, text="Batiment: ",anchor="w", font=FONT, bg="#eee", fg="grey")
        lb1.pack(expand=1, fill="both", padx=5, pady="5 0", ipady=5, ipadx=5)
        self.batiment = Entry(cadre1, font=FONT, bg="#fff", fg="#000")
        self.batiment.pack(expand=1, fill="both", padx=5, ipady=5, ipadx=5)

        lb = Label(cadre2, text="Description:", font=FONT, bg="#eee", fg="grey")
        lb.pack(expand=1, fill="both", ipady=5, padx=5, pady="5 0")
        self.description = Text(cadre2, font=FONT, relief="flat", height=5, bd=5, bg="#fff")
        self.description.pack(expand=1, fill="both", padx=5)

        btn_cadre = Frame(frm2)
        btn_cadre.pack(expand=1, fill="both", ipadx=5, ipady=5)

        btn = Button(btn_cadre, text="Annuler", font=FONT, fg="grey", relief="flat", command=self.destroy)
        btn.pack(expand=1, fill="both", side="left", padx=15, pady=15)

        btn = Button(btn_cadre, text="Save", font=FONT, fg="grey", relief="flat", command=self.saveService)
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


if __name__ == "__main__":
    MyWindow()
