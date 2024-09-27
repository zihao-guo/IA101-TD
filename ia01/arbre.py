from ia01.utils import gini, moyenne, variance

def score(y, reg):
    return variance(y) if reg else gini(y)

# -------------------------- Ex2.2 --------------------------
def coupe(X, y, d, s):
    """Partitionnement d'un ensemble sur le dimension d par rapport à un seuil s

    Paramètres
    ----------
    X : list[list]
        Liste de vecteurs à partitionner
    y : list
        Liste des prédictions associées à X
    d : int
        Dimension selon laquelle faire la coupe
    s : float
        Seuil pour faire la coupe

    Sorties
    -------
    X_inf, y_inf, X_sup, y_sup :
        X_inf, y_inf : partie des éléments tels que x[d] <= s
        X_sup, y_sup : partie des éléments tels que x[d] > s
    """
    assert (
        isinstance(d, int) and d >= 0
    ), "Le paramètre `d` doit être un entier positif."

    pass  # À compléter

def coupe(X, y, d, s):
    assert (
        isinstance(d, int) and d >= 0
    ), "Le paramètre `d` doit être un entier positif."

    n = len(X)
    X_inf, y_inf, X_sup, y_sup = [], [], [], []
    for i in range(n):
        if X[i][d] <= s:
            X_inf.append(X[i])
            y_inf.append(y[i])
        else:
            X_sup.append(X[i])
            y_sup.append(y[i])
    return X_inf, y_inf, X_sup, y_sup

# # Example dataset
# X = [
#     [1, 2],   # Sample 1
#     [3, 4],   # Sample 2
#     [2, 1],   # Sample 3
# ]
# y = [0, 1, 0]  # Labels corresponding to the samples

# # Set feature index d and threshold s
# d = 0  # We are splitting based on the first feature (d=0)
# s = 2.5  # Threshold value for splitting

# # Call the coupe function
# X_inf, y_inf, X_sup, y_sup = coupe(X, y, d, s)

# # Print the results
# print("X_inf:", X_inf)
# print("y_inf:", y_inf)
# print("X_sup:", X_sup)
# print("y_sup:", y_sup)

# -------------------------- Ex2.3 -------------------------- P55
def score_coupe(X, y, d, s, reg):
    _, y_inf, _, y_sup = coupe(X, y, d, s)
    n_inf = len(y_inf)
    n_sup = len(y_sup)
    n = n_inf + n_sup
    return n_inf / n * score(y_inf, reg) + n_sup / n * score(y_sup, reg)

# # Example dataset
# X = [
#     [1, 2],   # Sample 1
#     [2, 3],   # Sample 2
#     [3, 4],   # Sample 3
#     [4, 5],   # Sample 4
#     [5, 6],   # Sample 5
# ]
# y = [0, 1, 0, 1, 0]  # Labels corresponding to the samples (classification task)

# # Set feature index d and threshold s
# d = 0  # Split based on the first feature
# s = 2.5  # Threshold value for the split

# # Call the coupe function
# X_inf, y_inf, X_sup, y_sup = coupe(X, y, d, s)
# # Print the results
# print("X_inf:", X_inf)
# print("y_inf:", y_inf)
# print("X_sup:", X_sup)
# print("y_sup:", y_sup)
# # Call score_coupe for classification (reg = False)
# split_score_classification = score_coupe(X, y, d, s, reg=False)
# print("Score for classification (Gini index):", float(split_score_classification))

# -------------------------- Ex2.4 --------------------------
def seuil_coupe(X, d):
    """Calcul des seuils auxquels partitionner un ensemble sur la dimension d

    Paramètres
    ----------
    X : list[list]
        Liste de vecteurs à partitionner
    d : int
        Dimension selon laquelle faire la coupe        

    Sorties
    -------
    seuils : list
        Seuils pour faire les coupes
    """
    assert (
        isinstance(d, int) and d >= 0
    ), "Le paramètre `d` doit être un entier positif."

    pass  # À compléter

from ia01.utils import unique

def seuil_coupe(X, d):
    assert (
        isinstance(d, int) and d >= 0
    ), "Le paramètre `d` doit être un entier positif."

    xd = [x[d] for x in X]
    xd = sorted(unique(xd))
    n = len(xd)

    seuils = []
    for i in range(n-1):
        seuils.append((xd[i] + xd[i+1]) / 2)

    return seuils

