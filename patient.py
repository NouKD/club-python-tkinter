from tkinter import *
import sys
from tkinter import ttk
from  database import DataBase


class MyWindow:
    
    def __init__(self):
        FONT = "Arial 14 bold"
        self.root = Tk()
        self.root.title("gestion d'hopital")
        

        self.root.geometry("1700x600")
        self.root.minsize(width=700, height=500)
        
        #fonction
        def insert_db():
            self.mydb = DataBase()
            values = (entry_nom.get(), entry_prenom.get(), entry_age.get(), entry_contact.get(), entry_address.get(), entry_reference.get())
            
            for i in values:
                if i== '':
                    print("Entry  couldn't be empty")   
                    validate = False
                else:
                    validate = True
            if type(values[2]) == 'str':
                print("Veuillez entrer un nombre svp")
                validate = False
            
            if validate == True:
                try:
                    print(dir(self.mydb.setPatient))
                except Exception as e:
                    print(e)
        
        
        #fonction service
        def services():
            def service_desc(*args):
                var_description.set(self.combobox_service.get())
                print(self.combobox_service.g )
            
            service_description = {
                "churigie": """ Technique medicale avec intervention physique sur les tissu """,

                "pediatrie":""" branche de la medecine ayant trait au soins des enfants """,

                "gynecologie":""" science du traitement des maladies des organes sexuel feminin et tractus genitale """,

                "neurochirugie": """ Discipline chirurgicale qui est specialisée dans la chirurgies du systeme nerveux central et du systeme nerveux peripherique    """,

                "cardiologie":""" Specialité medicale qui etudie le coeur et ses maladies    """,

                "dermatologie":""" Dermatologie est une specialite de medecine qui s'occupe de la peau, des muqueuses et des pharnères (ongles, cheveux, poils)    """

            }

                
                
            self.nos_service = Toplevel(self.root)
            self.nos_service.title("nos services")
            self.nos_service.geometry("1700x600")
            self.nos_service.config(relief="flat", bd=5, bg="#eee")
            self.frame_service = Frame(self.nos_service, relief="flat", bd=5, bg="#eee")
            self.frame_service.pack(pady=30)
            
            self.label_service = Label(self.frame_service,text="service",bd=5, bg="powderblue", font=FONT,width=20)
            self.label_service.grid(row=0, column=0, pady=5)
            
            self.combobox_service = ttk.Combobox(self.frame_service)
            self.combobox_service['values'] = service_description.keys()
            self.combobox_service.grid(row=1, column=0,pady=5)
            
            self.label_service = Label(self.frame_service,text="description",bd=5, bg="powderblue", font=FONT,width=20)
            self.label_service.grid(row=2, column=0,pady=5)
            
            var_description = StringVar()
            var_description.trace_add("write", service_desc)
            self.desc = Message(self.frame_service, textvariable=var_description)
            self.desc.grid(row=3, column=0,pady=5)
            
            
        #self.menu
        self.menu = Menu(self.root)
        
        def quit():
            print("hello")
        #sous-self.menu
        self.patient = Menu(self.menu, tearoff=0)
        self.patient.add_command(label="Ajouter un nouveau patient")
        self.patient.add_command(label="Liste des patients")
        self.patient.add_command(label="Compte")
        
        
        #self.menu self.patient
        self.menu.add_cascade(label="Patient",menu=self.patient)

        
        self.service = Menu(self.menu, tearoff=0)
        #self.menu self.service
        self.menu.add_command(label="service",  command=services)
        
        self.medecin = Menu(self.menu,tearoff=0)
        #self.menu self.medecin
        self.menu.add_command(label="medecin", )
        
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
        
        #nom
        nom = StringVar()
        label_nom =Label(self.frame_home,text="nom", font=FONT, relief="flat",bg="powderblue", fg="black")
        entry_nom= Entry(self.frame_home,  font=FONT, relief="flat", bd=5, bg="#eee", )
        
        #prenom
        label_prenom =Label(self.frame_home,text="prenom", font=FONT, relief="flat",bg="powderblue", fg="black")
        entry_prenom= Entry(self.frame_home,  font=FONT, relief="flat", bd=5, bg="#eee")
        
        #age
        label_age =Label(self.frame_home,text="age", font=FONT, relief="flat",bg="powderblue", fg="black")
        entry_age= Entry(self.frame_home,  font=FONT, relief="flat", bd=5, bg="#eee")
        
        #contact
        label_contact =Label(self.frame_home,text="contact", font=FONT, relief="flat",bg="powderblue", fg="black")
        entry_contact= Entry(self.frame_home,  font=FONT, relief="flat", bd=5, bg="#eee")
        
        #address
        label_address =Label(self.frame_home,text="address", font=FONT, relief="flat",bg="powderblue", fg="black")
        entry_address= Entry(self.frame_home,  font=FONT, relief="flat", bd=5, bg="#eee")
        
        #reference
        label_reference =Label(self.frame_home,text="reference", font=FONT, relief="flat",bg="powderblue", fg="black")
        entry_reference= Entry(self.frame_home,  font=FONT, relief="flat", bd=5, bg="#eee")
        
        #envoyer
        envoyer_btn = Button(self.frame_home, text="Envoyer",  font=FONT, relief="flat", bd=5, bg="#eee", command=insert_db)
        
        #label_compte
        label_compte =Label(self.frame_account,text="Déjà un compte?  Entrez votre id", fg="#000", font=('', 14))

        
        #button
        
        #button_cree
        entry_cree =Entry(self.frame_account, text="compte", font=FONT, relief="flat",bg="#eee", fg="black")
        button_ok =Button(self.frame_account, text="OK",font=FONT, relief="flat", bd=5, bg="#eee", width=10)
        
        
        
        
        
        
        
        #affichage 
        label_nom.grid(row=0, column=0, sticky="nsew", padx=10, pady=5)
        entry_nom.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)
        
        label_prenom.grid(row=0, column=1, sticky="nsew", padx=10, pady=5)
        entry_prenom.grid(row=1, column=1, sticky="nsew", padx=10, pady=5)
        
        label_age.grid(row=0, column=2, sticky="nsew", padx=10, pady=5)
        entry_age.grid(row=1, column=2, sticky="nsew", padx=10, pady=5)
        
        label_contact.grid(row=2, column=0, sticky="nsew", padx=10, pady=5)
        entry_contact.grid(row=3, column=0, sticky="nsew", padx=10, pady=5)
        
        label_address.grid(row=2, column=1, sticky="nsew", padx=10, pady=5)
        entry_address.grid(row=3, column=1, sticky="nsew", padx=10, pady=5)
        
        label_reference.grid(row=2, column=2, sticky="nsew", padx=10, pady=5)
        entry_reference.grid(row=3, column=2, sticky="nsew", padx=10, pady=5)
        
        envoyer_btn.grid(row=4, column=1,  sticky="nsew", padx=10, pady=5)
        
        label_compte.grid(row=0, column=1, sticky="nsew", padx=10, pady=5)


        entry_cree.grid(row=1, column=1, sticky="nsew", padx=10, pady=5)
        button_ok.grid(row=2, column=1, sticky="nsew", padx=10, pady=5)
        
        
        
        
        self.root.config(menu=self.menu)
        self.root.mainloop()
        
        

myapp = MyWindow()
