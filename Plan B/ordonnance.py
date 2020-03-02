#! /usr/bin/env python3
# coding: utf-8

import tkinter as tk
import time as tm
#----------------------|
from database import DataBase


FONT = "Arial 14 bold"


class Ordonnance(tk.Toplevel):
    def __init__(self, consultation=0, destroyThis=None):
        tk.Toplevel.__init__(self)
        x, y = int((self.winfo_screenwidth()/2)-291), int((self.winfo_screenheight()/2)-145)
        self.geometry("582x290+{0}+{1}".format(x, y))
        self.minsize(300, 290)
        self.title("* Ordonnance *")

        if destroyThis: destroyThis.destroy()
        
        self.mydb = DataBase()
        
        self.consultation = consultation


        lb = tk.Label(self, text="Prescriptions", font=FONT, bg="#eee", fg="#222")
        lb.pack(expand=1, fill="x", ipady=10, padx=10)
        self.prescription = tk.Text(self, font="Arial 14 normal", relief="flat", bd=5, height=8, bg="#fff")
        self.prescription.pack(expand=1, fill="both", padx=10, pady="0 10")


        btn2 = tk.Button(self, text="Terminer", font=FONT, relief="flat", command=self.terminer)
        btn2.pack(expand=1, ipadx=25, ipady=5, pady="0 10")


    def terminer(self):
        content = self.prescription.get("1.0", "end").strip()
        date = tm.strftime("%d/%m/%Y %H:%M:%S")
        values = (self.consultation, content, date)
        self.mydb.setOrdonance(values)
        
        self.destroy()





if __name__ == "__main__":
    Ordonnance().mainloop()