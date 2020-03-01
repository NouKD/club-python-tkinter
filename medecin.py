from tkinter import *  
  
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
sbmitbtn = Button(fen1, text = "Submit",activebackground = "pink", activeforeground = "blue").place(x = 630, y = 260)  
  
  #-------création de saisir---------
e1 = Entry(fen1).place(x = 600, y = 60)     
e2 = Entry(fen1).place(x = 600, y = 100)    
e3 = Entry(fen1).place(x = 600, y = 140)  
e4 = Entry(fen1).place(x = 600, y = 180)  
e5 = Entry(fen1).place(x = 600, y = 220 )  
 
  
fen1.mainloop()  
