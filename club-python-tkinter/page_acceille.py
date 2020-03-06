#! /usr/bin/env python3
# coding: utf-8

from tkinter import*
#----------------------|
from liste import Lister
#----------------------|
from medecin import new_medecin
#----------------------|
from update import ServiceUpdate
#----------------------|
from database import DataBase

FONT = "Arial 14 bold"

fenetre = Tk()

fenetre.title("Acceille")

fenetre.geometry("1080x720")
fenetre.minsize(480,360)
#fenetre.iconbitmap("python.ico")
fenetre.config(background='#bdebdf')

Label_title = Label (fenetre, text="Bienvenu!", font=("arial", 77),bg="#bdebdf", fg='#1b14f5')
Label_title.pack(expand=1, pady=100)
fream = Frame (fenetre, bg='#bdebdf', bd=1, relief='flat')
boutton = Button(fream, text="liste de patient", font=("cursive",25), bg='white', fg='#c7e0f7', command=Lister)
boutton.pack(pady=25,side='left',padx=10, ipadx=5, ipady=5)
boutton = Button(fream, text="medecin", font=("cursive",25), bg='white', fg='#c7e0f7', command=new_medecin)
boutton.pack(pady=25,side='left',padx=10, ipadx=5, ipady=5)
boutton = Button(fream, text="service", font=("cursive",25), bg='white', fg='#c7e0f7', command=ServiceUpdate)
boutton.pack(pady=25,side='left',padx=10, ipadx=5, ipady=5)

fream.pack(expand=1, side='left',padx=5, pady=100, ipadx=5, ipady=5)


fenetre.mainloop(n=0)