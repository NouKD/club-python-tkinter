#! /usr/bin/env python3
# coding: utf-8

from tkinter import *

from liste import Lister
from medecin import new_medecin
from continuer import AddService, MyWindow
from database import DataBase


class PageAcceuil(Tk):
    def __init__(self):
        Tk.__init__(self)

        FONT = "Arial 14 bold"

        self.title("* ACCEUILL *")
        self.attributes('-zoomed', 1)
        #self.attributes('-fullscreen', True)
        self.resizable(0,0)
        self.config(background='#bdebdf')

        txt = "Bienvenu au centre MedicoNanien !"

        img = PhotoImage(file="img.png", width=1000, height=300)

        Label_title = Label(self, text=txt, image=img, compound="bottom", bd=1, font="Arial 55 bold", bg="#aee0f3", fg='#fff', relief='sunken')
        Label_title.pack(expand=1, ipadx=10, ipady=10)


        continuer = Button(self, text="Commencer", font=FONT, bg='#0bc06c', fg='#fff', relief="flat", command=lambda a=self: MyWindow(a))
        continuer.pack(pady=" 10 20", ipadx=5, ipady=5)


        cadre = Frame(self, bg='#aee0f3', bd=1, relief='sunken')
        cadre.pack(expand=1, side='left', padx=5, ipadx=5, ipady=5)

        patient = Button(cadre, text="Patients", font=FONT, bg='#05f', fg='#fff', relief="flat", command=Lister)
        patient.pack(pady=25, side='left', padx=10, ipadx=5, ipady=5)

        add_medecin = Button(cadre, text="Ajouter Medecin", font=FONT, bg='#05f', fg='#fff', relief="flat", command=new_medecin)
        add_medecin.pack(pady=25, side='left', padx=10, ipadx=5, ipady=5)

        add_service = Button(cadre, text="Ajouter Service", font=FONT, bg='#05f', fg='#fff', relief="flat", command=AddService)
        add_service.pack(pady=25, side='left', padx=10, ipadx=5, ipady=5)

        self.mainloop(n=0)


if __name__ == "__main__":
    PageAcceuil()