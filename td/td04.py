from ia01.utils import lecture_csv, est_complet
from ia01.metriques import valeurs_lim

# Exercice 1.1
data = lecture_csv("data/dep_48_filtre.csv")
data_ = []
for i in range(len(data)):
    if (data[i]["classe_consommation_energie"] != "N" ) & (data[i]["classe_estimation_ges"] != "N"):
        data_.append(data[i])
data = data_ # We keep only the data with known energy consumption and greenhouse gas emission
# print(len(data))

# Exercice 1.2
data_ = []
for i in range(len(data)):
    if int(data[i]["annee_construction"]) > 1:
        data_.append(data[i])
data = data_
# print(len(data))

# Exercice 1.6
surf_hab = []
for i in range(len(data)):
    surf_hab.append(float(data[i]["surface_habitable"]))
s_min, s_max = valeurs_lim(surf_hab)
# print(s_min, s_max)

data_ = []
for i in range(len(data)):
    if (float(data[i]["surface_habitable"]) >= s_min) & (float(data[i]["surface_habitable"]) <= s_max):
        data_.append(data[i])
data = data_
# print(len(data))

# Exercice 1.8
data_ = []
for i in range(len(data)):
    if est_complet(data[i]):
        data_.append(data[i])
data = data_
# print(len(data))

# Exercice 1.9
data_ = []
for i in range(len(data)):
    if (
        float(data[i]["surface_baies_orientees_nord"])
        + float(data[i]["surface_baies_orientees_est_ouest"])
        + float(data[i]["surface_baies_orientees_sud"])
        + float(data[i]["surface_planchers_hauts_deperditifs"])
        + float(data[i]["surface_planchers_bas_deperditifs"])
        + float(data[i]["surface_parois_verticales_opaques_deperditives"])
        > 0
    ):
        data_.append(data[i])
data = data_
# print(len(data))

# Exercice 1.10
data_ = []
for i in range(len(data)):
    if float(data[i]["consommation_energie"]) + float(data[i]["estimation_ges"]) > 0:
        data_.append(data[i])
data = data_
print(len(data))