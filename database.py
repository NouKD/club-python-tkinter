#                                RECOMMANDATIONS
#________________________________________________________________________________________________________________
#  [IMPORTANT] Pardonnez modifier ce fichier avec précaution pour limiter les erreur dans le programme [IMPORTANT]                                            |
#  [IMPORTANT] Pour les propriétés setter le paramètre "values" doit être un tuple et l'ordre des différents champs doit être respecte [IMPORTANT]|
#  Certaines méthodes ne sont pas encore présente veuillez les ajouter si possible
#
#  Exemple:
#                  getAllService() --> qui va retourner la liste des services disponibles
#                  getMedecinBySpecialite(service_id) --> qui va retourner la liste des médecin dont l'id de la spécialité correspond a service_id
#                  getAllPatient() --> qui va retourner la liste de touts les patient enregistre
# Et d'autre encore selon vos besoins
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|


#! /usr/bin/env python3
# coding: utf-8

import sqlite3 as sq3


def verify(liste):
    all_is_valide = True
    for e in liste:
        if len(e.get().strip()) < 1:
            e.config(bg="red")
            e.master.bell()
            all_is_valide = False
        else:
            e.config(bg="#fff")
    return all_is_valide


class DataBase():
    def __init__(self):
        fichierDonnees = "database.sq3"
        self.connector = sq3.connect(fichierDonnees)
        self.cursor = self.connector.cursor()

        # Si [ la base de donnees existe deja une exception sera leve]
        try:
            self.cursor.execute("CREATE TABLE patient(id INTEGER PRIMARY KEY AUTOINCREMENT, nom TEXT, prenom TEXT, contact TEXT, adresse TEXT, referent TEXT, date TEXT, service INTEGER)")
            self.connector.commit()
            self.cursor.execute("CREATE TABLE compte(id INTEGER PRIMARY KEY AUTOINCREMENT, numero_compte INTEGER, patient_id INTEGER, date TEXT, actif INTEGER)")
            self.connector.commit()
            self.cursor.execute("CREATE TABLE service(id INTEGER PRIMARY KEY AUTOINCREMENT, nom TEXT, description TEXT, batiment TEXT)")
            self.connector.commit()
            self.cursor.execute("CREATE TABLE medecin(id INTEGER PRIMARY KEY AUTOINCREMENT, nom TEXT, prenom TEXT, specialite_id INTEGER, adresse TEXT, contact TEXT)")
            self.connector.commit()
            self.cursor.execute("CREATE TABLE consultation(id INTEGER PRIMARY KEY AUTOINCREMENT, patient_id INTEGER, medecin_id INTEGER, date TEXT, taille REAL, temperature INTEGER, group_sang TEXT, diagnostic TEXT)")
            self.connector.commit()
            self.cursor.execute("CREATE TABLE examen(id INTEGER PRIMARY KEY AUTOINCREMENT, consultation_id INTEGER, resultat TEXT, type TEXT)")
            self.connector.commit()
            self.cursor.execute("CREATE TABLE ordonance(id INTEGER PRIMARY KEY AUTOINCREMENT, consultation_id INTEGER, content TEXT)")
            self.connector.commit()
        except sq3.OperationalError:
            pass
        # Si non [La base de donnee n'existe pas donc elle est creer et les differents champs aussi]
        else:
            # Par consequent on enregistre certaines valeur par defaut utile
            self.default()


    def default(self):
        values = ("Generaliste", "S'occupe des cas generaux sans specificite", "Batiment A")
        self.setService(values)


    def setPatient(self, values):
        self.cursor.execute("INSERT INTO patient(nom, prenom, contact, adresse, referent, date, service) VALUES(?,?,?,?,?,?,?)", values)
        self.connector.commit()


    def setCompte(self, values):
        self.cursor.execute("INSERT INTO compte(numero_compte, patient_id, date, actif) VALUES(?,?,?,?)", values)
        self.connector.commit()


    def setService(self, values):
        self.cursor.execute("INSERT INTO service(nom, description, batiment) VALUES(?,?,?)", values)
        self.connector.commit()


    def setMedecin(self, values):
        self.cursor.execute("INSERT INTO medecin(nom, prenom, specialite_id, adresse, contact) VALUES(?,?,?,?,?)", values)
        self.connector.commit()


    def setConsultation(self, values):
        query = "INSERT INTO consultation(patient_id, medecin_id, date, taille, temperature, group_sang, diagnostic) VALUES(?,?,?,?,?,?,?)"
        self.cursor.execute(query, values)
        self.connector.commit()


    def setExamen(self, values):
        self.cursor.execute("INSERT INTO examen(consultation_id, resultat, type) VALUES(?,?,?)", values)
        self.connector.commit()


    def setOrdonance(self, values):
        self.cursor.execute("INSERT INTO ordonance(consultation_id, content) VALUES(?,?)", values)
        self.connector.commit()


    def getOne(self, table, champ, indice):
        '''
        Le paramettre table doit etre parmit la liste :["patient", "compte", "medecin", "consultation", "examen", "ordonance"]
        champ ==> element de la recherche
        indice ==> l'element a quoi doit correspondre la recherche
        ex:
            patient_name = 1
            user = getOne("patient", "nom", patient_name)
            print(user)
            [Vas retourner le patient dont l'identifiant est egale a 1]
        ''' 
        query = "SELECT * FROM {0} WHERE {1}='{2}'".format(table, champ, indice)
        self.cursor.execute(query)
        return self.cursor.fetchone()


    def getOneById(self, table, idt):
        query = "SELECT * FROM {0} WHERE id={1}".format(table, idt)
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def getAll(self, table):
        query = "SELECT * FROM {0}".format(table)
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def updatePatientServiceId(self, service_id, patient_id):
        query = "UPDATE patient SET service={0} WHERE id={1}".format(service_id, patient_id)
        self.cursor.execute(query)
        self.connector.commit()