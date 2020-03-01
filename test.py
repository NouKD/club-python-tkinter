import sqlite3 as sq3


fichierDonnees = "database.sq3"
connector = sq3.connect(fichierDonnees)
cursor = connector.cursor()
cursor.execute("CREATE TABLE patient(id INTEGER PRIMARY KEY AUTOINCREMENT, nom TEXT, prenom TEXT, age INTEGER, contact TEXT, adresse TEXT, referent TEXT, date TEXT)")
connector.commit()
cursor.execute("CREATE TABLE compte(id INTEGER PRIMARY KEY AUTOINCREMENT, numero_compte INTEGER, patient_id INTEGER, date TEXT, actif INTEGER)")
connector.commit()
cursor.execute("CREATE TABLE service(id INTEGER PRIMARY KEY AUTOINCREMENT, nom TEXT, description TEXT, batiment TEXT)")
connector.commit()
cursor.execute("CREATE TABLE medecin(id INTEGER PRIMARY KEY AUTOINCREMENT, nom TEXT, prenom TEXT, specialite_id INTEGER, adresse TEXT, contact TEXT)")
connector.commit()
cursor.execute("CREATE TABLE consultation(id INTEGER PRIMARY KEY AUTOINCREMENT, patient_id INTEGER, medecin_id INTEGER, date TEXT, taille REAL, temperature INTEGER, group_sang TEXT, diagnostic TEXT)")
connector.commit()
cursor.execute("CREATE TABLE examen(id INTEGER PRIMARY KEY AUTOINCREMENT, consultation_id INTEGER, resultat TEXT, type TEXT)")
connector.commit()
cursor.execute("CREATE TABLE ordonance(id INTEGER PRIMARY KEY AUTOINCREMENT, consultation_id INTEGER, content TEXT)")
connector.commit()


# Si non [La base de donnee n'existe pas donc elle est creer et les differents champs aussi]
