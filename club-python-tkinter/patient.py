from tkinter import *
import sys, time
from tkinter import ttk
from  database import DataBase

FONT = "Arial 14 bold"

class MyWindow:
    
    def __init__(self):
        
        self.root = Tk()
        self.root.title("gestion d'hopital")
        self.mydb = DataBase()

        self.root.geometry("957x450")
        self.root.resizable(0,0)
        
        #fonctions  liée a l'interaction avec la base de données
        #fonction d'insertion dans la base de données 
        # NB:  j'utilise la fonction d'Elysée setPatient(values) 
    def insert_db(self):
        
        date = time.strftime("%d-%m-%y  %H:%M")
        values = (self.entry_nom.get(), self.entry_prenom.get(), self.entry_age.get(), self.entry_contact.get(), self.entry_address.get(), self.entry_reference.get(), date)
        self.liste_entr = [self.entry_nom, self.entry_prenom, self.entry_age, self.entry_contact, self.entry_address, self.entry_reference]
        for i in values:
            if not i:   
                validate = False
            else:
                validate = True
        if type(values[2]) == 'str':
            validate = False
            
        if validate:
            try:
                self.mydb.setPatient(values)
                print("Bien enregistré")
                for i in self.liste_entr: i.delete("0", "end")
            except Exception as e:
                print(e)
        # fonction de recuperation de donnnées dans la base de données 
        # NB:  j'utilise les fonction d'Elysée getOneById(table, idt) 
    def fetch_id(self, *args):
        idt = self.entry_cree.get()
        try:
            if idt.isdigit:
                idt = int(idt)
                id_patient_existant = self.mydb.getOneById("patient", idt)
                self.label_id_var.set(f"Bienvenue {id_patient_existant[1] + id_patient_existant[2]} nous vous connectons a la base de données")
        except TypeError:
            self.label_id_var.set(("Cet id ne correspond à aucun patient veuillez vous inscrit si vous ne l'êtes pas"))


    #fonction service
    def change(self, *args):
        self.desc.config(text="")
        self.batiment.config(text="")
        self.combobox_service


    def services_desc(self):
        
        service_description = self.mydb.getAll("service")
        print(service_description)

        self.nos_service = Toplevel(self.root)
        self.nos_service.after(20000, lambda:print(self.nos_service.geometry()))
        self.nos_service.title("nos services")
        self.nos_service.geometry("357x279+973+50")
        self.nos_service.resizable(False, False)
        self.nos_service.config(relief="flat", bd=5, bg="#eee")
        self.frame_service = Frame(self.nos_service, relief="flat", bd=5, bg="#eee")
        self.frame_service.pack(pady=30)

        serv = Label(self.frame_service,text="service",bd=5, bg="powderblue", font=FONT,width=20)
        serv.pack()

        self.service_var = StringVar()
        self.combobox_service = ttk.Combobox(self.frame_service, textvariable=self.service_var)
        self.combobox_service.pack()
        self.combobox_service['values'] = [item[1] for item in service_description]
        self.service_var.trace("w", self.change)

        batiment = Label(self.frame_service,text="Batiment",bd=5, bg="powderblue", font=FONT)
        batiment.pack()

        self.batiment_var = StringVar()
        self.batiment = Label(self.frame_service,text="Batiment",bd=5, bg="powderblue", font=FONT, textvariable=self.batiment_var)
        self.batiment.pack()

        label_service = Label(self.frame_service,text="Description",bd=5, bg="powderblue", font=FONT,width=20)
        label_service.pack()

        self.desc = Label(self.frame_service)
        self.desc.pack()


        #self.menu
        self.menu = Menu(self.root)

        def quit():
            print("hello")
        #sous-self.menu

        #sous-menu patient
        self.patient = Menu(self.menu, tearoff=0)
        self.patient.add_command(label="Ajouter un nouveau patient")
        self.patient.add_command(label="Liste des patients")
        self.patient.add_command(label="Compte")
        self.menu.add_cascade(label="Patient",menu=self.patient)

        #self.menu self.patient
        
        self.service = Menu(self.menu, tearoff=0)
        self.service.add_command(label="services", command=self.services_desc)

        #self.menu self.service
        self.menu.add_cascade(label="service",menu=self.service)

        self.medecin = Menu(self.menu,tearoff=0)
        #self.menu self.medecin
        self.menu.add_command(label="medecin")

        self.examen = Menu(self.menu,tearoff=0)
        #self.menu examen
        self.menu.add_command(label="examen")


        self.consultation = Menu(self.menu,tearoff=0)
        #self.menu self.consultation
        self.menu.add_command(label="consultation")


        self.ordonnance = Menu(self.menu,tearoff=0)
        #self.menu self.ordonnance
        self.menu.add_command(label="ordonnance")

        self.medoc = Menu(self.menu, tearoff=0)
        #self.menu medoc
        self.menu.add_command(label="medoc")

        #frame principale
        self.frame_principale = Frame(self.root)
        self.frame_principale.pack(expand="YES")


        #formulaire d'accueil
        self.frame_home = Frame(self.frame_principale)
        self.frame_home.grid(row=0, pady=20, padx=20)

        #frame secondaire pour les patient ayant un compte
        self.frame_account = Frame(self.frame_principale, pady=10, width=200, height=200)
        self.frame_account.grid(row=0, column=1)

        label_nom =Label(self.frame_home,text="nom", font=FONT, relief="flat",bg="powderblue", fg="black")
        self.entry_nom= Entry(self.frame_home,  font=FONT, relief="flat", bd=5, bg="#eee", )


        label_prenom =Label(self.frame_home,text="prenom", font=FONT, relief="flat",bg="powderblue", fg="black")
        self.entry_prenom= Entry(self.frame_home,  font=FONT, relief="flat", bd=5, bg="#eee")

        label_age =Label(self.frame_home,text="age", font=FONT, relief="flat",bg="powderblue", fg="black")
        self.entry_age= Entry(self.frame_home,  font=FONT, relief="flat", bd=5, bg="#eee")


        label_contact =Label(self.frame_home,text="contact", font=FONT, relief="flat",bg="powderblue", fg="black")
        self.entry_contact= Entry(self.frame_home,  font=FONT, relief="flat", bd=5, bg="#eee")

        #address
        label_address =Label(self.frame_home,text="address", font=FONT, relief="flat",bg="powderblue", fg="black")
        self.entry_address= Entry(self.frame_home,  font=FONT, relief="flat", bd=5, bg="#eee")

        #reference
        label_reference =Label(self.frame_home,text="reference", font=FONT, relief="flat",bg="powderblue", fg="black")
        self.entry_reference= Entry(self.frame_home,  font=FONT, relief="flat", bd=5, bg="#eee")

        #envoyer
        envoyer_btn = Button(self.frame_home, text="Envoyer",  font=FONT, relief="flat", bd=5, bg="#eee", command=self.insert_db)

        #label_compte
        label_compte =Label(self.frame_account,text="Déjà un compte?  Entrez votre id", fg="#000", font=('', 14))


        #button

        #button_id
        self.entry_cree =Entry(self.frame_account, text="compte", font=FONT, relief="flat",bg="#eee", fg="black")
        self.label_id_var = StringVar()
        self.label_id_var.trace("w", self.fetch_id)
        label_id = Label(self.frame_account, textvariable = self.label_id_var , fg="#000", font=('', 14), wraplength=200)
        #print(label_id.config())
        button_ok =Button(self.frame_account, text="OK", command = self.fetch_id ,font=FONT, relief="flat", bd=5, bg="#eee", width=10)


        #affichage
        label_nom.grid(row=0, column=0, sticky="nsew", padx=10, pady=5)
        self.entry_nom.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)

        label_prenom.grid(row=0, column=1, sticky="nsew", padx=10, pady=5)
        self.entry_prenom.grid(row=1, column=1, sticky="nsew", padx=10, pady=5)

        label_age.grid(row=0, column=2, sticky="nsew", padx=10, pady=5)
        self.entry_age.grid(row=1, column=2, sticky="nsew", padx=10, pady=5)

        label_contact.grid(row=2, column=0, sticky="nsew", padx=10, pady=5)
        self.entry_contact.grid(row=3, column=0, sticky="nsew", padx=10, pady=5)

        label_address.grid(row=2, column=1, sticky="nsew", padx=10, pady=5)
        self.entry_address.grid(row=3, column=1, sticky="nsew", padx=10, pady=5)

        label_reference.grid(row=2, column=2, sticky="nsew", padx=10, pady=5)
        self.entry_reference.grid(row=3, column=2, sticky="nsew", padx=10, pady=5)

        envoyer_btn.grid(row=4, column=1,  sticky="nsew", padx=10, pady=5)

        label_compte.grid(row=0, column=1, sticky="nsew", padx=10, pady=5)


        self.entry_cree.grid(row=1, column=1, sticky="nsew", padx=10, pady=5)
        button_ok.grid(row=2, column=1, sticky="nsew", padx=10, pady=5)
        label_id.grid(row=3, column=1, sticky="nsew", padx=10, pady=5)

        self.root.config(menu=self.menu)
        self.root.mainloop()



myapp = MyWindow()
