#! /usr/bin/env python3
# coding: utf-8

import tkinter as tk
import time as tm
#----------------------|
from database import DataBase


FONT = "Arial 14 bold"

class Consultation(tk.Toplevel):
    def __init__(self, id_patient=None, id_medecin=None):
        tk.Toplevel.__init__(self)
        self.geometry("559x305")
        self.resizable(0,0)
        
        self.mydb = DataBase()
        
        self.id_patient = id_patient
        self.id_medecin = id_medecin
        
        frame = tk.Frame(self)
        frame.pack(expand=1, fill="both", padx=5, pady=5)

        frame_left = tk.Frame(frame)
        frame_left.pack(expand=1, fill="y", side="left", padx=5, pady=5, ipadx=5)
        frame_right = tk.Frame(frame)
        frame_right.pack(expand=1, fill="y", side="right", padx=5, pady=5, ipadx=5)
        
        lb = tk.Label(frame_left, text="Taille", font=FONT, bg="#fff", fg="gray75")
        lb.pack(expand=1, fill="x", ipadx=5, ipady=5)
        self.var_taille = tk.StringVar()
        self.champ_taille = tk.Entry(frame_left, font=FONT, relief="flat", textvariable=self.var_taille, bg="#eee")
        self.champ_taille.pack(expand=1, fill="x", ipadx=5, ipady=5)

        lb = tk.Label(frame_left, text="Temperature", font=FONT, bg="#fff", fg="gray75")
        lb.pack(expand=1, fill="x", ipadx=5, ipady=5, pady="5 0")
        self.var_temp = tk.StringVar()
        self.champ_temp = tk.Entry(frame_left, font=FONT, relief="flat", textvariable=self.var_temp, bg="#eee")
        self.champ_temp.pack(expand=1, fill="x", ipadx=5, ipady=5)

        lb = tk.Label(frame_left, text="Group sanguin", font=FONT, bg="#fff", fg="gray75")
        lb.pack(expand=1, fill="x", ipadx=5, ipady=5, pady="5 0")
        self.var_grpsang = tk.StringVar()
        self.champ_grpsang = tk.Entry(frame_left, font=FONT, relief="flat", textvariable=self.var_grpsang, bg="#eee")
        self.champ_grpsang.pack(expand=1, fill="x", ipadx=5, ipady=5)

        lb = tk.Label(frame_right, text="Diagnostique", font=FONT, bg="#fff", fg="gray75")
        lb.pack(expand=1, fill="x", ipadx=5, ipady=5)
        self.champ_diagn = tk.Text(frame_right, font=FONT, relief="flat", bd=5, height=9, bg="#eee")
        self.champ_diagn.pack(expand=1, fill="both")
        
        btn_frame = tk.Frame(self)
        btn_frame.pack(expand=1, fill="both", padx=5, pady="0 5")
        
        btn1 = tk.Button(btn_frame, text="Annuler", font=FONT, relief="flat", command=self.destroy)
        btn1.pack(expand=1, padx=5, ipadx=5, ipady=5, side="left")
        btn2 = tk.Button(btn_frame, text="Continuer", font=FONT, relief="flat", command=self.continuer)
        btn2.pack(expand=1, padx=5, ipadx=5, ipady=5, side="right")

        self.champs_list = [self.champ_taille, self.champ_temp, self.champ_grpsang]

    def continuer(self):
        all_is_valide = True
        for e in self.champs_list:
            if len(e.get().strip()) < 1:
                e.config(bg="red")
                all_is_valide = False
            else:
                e.config(bg="#eee")
            
        if all_is_valide:
            date_time = tm.strftime("%d/%m/%Y %H:%M:%S")
            values = (
                            self.id_patient, self.id_medecin, date_time, self.champ_taille.get(),
                            self.champ_temp.get(), self.champ_grpsang.get(),
                            self.champ_diagn.get(index1="1.0", index2="end")
                            )
            self.mydb.setConsultation(values)
            info_consulte = self.mydb.getConsultation(date_time=date_time)
            print(type(info_consulte), info_consulte)
            #Examen(consultation=info_consulte[0], destroyThis=self)
        
if __name__ == "__main__":
    Consultation().mainloop()