#!/usr/bin/env python
# coding: utf-8

from tkinter import*
#importer la bd
from database import DataBase, verify

#cree une fenetre
fenetre = Tk()
#presolalise la fenetre 
fenetre.title("compte")
fenetre.geometry("1080x720")
fenetre.minsize(480,360)
#appel de la bd
mydb = DataBase()
fenetre.iconbitmap("python.ico")
fenetre.config(background='#bdebdf')

#creee la frame principal
fram= Frame(fenetre, bg='#bdebdf', bd=1, relief=SUNKEN)

#ajoute d'un fiste test
Label_title = Label (fram, text="numero_compte", font=("arial", 40),bg="#bdebdf", fg='#1b14f5')
Label_title.pack()
num_entry = Entry (fram, font=("arial", 25),bg="#bdebdf", fg='#1b14f5')
num_entry.pack()
#ajoute d'un second test

Label_subtitle = Label (fram, text="date de creation", font=("courrier", 30),bg="#bdebdf", fg='#1b14f5')
Label_subtitle.pack()
date_entry = Entry (fram, font=("arial", 25),bg="#bdebdf", fg='#1b14f5')
date_entry.pack()

#ajoute d'un trois test
Label_subtitle = Label (fram, text="id_patient", font=("courrier", 30),bg="#bdebdf", fg='#1b14f5')
Label_subtitle.pack()
date_entry = Entry (fram, font=("arial", 25),bg="#bdebdf", fg='#1b14f5')
date_entry.pack()

Label_subtitle = Label (fram, text="actif?", font=("courrier", 30),bg="#bdebdf", fg='#1b14f5')
Label_subtitle.pack()
var = IntVar()
Radiobutton(fram, variable=var, font="Arial 14 bold", anchor="w", text="oui", value=1).pack(expand=1, fill="both", padx=5, pady=5)
Radiobutton(fram, variable=var, font="Arial 14 bold", anchor="w", text="non", value=0).pack(expand=1, fill="both", padx=5, pady=5)

#ajoute un bouton
boutton = Button(fram, text="entre", font=("cursive",25), bg='white', fg='#ec062f')
boutton.pack(pady=25, fill=X)

#ajouter
fram.pack(expand=1, fill="both", padx=5, pady=5, ipadx=5, ipady=5)

#affichage de la fenetre
fenetre.mainloop()