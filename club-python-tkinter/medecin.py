from tkinter import *  
from database import *
from tkinter.messagebox import *
import sys, time
mydb = DataBase()
def insert_db():
  date = time.strftime("%d-%m-%y  %H:%M")
  cham = [e1.get(), e2.get(), e3.get(), e4.get(), e5.get()]
  values = tuple(cham + [date])

  for i in cham:
    if not i.strip():
      print("veuillez remplir les champs")
    elif i.strip().isdigit():
      print("veuillez ecrire votre nom")
    else:
      validation = True
    if validation == True:
      try:
        mydb.setMedecin(values)
        print("bien enregistré")
      except Exception as e:
        print(e)
                      
def callback():
    if askyesno('Enregistrement', 'Êtes-vous sûr de vouloir faire ça?'):
        showinfo('..')
    else:
        showinfo('Annuler', 'enregistrement annulé')
  
fen1 = Tk()  
fen1.title("Enregistrement Medecin")
  
fen1.geometry("1700x600")  


#------création label---------  
nom_medecin = Label(fen1, text = "Enregistrer un medecin").place(x = 590, y = 10)
nom = Label(fen1, text = "Nom").place(x = 500, y = 60)    
prenom = Label(fen1, text = "Prenom").place(x = 500, y = 100)    
specialité = Label(fen1, text = "Spécialité").place(x = 500, y = 140) 
adresse = Label(fen1, text = "Adresse").place(x = 500, y = 180)
contact = Label(fen1, text = "Contact").place(x = 500, y = 220)  
sbmitbtn = Button(fen1, text = "soumettre",activebackground = "pink", activeforeground = "blue", command=insert_db).place(x = 630, y = 260)  
  
  #-------création de saisir---------
e1 = Entry(fen1)
e1.place(x = 600, y = 60)  
e2 = Entry(fen1)
e2.place(x = 600, y = 100)  
e3 = Entry(fen1)
e3.place(x = 600, y = 140) 
e4 = Entry(fen1)
e4.place(x = 600, y = 180) 
e5 = Entry(fen1)
e5.place(x = 600, y = 220) 
 
  
fen1.mainloop()  
