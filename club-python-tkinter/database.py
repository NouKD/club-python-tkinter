#                                RECOMMANDATIONS
# ________________________________________________________________________________________________________________
#  [IMPORTANT] Pardonnez modifier ce fichier avec précaution pour limiter les erreur dans le programme [IMPORTANT]                                            |
#  [IMPORTANT] Pour les propriétés setter le paramètre "values" doit être un tuple et l'ordre des différents champs doit être respecte [IMPORTANT]|
#  Certaines méthodes ne sont pas encore présente veuillez les ajouter si possible
#
#  Exemple:
#                  getAllService() --> qui va retourner la liste des services disponibles
#                  getMedecinBySpecialite(service_id) --> qui va retourner la liste des médecin dont l'id de la spécialité correspond a service_id
#                  getAllPatient() --> qui va retourner la liste de touts les patient enregistre
# Et d'autre encore selon vos besoins
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------|


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
        fichierDonnees = "./database.sq3"
        self.connector = sq3.connect(fichierDonnees)
        self.cursor = self.connector.cursor()

        # Si [ la base de donnees existe deja une exception sera leve]
        try:
            self.cursor.execute(
                "CREATE TABLE patient(id INTEGER PRIMARY KEY AUTOINCREMENT, nom TEXT, prenom TEXT, age INTEGER, contact TEXT, adresse TEXT, referent TEXT, date TEXT)")
            self.connector.commit()
            self.cursor.execute(
                "CREATE TABLE compte(id INTEGER PRIMARY KEY AUTOINCREMENT, patient_id INTEGER, date TEXT, actif INTEGER)")
            self.connector.commit()
            self.cursor.execute(
                "CREATE TABLE service(id INTEGER PRIMARY KEY AUTOINCREMENT, nom TEXT, description TEXT, batiment TEXT)")
            self.connector.commit()
            self.cursor.execute(
                "CREATE TABLE medecin(id INTEGER PRIMARY KEY AUTOINCREMENT, nom TEXT, prenom TEXT, specialite_id INTEGER, adresse TEXT, contact TEXT)")
            self.connector.commit()
            self.cursor.execute(
                "CREATE TABLE consultation(id INTEGER PRIMARY KEY AUTOINCREMENT, patient_id INTEGER, medecin_id INTEGER, date TEXT, taille REAL, temperature INTEGER, group_sang TEXT, diagnostic TEXT)")
            self.connector.commit()
            self.cursor.execute(
                "CREATE TABLE examen(id INTEGER PRIMARY KEY AUTOINCREMENT, consultation_id INTEGER, resultat TEXT, type TEXT, date TEXT)")
            self.connector.commit()
            self.cursor.execute(
                "CREATE TABLE ordonance(id INTEGER PRIMARY KEY AUTOINCREMENT, consultation_id INTEGER, content TEXT, date TEXT)")
            self.connector.commit()
        except sq3.OperationalError:
            pass
        # Si non [La base de donnee n'existe pas donc elle est creer et les differents champs aussi]
        else:
            # Par consequent on enregistre certaines valeur par defaut utile
            self.default()

    def default(self):
        values = ("Generalite", "S'occupe des cas generaux sans specificite", "Batiment A")
        self.setService(values)
        values = ("Pediatrie", "La Pediatrie est la partie de la medecine qui concerne les enfants", "Batiment C")
        self.setService(values)
        values = ("Cancerologie", "Etude du cancer, de son diagnostic et de son traitement", "Batiment B")
        self.setService(values)
        values = ("Cardiologie", "Etude de la structure, fonctions et desordes du coeur", "Batiment D")
        self.setService(values)

    def setPatient(self, values):
        self.cursor.execute(
            "INSERT INTO patient(nom, prenom, age, contact, adresse, referent, date) VALUES(?,?,?,?,?,?,?)", values)
        self.connector.commit()

    def setCompte(self, values):
        self.cursor.execute(
            "INSERT INTO compte(patient_id, date, actif) VALUES(?,?,?)", values)
        self.connector.commit()

    def setService(self, values):
        self.cursor.execute(
            "INSERT INTO service(nom, description, batiment) VALUES(?,?,?)", values)
        self.connector.commit()

    def setMedecin(self, values):
        self.cursor.execute(
            "INSERT INTO medecin(nom, prenom, specialite_id, adresse, contact) VALUES(?,?,?,?,?)", values)
        self.connector.commit()

    def setConsultation(self, values):
        query = "INSERT INTO consultation(patient_id, medecin_id, date, taille, temperature, group_sang, diagnostic) VALUES(?,?,?,?,?,?,?)"
        self.cursor.execute(query, values)
        self.connector.commit()

    def setExamen(self, values):
        self.cursor.execute(
            "INSERT INTO examen(consultation_id, resultat, type, date) VALUES(?,?,?,?)", values)
        self.connector.commit()

    def setOrdonance(self, values):
        self.cursor.execute(
            "INSERT INTO ordonance(consultation_id, content, date) VALUES(?,?,?)", values)
        self.connector.commit()

    def getOne(self, table, champ, valeur_champ):
        '''
        Le paramettre table doit etre parmit la liste :["patient", "compte", "medecin", "consultation", "examen", "ordonance"]
        champ ==> element de la recherche
        valeur_champ ==> l'element a quoi doit correspondre la recherche
        ex:
            patient_name = 1
            user = getOne("patient", "nom", patient_name)
            print(user)
            [Vas retourner le patient dont l'identifiant est egale a 1]
        '''
        query = "SELECT * FROM {0} WHERE {1}='{2}'".format(
            table, champ, valeur_champ)
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def getOneById(self, table, idt, champ="id"):
        query = "SELECT * FROM {0} WHERE {1}={2}".format(table, champ, idt)
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def getAll(self, table):
        query = "SELECT * FROM {0}".format(table)
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def updateService(self, bat, desc, nom):
        query = 'UPDATE service SET batiment="{0}", description="{1}" WHERE nom="{2}"'.format(bat, desc, nom)
        self.cursor.execute(query)
        self.connector.commit()

    def updateMedecin(self, addr, cont, id):
        query = 'UPDATE medecin SET adresse="{0}", contact="{1}" WHERE id={2}'.format(addr, cont, id)
        self.cursor.execute(query)
        self.connector.commit()

    def deleteService(self, nom):
        self.cursor.execute('DELETE FROM service WHERE nom="{}"'.format(nom,))
        self.connector.commit()

    def deleteMedecin(self, id):
        self.cursor.execute('DELETE FROM medecin WHERE id={}'.format(id,))
        self.connector.commit()

    def listPatients(self):
        query = 'SELECT p.nom, p.prenom, s.nom, m.nom, m.prenom, e.consultation_id, c.id, p.id FROM patient as p, medecin as m, examen as e, service as s, consultation as c WHERE c.patient_id=p.id AND e.consultation_id=c.id AND m.specialite_id=s.id AND c.medecin_id=s.id GROUP BY p.id  ORDER BY c.date'
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def listPatient(self):
        query = 'SELECT p.nom, p.prenom, s.nom, m.nom, m.prenom, c.date, e.id, c.id, p.id FROM patient as p, medecin as m, examen as e, service as s, consultation as c WHERE c.medecin_id=m.id AND c.patient_id=p.id AND e.consultation_id=c.id AND c.date=e.date AND m.specialite_id=s.id AND c.medecin_id=s.id GROUP BY c.date ORDER BY p.nom'
        self.cursor.execute(query)
        return self.cursor.fetchall()
