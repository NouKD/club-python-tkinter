#! /usr/bin/env python3
# coding: utf-8

import tkinter as tk
import time as tm
#----------------------|
from database import DataBase


FONT = "Arial 14 bold"


class Examen(tk.Toplevel):
    def __init__(self, id_consultation=None):
        tk.Toplevel.__init__(self)
        x, y = int((self.winfo_screenwidth()/2)-279.5), int((self.winfo_screenheight()/2)-152.5)
        self.geometry("559x305+{0}+{1}".format(x, y))
        self.resizable(0,0)
        self.title("* Examen *")
        
        self.mydb = DataBase()
        
        self.id_consultation = id_consultation
        
        
        frame = tk.Frame(self)
        frame.pack(expand=1, fill="both", padx=5, pady=5)

        frame_left = tk.Frame(frame)
        frame_left.pack(expand=1, fill="y", side="left", padx=5, pady=5, ipadx=5)
        frame_right = tk.Frame(frame)
        frame_right.pack(expand=1, fill="y", side="right", padx=5, pady=5, ipadx=5)
        
        lb = tk.Label(frame_left, text="Type", font=FONT, bg="#fff", fg="gray75")
        lb.pack(expand=1, fill="x", ipadx=5, ipady=5)
        self.var_type = tk.StringVar()
        self.champ_type = tk.Entry(frame_left, font=FONT, relief="flat", textvariable=self.var_type, bg="#eee")
        self.champ_type.pack(expand=1, fill="x")

        

        lb = tk.Label(frame_right, text="Resultat", font=FONT, bg="#fff", fg="gray75")
        lb.pack(expand=1, fill="x", ipadx=5, ipady=5)
        self.champ_resul = tk.Text(frame_right, font=FONT, relief="flat", bd=5, height=9, bg="#eee")
        self.champ_resul.pack(expand=1, fill="both")
        
        btn_frame = tk.Frame(self)
        btn_frame.pack(expand=1, fill="both", padx=5, pady="0 5")
        
        btn1 = tk.Button(btn_frame, text="Annuler", font=FONT, relief="flat", command=self.destroy)
        btn1.pack(expand=1, padx=5, ipadx=5, ipady=5, side="left")
        btn2 = tk.Button(btn_frame, text="Continuer", font=FONT, relief="flat", command=self.continuer)
        btn2.pack(expand=1, padx=5, ipadx=5, ipady=5, side="right")

        self.champs_list = [self.champ_type]

    def continuer(self):
        all_is_valide = True
        for e in self.champs_list:
            if len(e.get().strip()) < 1:
                e.config(bg="red")
                all_is_valide = False
            else:
                e.config(bg="#eee")

        if all_is_valide:
            values = (
                    self.id_consultation, self.champ_type.get(),
                    self.champ_resul.get(index1="1.0", index2="end")
                )
            self.mydb.setExamen(values)
            info_examen = self.mydb.getOne("partient","id", patient_id)
            print(type(info_examen), info_examen)
            #Examen(Examen=info_consulte[0], destroyThis=self)
            


if __name__ == "__main__":
    Examen().mainloop()