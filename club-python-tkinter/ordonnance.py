from tkinter import *
app =Tk()
app.geometry("1700x1000")
app.config(bg="#eee")
app.title("ordonnance")

frame1 = Frame(app,bg="#eee")
frame1.pack(pady=50)

# numero ordonnance
label1 = Label(frame1, text="n° de consultation", font="Arial 18 bold",bg="#fff",width=26)
label1.pack()

entry_nber = IntVar()
entry1 = Entry(frame1,textvariable=entry_nber, font="Arial 15 bold",bg="#eee", bd=2,width=30)
entry1.pack()


#médicaments
label2 = Label(frame1, text="Médicaments", font="Arial 18 bold",bg="#fff",width=26)
label2.pack()

entry_md = StringVar()
entry2 = Entry(frame1,textvariable=entry_md, font="Arial 15 bold",bg="#eee", bd=2,width=30)
entry2.pack()

#ordonnance
label3 = Label(frame1, text="ordonnance", font="Arial 18 bold",bg="#fff",width=26)
label3.pack()

entry_ord = StringVar()
entry3 = Entry(frame1,textvariable=entry_ord, font="Arial 15 bold",bg="#eee", bd=2,width=30)
entry3.pack()


button = Button(frame1,text="envoyer", font="Arial 15 bold",bg="#eee", bd=2,width=15)
button.pack()








app.mainloop()
