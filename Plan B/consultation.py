#! /usr/bin/env python3
# coding: utf-8

import tkinter as tk
import time as tm
#----------------------|
from database import DataBase, verify
from examen import Examen

FONT = "Arial 14 bold"


class Consultation(tk.Toplevel):
    def __init__(self, compte=None, medecin=None):
        tk.Toplevel.__init__(self)
        x, y = int((self.winfo_screenwidth()/2)-279.5), int((self.winfo_screenheight()/2)-152.5)
        self.geometry("559x305+{0}+{1}".format(x, y))
        self.resizable(0,0)
        self.title("* Consultation *")
        
        self.mydb = DataBase()
        
        self.compte = compte
        self.medecin = medecin
        
        frame = tk.Frame(self)
        frame.pack(expand=1, fill="both", padx=5, pady=5)

        frame_left = tk.Frame(frame)
        frame_left.pack(expand=1, fill="y", side="left", padx=5, pady=5, ipadx=5)
        frame_right = tk.Frame(frame)
        frame_right.pack(expand=1, fill="y", side="right", padx=5, pady=5, ipadx=5)
        
        lb = tk.Label(frame_left, text="Taille", font=FONT, bg="#fff", fg="grey")
        lb.pack(expand=1, fill="x", ipadx=5, ipady=5)
        self.var_taille = tk.StringVar()
        self.champ_taille = tk.Entry(frame_left, font=FONT, justify="center", relief="flat", textvariable=self.var_taille, bg="#eee")
        self.champ_taille.pack(expand=1, fill="x", ipadx=5, ipady=5)

        lb = tk.Label(frame_left, text="Temperature", font=FONT, bg="#fff", fg="grey")
        lb.pack(expand=1, fill="x", ipadx=5, ipady=5, pady="5 0")
        self.var_temp = tk.StringVar()
        self.champ_temp = tk.Entry(frame_left, font=FONT, justify="center", relief="flat", textvariable=self.var_temp, bg="#eee")
        self.champ_temp.pack(expand=1, fill="x", ipadx=5, ipady=5)

        lb = tk.Label(frame_left, text="Group sanguin", font=FONT, bg="#fff", fg="grey")
        lb.pack(expand=1, fill="x", ipadx=5, ipady=5, pady="5 0")
        self.var_grpsang = tk.StringVar()
        self.champ_grpsang = tk.Entry(frame_left, font=FONT, justify="center", relief="flat", textvariable=self.var_grpsang, bg="#eee")
        self.champ_grpsang.pack(expand=1, fill="x", ipadx=5, ipady=5)

        lb = tk.Label(frame_right, text="Diagnostique", font=FONT, bg="#fff", fg="grey")
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
        all_is_valide = verify(self.champs_list)
        if all_is_valide:
            date_time = tm.strftime("%d/%m/%Y %H:%M:%S")

            values = tuple([self.compte, self.medecin, date_time] + [value.get().strip().upper() for value in self.champs_list] + [self.champ_diagn.get(index1="1.0", index2="end")])
            self.mydb.setConsultation(values)
            info = self.mydb.getOne("consultation", "date", date_time)
 
            Examen(consultation=info[0], date=date_time, destroyThis=self)




        
if __name__ == "__main__":
    Consultation().mainloop()