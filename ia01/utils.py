def test_utils():
    """Fonction de test"""
    print("Test du module utils du package ia01 !")

def unique(y):
    '''Trouve les éléments uniques de la liste y'''
    return list(set(y))

def compte(y):
    '''Compte le nombre d'occurrences de chaque élément dans la liste y'''
    return [y.count(ob) for ob in unique(y)]

# print(unique([1, 1, 2, 3, 3, 3, 3]))
# print(compte([1, 1, 2, 3, 3, 3, 3]))
# print(unique(["chat", "chien", "chien", "chat", "chat", "chat"]))
# print(compte(["chat", "chien", "chien", "chat", "chat", "chat"]))

def lecture_csv(fichier, sep=","):
    """Lecture d'un fichier texte sous format CSV.
    La première ligne du fichier donne le nom des champs.

    Paramètres
    ----------
    fichier : string
        Chemin vers le fichier à lire
    sep : char, default = ","
        Caractère pour séparer les champs

    Sorties
    -------
    data : list of dict
        Liste des éléments du fichier CSV.
        Chaque élément est stocké dans un dictionnaire dont les champs
        sont donnés par la première ligne du fichier CSV.
    """
    data = []
    with open(fichier, "r") as f:
        lines = f.read().splitlines()
        keys = lines[0].split(sep)
        for line in lines[1:]:
            values = line.split(sep)
            data.append(dict(zip(keys, values)))
    return data


def moyenne(y):
    '''Calcule la moyenne des éléments de la liste y'''
    return sum(y) / len(y)
# # Liste des valeurs
# y = [2.5, 2.5, 2.5]
# # Calcul de la moyenne
# moyenne_valeur = moyenne(y)
# print(moyenne(y))

def argsort(x, reverse=False):
    """Calcul l'indice de chaque élément dans l'ordre trié.

    Paramètres
    ----------
    x : list
        Liste d'éléments non trié
    reverse : bool
        False (par défaut): tri par ordre croissant
        True : tri par ordre décroissant

    Sorties
    -------
    idx : list
        Liste des indices dans l'ordre
        Si tri croissant, alors x[idx[0]] est le plus petit élément de x
    """
    return sorted(range(len(x)), key=x.__getitem__, reverse=reverse)

# x = [5, 1, 6, 4, 8, 2, 9]
# idx = argsort(x)
# print("Les deux plus petits éléments de x sont :", x[idx[0]], "et", x[idx[1]])


# ================== ex1.6
def normalisation(X, loc, scale):
    """Méthodes de normalisation de vecteurs

    Paramètres
    ----------
    X : list[list]
        Liste de vecteurs sur lesquels appliquer la normalisation
    loc, scale : list
        Liste de paramètres de normalisation pour chaque dimension
        Pour un vecteur x de la liste X, la normalisation pour chaque dimension est :
        x[j] = (x[j] - loc[j]) / scale[j]

    Sorties
    -------
    Xnorm : list[list]
        Liste des vecteurs normalisés
    """
    
    pass # À compléter

def normalisation(X, loc, scale):
    n = len(X)
    d = len(X[0])
    X_norm = []
    for i in range(n):
        xi_norm = []
        for j in range(d):
            xi_norm.append((X[i][j] - loc[j]) / scale[j])
        X_norm.append(xi_norm)
        
    return X_norm

# # Example dataset X with two features
# X = [
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ]
# # Mean (loc) and standard deviation (scale) for each feature
# loc = [3, 4]     # Means for each feature
# scale = [2, 2]   # Standard deviations for each feature
# # Call the normalisation function
# X_norm = normalisation(X, loc, scale)
# # Print the normalized dataset
# print("Normalized dataset:", X_norm)

# ================== ex1.7
def norm_param(X, methode="echelle"):
    """Calcul des paramètres de normalisation

    Paramètres
    ----------
    X : list[list]
        Liste de vecteurs à partir desquels calculer les paramètres de normalisation
    methode : str, default = "echelle"
        Méthode de normalisation utilisée : "echelle" ou "centre"

    Sorties
    -------
    loc, scale : list
        Liste de paramètres de normalisation pour chaque dimension
    """

    assert (
        methode == "echelle" or methode == "centre"
    ), "Le paramètre `methode` doit valoir `echelle` ou `centre`."
    pass  # À compléter

def variance(x):
    n = len(x)
    var = 0
    x_moy = moyenne(x)
    for i in range(n):
        var = var + (x[i] - x_moy) ** 2
    var = var / n
    return var

def ecart_type(x):
    return variance(x) ** 0.5

def norm_param(X, methode="echelle"):
    assert (
        methode == "echelle" or methode == "centre"
    ), "Le paramètre `methode` doit valoir `echelle` ou `centre`."

    n = len(X)
    d = len(X[0])
    loc, scale = [], []

    for j in range(d):
        X_j = []
        for i in range(n):
            X_j.append(X[i][j])
        if methode == "echelle":
            min_j = min(X_j)
            max_j = max(X_j)
            loc.append(min_j)
            scale.append(max_j - min_j)
        else:
            moy_j = moyenne(X_j)
            std_j = ecart_type(X_j)
            loc.append(moy_j)
            scale.append(std_j)

    return loc, scale

# # Exemple de dataset X
# X = [
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ]
# # Appel à norm_param avec la méthode "echelle" (min-max scaling)
# loc_echelle, scale_echelle = norm_param(X, methode="echelle")
# print("Paramètres pour l'échelle (min-max scaling):")
# print("loc:", loc_echelle) # [1] [4]
# print("scale:", scale_echelle)
# # Appel à norm_param avec la méthode "centre" (z-score normalization)
# loc_centre, scale_centre = norm_param(X, methode="centre")
# print("\nParamètres pour la centration (z-score normalization):")
# print("loc:", loc_centre) # [3] [8/3^(1/2)]
# print("scale:", scale_centre)


# ================== ex2.1
def gini(y):
    """Calcul de l'impureté de Gini

    Paramètres
    ----------
    y : list
        Liste de labels

    Sorties
    -------
    g : float
        Impureté de Gini
    """

    pass  # À compléter

def gini(y):
    c = compte(y)
    n = sum(c)
    g = 1
    for ci in c:
        g -= (ci/n) ** 2
    return g

# # Exemple d'une liste de classes
# y = [0, 1, 0, 0, 1]
# # Afficher le résultat
# print("Indice de Gini:", gini(y))

# TD04
## EX1.7
def est_complet(x):
    for c in x.keys():
        if x[c] == "":
            return False
    return True
# x = {"name": "Alice", "age": "25", "city": "Paris"}
# print(est_complet(x))
# x = {"name": "Bob", "age": "", "city": "London"}
# print(est_complet(x)) 
