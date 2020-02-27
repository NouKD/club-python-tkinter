#                     RECOMMANDATIONS
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


class DataBase():
    def __init__(self):
        fichierDonnees = "database.sq3"
        self.connector = sq3.connect(fichierDonnees)
        self.cursor = self.connector.cursor()

        # Si [ la base de donnees existe deja une exception sera leve]
        try:
            self.cursor.execute("CREATE TABLE partient(id INTEGER PRIMARY KEY AUTOINCREMENT, nom TEXT, prenom TEXT, contact TEXT, adresse TEXT, referent TEXT)")
            self.connector.commit()
            self.cursor.execute("CREATE TABLE compte(id INTEGER PRIMARY KEY AUTOINCREMENT, patient_id INTEGER, date TEXT, actif INTEGER)")
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


    def setPartient(self, values):
        self.cursor.execute("INSERT INTO partient(nom, prenom, contact, adresse, referent) VALUES(?,?,?,?,?)", values)
        self.connector.commit()


    def setCompte(self, values):
        self.cursor.execute("INSERT INTO compte(patient_id, date, actif) VALUES(?,?,?)", values)
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


    def getOne(self, champ, by, indice):
        '''
        Le paramettre champ doit etre parmit la liste :["partient", "compte", "medecin", "consultation", "examen", "ordonance"]
        by ==> element de la recherche
        indice ==> l'element a quoi doit correspondre la recherche
        ex:
            patient_id = 1
            user = getOne("patient", "id", patient_id)
            print(user)
            [Vas retourner le patient dont l'identifiant est egale a 1]
        ''' 
        query = "SELECT * FROM {0} WHERE {1}='{2}'".format(champ, by, indice)
        self.cursor.execute(query)
        return self.cursor.fetchone()
