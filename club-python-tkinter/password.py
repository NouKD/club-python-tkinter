
import tkinter as tk

from database import DataBase, verify


FT = "Arial 14 bold"


class Password(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.geometry("248x280")
        self.resizable(0, 0)
        self.sizefrom(who="user")
        self.title("Mot de passe oublie")
        self.configure(background="#fff")
        self.mydb = DataBase()

        self.error = tk.Label(self, anchor="w", font="Arial 10 bold", fg="red", bg="#fff")
        self.error.pack(expand=1, fill="both", padx=10, pady="5 0", ipady=5, ipadx=5)

        lb1 = tk.Label(self, text="Nom", anchor="w", font=FT, bg="#c7e0f7", fg="#05f")
        lb1.pack(expand=1, fill="both", padx=10, pady="5 0", ipady=5, ipadx=5)
        self.nom = tk.Entry(self, font=FT, bg="#fff", fg="grey", justify="center")
        self.nom.pack(expand=1, fill="both", padx=10, ipady=5, ipadx=5)

        lb1 = tk.Label(self, text="Contact", anchor="w", font=FT, bg="#c7e0f7", fg="#05f")
        lb1.pack(expand=1, fill="both", padx=10, pady="5 0", ipady=5, ipadx=5)
        self.contact = tk.Entry(self, font=FT, bg="#fff", fg="grey", justify="center")
        self.contact.pack(expand=1, fill="both", padx=10, ipady=5, ipadx=5)

        self.info = tk.Label(self, font="Arial 12 bold", bg="#fff", fg="grey")
        self.info.pack(expand=1, fill="both", padx=10, pady=5, ipady=5, ipadx=5)
        self.info.bind("<1>", self.copy)
        
        btn = tk.Button(self, text="Rechercher", font=FT, bg="#c7e0f7", fg="#05f", relief="flat", command=self.search)
        btn.pack(expand=1, fill="both", side="right", padx=10, pady=5)

    def copy(self, _):
        self.master.clipboard_clear()
        self.master.clipboard_append(self.info["text"])
        self.master.bell()

    def search(self):
        valide = verify([self.nom, self.contact])
        if not valide:
            self.error.config(text="Touts les champs sont obligatoires")
            self.info["text"] = ""
        else:
            self.error.config(text="")
            result = self.mydb.recuva(self.nom.get().strip().upper(), self.contact.get().strip())
            if not result:
                self.info.config(fg="red", text="Aucune correspondance !")
            else:
                self.info.config(fg="green", text=result)


if __name__ == "__main__":
    Password().mainloop()