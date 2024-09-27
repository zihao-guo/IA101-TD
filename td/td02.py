from ia01.utils import lecture_csv
from ia01.metriques import reqm, taux_erreur
from ia01.majoritaire import vote_majoritaire
from ia01.kppv import kppv
from ia01.arbre import arbre_train, arbre_pred

data = lecture_csv("data/dorade.csv")

X_train = [[float(d["longueur"])] + ([1, 0] if d["espece"] == "marbree" else [0, 1]) for d in data]
y_train = [float(d["poids"]) for d in data]

y_pred = [vote_majoritaire(y_train, reg=True)] * len(y_train)
print("REQM pour le vote majoritaire :", reqm(y_train, y_pred))

for k in [3, 5, 7]:
    y_pred = kppv(X_train, X_train, y_train, k, reg=True)
    print("REQM pour k =", k, ":", reqm(y_train, y_pred))

arbre = arbre_train(X_train, y_train)

for p in [2, 5, 10, 20, 30]:
    y_pred = arbre_pred(X_train, arbre, p)
    print("Profondeur max =", p, ":", taux_erreur(y_train, y_pred))