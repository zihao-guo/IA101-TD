from ia01.utils import lecture_csv

data = lecture_csv("data/dep_48_clean.csv")

# Exercice 2.1
y = []
for d in data:
    if d["classe_estimation_ges"] in ["F", "G"] or d["classe_consommation_energie"] in ["F", "G"]:
        y.append(1)
    else:
        y.append(0)

import math
X = []
for i in range(len(data)):
    X.append([])
    for c in data[0].keys():
        dc = data[i][c]        
        if c == "tr001_modele_dpe_type_libelle":
            if dc == "Copropriété":
                X[i] += [1, 0, 0, 0]
            elif dc == "Location":
                X[i] += [0, 1, 0, 0]
            elif dc == "Neuf":
                X[i] += [0, 0, 1, 0]
            elif dc == "Vente":
                X[i] += [0, 0, 0, 1]
        elif c == "tr002_type_batiment_libelle":
            if dc == "Appartement":
                X[i] += [1, 0, 0]
            elif dc == "Logements collectifs":
                X[i] += [0, 1, 0]
            elif dc == "Maison":
                X[i] += [0, 0, 1]
        else:
            # X[i].append(float(dc))
            try:
                X[i].append(float(dc))  # 尝试转换为浮点数
            except ValueError:
                # print(f"无法将 {dc} 转换为浮点数，使用 NaN 代替")
                X[i].append(math.nan)  # 或者 append 一个默认值，例如 NaN


# Exercice 2.3
from ia01.evaluation import partition_train_val

X, y, X_test, y_test = partition_train_val(X, y, 1/4)

# # Exercice 2.4
from ia01.evaluation import partition_val_croisee
from ia01.metriques import taux_erreur
from ia01.arbre import arbre_train, arbre_pred
from ia01.utils import argsort

K = 5
X_K, y_K = partition_val_croisee(X, y, K)

prof = list(range(12)) + [float("inf")]
erreur_cv = [0] * len(prof)

for i in range(K):
    X_val, y_val = X_K[i], y_K[i]
    X_train, y_train = [], []
    for j in range(K):
        if j != i:
            X_train += X_K[j]
            y_train += y_K[j]
    arbre = arbre_train(X_train, y_train)
    for j, p in enumerate(prof):
        y_pred_val = arbre_pred(X_val, arbre, max_prof=p)
        erreur_cv[j] += taux_erreur(y_val, y_pred_val) / K

for j, p in enumerate(prof):
    print(
        f"Taux d'erreur pour prof={p} ; e={erreur_cv[j]:.3f}"
    )
bestp_e = argsort(erreur_cv)[0]
print(f"Profondeur optimale : prof = {bestp_e}")


from ia01.evaluation import partition_val_croisee
from ia01.metriques import taux_erreur, precision, rappel, f_score
from ia01.arbre import arbre_train, arbre_pred
from ia01.utils import argsort

K = 5
X_K, y_K = partition_val_croisee(X, y, K)

prof = list(range(12)) + [float("inf")]
erreur_cv = [0] * len(prof)
prec_cv = [0] * len(prof)
rap_cv = [0] * len(prof)
f_cv = [0] * len(prof)

for i in range(K):
    X_val, y_val = X_K[i], y_K[i]
    X_train, y_train = [], []
    for j in range(K):
        if j != i:
            X_train += X_K[j]
            y_train += y_K[j]
    arbre = arbre_train(X_train, y_train)
    for j, p in enumerate(prof):
        y_pred_val = arbre_pred(X_val, arbre, max_prof=p)
        erreur_cv[j] += taux_erreur(y_val, y_pred_val) / K
        prec_cv[j] += precision(y_val, y_pred_val, 1) / K
        rap_cv[j] += rappel(y_val, y_pred_val, 1) / K
        f_cv[j] += f_score(y_val, y_pred_val, 1) / K

for j, p in enumerate(prof):
    print(
        f"Taux d'erreur pour prof={p} ; e={erreur_cv[j]:.3f} ; p={prec_cv[j]:.3f} ; r={rap_cv[j]:.3f} ; f={f_cv[j]:.3f}"
    )
bestp_e = argsort(erreur_cv)[0]
bestp_p = argsort(prec_cv, True)[0]
bestp_r = argsort(rap_cv, True)[0]
bestp_f = argsort(f_cv, True)[0]
print(f"Meilleur taux d'erreur : prof = {bestp_e}")
print(f"Meilleure précision : prof = {bestp_p}")
print(f"Meilleur rappel : prof = {bestp_r}")
print(f"Meilleur F1-score : prof = {bestp_f}")

# Exercice 2.8
from ia01.metriques import matrice_confusion
arbre = arbre_train(X, y)

for p in [bestp_e, bestp_p, bestp_r, bestp_f]:
    print(f"Profondeur = {p}")
    y_pred_test = arbre_pred(X_test, arbre, max_prof=p)
    erreur_test = taux_erreur(y_test, y_pred_test)
    mat_conf = matrice_confusion(y_test, y_pred_test, [0 ,1])
    for i in range(len(mat_conf)):
        print(mat_conf[i])