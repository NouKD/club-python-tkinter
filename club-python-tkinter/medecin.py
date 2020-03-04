
from tkinter import *
from tkinter.ttk import Combobox
from database import *


def new_medecin():

    mydb = DataBase()
    services = mydb.getAll("service")
    services_liste = [service[1] for service in services]

    def insert_db():
        cham = [e1, e2, e4, e5]
        validate = verify(cham)
        if not validate: return
        specialite = e3.get()
        liste = [item for item in services if specialite in item][0]
        service_id = liste[0]

        values = tuple([e1.get().strip().upper(), e2.get().strip().title(), service_id, e4.get().strip(), e5.get().strip()])
        mydb.setMedecin(values)
        [e.delete(0, "end") for e in cham]


    master = Tk()
    master.title("Enregistrement Medecin")
    master.geometry("392x312")
    master.resizable(0,0)

    nom_medecin = Label(master, text="Enregistrer un medecin")
    nom_medecin.grid(row=0, column=0, columnspan=2,
                    sticky="ew", ipadx=5, ipady=5, pady="3 2")

    nom = Label(master, text="Nom", anchor="w")
    nom.grid(row=1, column=0, sticky="ew", ipadx=5,
            ipady=5, padx=10, pady="3 2")

    prenom = Label(master, text="Prenom: ", anchor="w")
    prenom.grid(row=2, column=0, sticky="ew", ipadx=5,
                ipady=5, padx=10, pady="3 2")

    specialite = Label(master, text="Spécialité: ", anchor="w")
    specialite.grid(row=3, column=0, sticky="ew", ipadx=5,
                    ipady=5, padx=10, pady="3 2")

    adresse = Label(master, text="Adresse: ", anchor="w")
    adresse.grid(row=4, column=0, sticky="ew", ipadx=5,
                ipady=5, padx=10, pady="3 2")

    contact = Label(master, text="Contact: ", anchor="w")
    contact.grid(row=5, column=0, sticky="ew", ipadx=5,
                ipady=5, padx=10, pady="3 2")

    sbmitbtn = Button(master, text="soumettre", activebackground="pink",
                    activeforeground="blue", command=insert_db)
    sbmitbtn.grid(row=6, column=0, columnspan=2, ipadx=5, ipady=5, pady="3 2")

    # -------création de saisir---------
    e3 = StringVar()
    e1 = Entry(master, font="Arial 16")
    e1.grid(row=1, column=1, sticky="ew", ipadx=5, ipady=5, pady="3 2", padx="0 10")
    e2 = Entry(master, font="Arial 16")
    e2.grid(row=2, column=1, sticky="ew", ipadx=5, ipady=5, pady="3 2", padx="0 10")

    cb = Combobox(master, justify="center", textvariable=e3, state="readonly", font="Arial 16", values=services_liste)
    cb.grid(row=3, column=1, sticky="ew", ipadx=5, ipady=5, pady="3 2", padx="0 10")
    e3.set(services_liste[0])

    e4 = Entry(master, font="Arial 16")
    e4.grid(row=4, column=1, sticky="ew", ipadx=5, ipady=5, pady="3 2", padx="0 10")
    e5 = Entry(master, font="Arial 16")
    e5.grid(row=5, column=1, sticky="ew", ipadx=5, ipady=5, pady="3 2", padx="0 10")

    master.mainloop()
