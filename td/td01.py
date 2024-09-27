# classification 2-5
from ia01.utils import lecture_csv
from ia01.metriques import taux_erreur
from ia01.majoritaire import vote_majoritaire

data = lecture_csv("data/dorade.csv") # Lecture du fichier CSV

y_true = [d["espece"] for d in data] # Labels réels
y_pred = [vote_majoritaire(y_true)] * len(y_true) # Labels prédits
print("Taux d'erreur: ", taux_erreur(y_true, y_pred)*100, "%")


# regression 2-4
from ia01.utils import lecture_csv
from ia01.metriques import eqm
from ia01.majoritaire import vote_majoritaire

data = lecture_csv("data/dorade.csv")

y_true = [float(d["poids"]) for d in data] # Labels réels
y_pred = [vote_majoritaire(y_true, reg=True)] * len(y_true) # Labels prédits

print(eqm(y_true, y_pred)) 