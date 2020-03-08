#! /usr/bin/env python3
# coding: utf-8

import tkinter as tk
import time as tm
#----------------------|
from database import DataBase
from ordonnance import Ordonnance

FONT = "Arial 14 bold"


class Examen(tk.Toplevel):
    def __init__(self, consultation=None, date=tm.strftime("%d/%m/%Y %H:%M:%S"), destroyThis=None):
        tk.Toplevel.__init__(self)
        x, y = int((self.winfo_screenwidth()/2)-246), int((self.winfo_screenheight()/2)-205)
        self.geometry("492x410+{0}+{1}".format(x, y))
        self.minsize(492, 410)
        self.title("* Examen *")

        if destroyThis: destroyThis.destroy()
        self.date = date
        self.mydb = DataBase()
        
        self.consultation = consultation

        lb = tk.Label(self, text="Resultat de l'Examen", font=FONT, bg="#eee", fg="#222")
        lb.pack(expand=1, fill="x", ipady=10, padx=10)
        self.result = tk.Text(self, font="Arial 14 normal", relief="flat", bd=5, height=6, bg="#fff")
        self.result.pack(expand=1, fill="both", padx=10, pady="0 10")

        lb = tk.Label(self, text="Type d'Examen", font=FONT, bg="#eee", fg="#222")
        lb.pack(expand=1, fill="x", ipady=10, padx=10)
        self.type = tk.Text(self, font="Arial 14 normal", relief="flat", bd=5, height=4, bg="#fff")
        self.type.pack(expand=1, fill="both", padx=10, pady="0 10")

        btn2 = tk.Button(self, text="Continuer", font=FONT, relief="flat", command=self.continuer)
        btn2.pack(expand=1, ipadx=25, ipady=5, pady="0 10")

    def continuer(self):
        resultat = self.result.get("1.0", "end").strip().capitalize()
        exam_type = self.type.get("1.0", "end").strip().capitalize()
        values = [self.consultation, resultat, exam_type, self.date]
        
        self.mydb.setExamen(values)
        
        self.result.delete("1.0", "end")
        self.type.delete("1.0", "end")
        
        Ordonnance(self.consultation, self)


if __name__ == "__main__":
    Examen().mainloop()