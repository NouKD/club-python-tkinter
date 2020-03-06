#! /usr/bin/env python3
# coding: utf-8

from tkinter import *
import time as tm
from tkinter.ttk import Combobox
#----------------------|
from database import DataBase, verify
from examen import Examen

FONT = "Arial 14 bold"

class Consultation(Toplevel):
    def __init__(self, id_patient=None, id_medecin=None):
        Toplevel.__init__(self)
        x, y = int((self.winfo_screenwidth()/2)-279.5), int((self.winfo_screenheight()/2)-152.5)
        self.geometry("559x305+{0}+{1}".format(x, y))
        self.resizable(0,0)
        self.title("* Consultation *")
        
        self.mydb = DataBase()
        
        self.id_patient = id_patient
        self.id_medecin = id_medecin
        
        frame = Frame(self)
        frame.pack(expand=1, fill="both", padx=5, pady=5)

        frame_left = Frame(frame)
        frame_left.pack(expand=1, fill="y", side="left", padx=5, pady=5, ipadx=5)
        frame_right = Frame(frame)
        frame_right.pack(expand=1, fill="y", side="right", padx=5, pady=5, ipadx=5)
        
        lb = Label(frame_left, text="Taille", font=FONT, bg="#c7e0f7", fg="#05f")
        lb.pack(expand=1, fill="x", ipadx=5, ipady=5)
        self.var_taille = StringVar()
        self.champ_taille = Entry(frame_left, font=FONT, relief="sunken", textvariable=self.var_taille, bg="#eee")
        self.champ_taille.pack(expand=1, fill="x", ipadx=5, ipady=5)

        lb = Label(frame_left, text="Temperature", font=FONT, bg="#c7e0f7", fg="#05f")
        lb.pack(expand=1, fill="x", ipadx=5, ipady=5, pady="5 0")
        self.var_temp = StringVar()
        self.champ_temp = Spinbox(frame_left, font=FONT, relief="flat", textvariable=self.var_temp, bg="#eee",from_= 25 , to = 40)
        self.champ_temp.pack(expand=1, fill="x", ipadx=5, ipady=5)

        lb = Label(frame_left, text="Group sanguin", font=FONT, bg="#c7e0f7", fg="#05f")
        lb.pack(expand=1, fill="x", ipadx=5, ipady=5, pady="5 0")
        self.var_grpsang = StringVar()
        self.champ_grpsang = Combobox(frame_left, font=FONT, textvariable=self.var_grpsang, values =["A","A+","A-","B","B+","B-","AB","AB+","AB-","O","O+","O-"])
        self.champ_grpsang.pack(expand=1, fill="x", ipadx=5, ipady=5)

        lb = Label(frame_right, text="Diagnostique", font=FONT, bg="#c7e0f7", fg="#05f")
        lb.pack(expand=1, fill="x", ipadx=5, ipady=5)
        self.champ_diagn = Text(frame_right, font=FONT, relief="sunken", bd=5, height=9, bg="#eee")
        self.champ_diagn.pack(expand=1, fill="both")

        btn_frame = Frame(self)
        btn_frame.pack(expand=1, fill="both", padx=5, pady="0 5")
        
        btn1 = Button(btn_frame, text="Annuler", font=FONT, relief="sunken", command=self.destroy)
        btn1.pack(expand=1, padx=5, ipadx=5, ipady=5, side="left")
        btn2 = Button(btn_frame, text="Continuer", font=FONT, relief="sunken", command=self.continuer)
        btn2.pack(expand=1, padx=5, ipadx=5, ipady=5, side="right")

        self.champs_list = [self.champ_taille, self.champ_temp, self.champ_grpsang]

    def continuer(self):
        all_is_valide = verify(self.champs_list) 
        if all_is_valide:
            date_time = tm.strftime("%d/%m/%Y %H:%M:%S")

            values = tuple([self.id_patient, self.id_medecin, date_time] + [value.get().strip() for value in self.champs_list] + [self.champ_diagn.get(index1="1.0", index2="end")])
            self.mydb.setConsultation(values)
            info = self.mydb.getOne("consultation", "date", date_time)
 
            Examen(consultation=info[0], date=date_time, destroyThis=self)


if __name__ == "__main__":
    Consultation().mainloop()