# # Example dataset
# X = [
#     [1, 2],   # Sample 1
#     [3, 4],   # Sample 2
#     [2, 1],   # Sample 3
#     [4, 5],   # Sample 4
#     [5, 6]    # Sample 5
# ]
# # Feature index
# d = 0  # We will use the first feature (d=0) for splitting
# # Call seuil_coupe to calculate thresholds
# seuils = seuil_coupe(X, d)
# # Print the thresholds
# print("Thresholds:", seuils)


# -------------------------- Ex2.5 --------------------------
def meilleure_coupe(X, y, reg):
    """Calcul des seuils auxquels partitionner un ensemble sur la dimension d

    Paramètres
    ----------
    X : list[list]
        Liste de vecteurs à partitionner
    y : list
        Liste des prédictions associées à X
    reg : bool
        Indique s'il s'agit d'un problème de régression (True) ou de classification (False)

    Sorties
    -------
    best_dim : int
        Meilleure dimension pour faire la coupe
    best_seuil : float
        Meilleure seuils pour faire la coupe
    X_inf, y_inf, X_sup, y_sup : list
        Partitionnement résultant de la coupe
    """
    dim = len(X[0])
    # Initialisation
    best_dim = 0
    best_seuil = -float("inf")
    best_score = score(y, reg)
    # Iteration sur chaque dimension
    for d in range(dim):
        seuils = seuil_coupe(X, d)
        # Iteration sur les seuils
        for s in seuils:
            sc = score_coupe(X, y, d, s, reg)
            if sc < best_score:
                best_score = sc
                best_dim = d
                best_seuil = s
    X_inf, y_inf, X_sup, y_sup = coupe(X, y, best_dim, best_seuil)
    return best_dim, best_seuil, X_inf, y_inf, X_sup, y_sup

from ia01.majoritaire import vote_majoritaire


def arbre_train(X_train, y_train, reg=False, max_prof=float("inf"), profondeur=0):
    """
    Apprentissage d'un arbre de décision

    Paramètres
    ----------
    X_train : list[list]
        Liste des vecteurs de l'ensemble d'apprentissage
    y_train : list
        Liste des prédictions associées aux éléments de X_train
    reg : bool, default = False
        Indique s'il s'agit d'un problème de régression (True) 
        ou de classification (False)
    max_prof : int, default = float("inf")
        Profondeur maximale de l'arbre de décision
    profondeur : int
        Profondeur courante du noeud de l'arbre, paramètre utilisé par récurrence

    Sorties
    -------
    arbre :
        Structure arbre binaire, chaque noeud est un dictionnaire contenant 
        un champ "info" et un champ "coupe".
        Dans le champ "info", il y a l'information de profondeur ("profondeur"), 
        le score associé ("score") et une prédiction si elle est faite 
        au niveau de ce noeud ("prediction").
        Le champ "coupe" est nul ("None") si le noeud est une feuille, sinon il
        contient la dimension ("dimension") et le seuil ("seuil") de la coupe ainsi
        que les deux sous-arbres résultants de la coupe ("arbre_inf" et "arbre_sup").
    """
    arbre = {
        "info": {
            "profondeur": profondeur,
            "score": score(y_train, reg),
            "prediction": vote_majoritaire(y_train, reg),
        },
        "coupe": None,
    }
    if profondeur < max_prof:
        d, s, X_inf, y_inf, X_sup, y_sup = meilleure_coupe(X_train, y_train, reg)
        if X_inf:
            arbre["coupe"] = {
                "dimension": d,
                "seuil": s,
                "arbre_inf": arbre_train(X_inf, y_inf, reg, max_prof, profondeur + 1),
                "arbre_sup": arbre_train(X_sup, y_sup, reg, max_prof, profondeur + 1),
            }
    return arbre


def arbre_pred(X, arbre, max_prof=float("inf")):
    """
    Prédiction à partir d'un arbre de décision

    Paramètres
    ----------
    X : list[list]
        Liste de vecteurs sur lesquels appliquer l'arbre de décision
    arbre : 
        Arbre de décision
    max_prof : int, default = float("inf")
        Profondeur maximale d'exploration de l'arbre de décision

    Sorties
    -------
    y_pred : list
        Liste des prédictions associées aux éléments de X
    """

    def arbre_pred_single(x, arbre, max_prof):
        if arbre["coupe"] is None or arbre["info"]["profondeur"] >= max_prof:
            return arbre["info"]["prediction"]
        else:
            d = arbre["coupe"]["dimension"]
            s = arbre["coupe"]["seuil"]
            if x[d] <= s:
                return arbre_pred_single(x, arbre["coupe"]["arbre_inf"], max_prof)
            else:
                return arbre_pred_single(x, arbre["coupe"]["arbre_sup"], max_prof)

    return [arbre_pred_single(x, arbre, max_prof) for x in X]