import pandas as pd
import numpy as np

# Définir le nombre de patients à simuler
nombre_patients = 500

# Générer des données aléatoires pour les patients
np.random.seed(42)
age = np.random.randint(18, 90, size=nombre_patients)  # Âge des patients entre 18 et 90 ans
sexe = np.random.choice(['Homme', 'Femme'], size=nombre_patients)  # Sexe des patients
symptomes = np.random.choice(['Fièvre', 'Toux', 'Douleur', 'Fatigue', 'Nausée'], size=nombre_patients)

# Données avant l'utilisation de l'IA
precision_avant_ia = np.random.normal(70, 10, size=nombre_patients)  # Précision moyenne de 70% avec écart-type de 10
temps_diagnostic_avant_ia = np.random.normal(30, 5, size=nombre_patients)  # Temps moyen de 30 minutes
complications_avant_ia = np.random.normal(20, 5, size=nombre_patients)  # Taux de complications à 20%

# Données après l'utilisation de l'IA
precision_apres_ia = np.clip(precision_avant_ia + np.random.normal(10, 5, size=nombre_patients), 0, 100)
temps_diagnostic_apres_ia = np.clip(temps_diagnostic_avant_ia - np.random.normal(10, 3, size=nombre_patients), 5, None)
complications_apres_ia = np.clip(complications_avant_ia - np.random.normal(5, 2, size=nombre_patients), 0, 100)

# Créer un DataFrame pandas avec toutes les données
df = pd.DataFrame({
    'Age': age,
    'Sexe': sexe,
    'Symptômes': symptomes,
    'Précision Avant IA': precision_avant_ia,
    'Temps Diagnostic Avant IA': temps_diagnostic_avant_ia,
    'Complications Avant IA': complications_avant_ia,
    'Précision Après IA': precision_apres_ia,
    'Temps Diagnostic Après IA': temps_diagnostic_apres_ia,
    'Complications Après IA': complications_apres_ia
})

# Enregistrer les données simulées dans un fichier CSV
df.to_csv('donnees_sante_simulees.csv', index=False)

print('Données simulées enregistrées dans donnees_sante_simulees.csv')
