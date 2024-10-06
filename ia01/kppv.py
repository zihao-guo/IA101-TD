# ================== ex1.1
def distance2(x1, x2, p=2):
    """Calcule la distance de Minkowski de paramètre p entre les vecteurs x1 et x2

    Paramètres
    ----------
    x1, x2 : list
        Vecteurs de dimension d
    p : float, default = 2
        Paramètre de la distance de Minkowski
        p > 0, pour la distance de Tchebychev p = float('inf')

    Sorties
    -------
    dist : float
        Distance entre x1 et x2
    """

    assert len(x1) == len(x2), "Les vecteurs x1 et x2 doivent être de même dimension."
    assert p > 0, "Le paramètre p doit être strictement supérieur à 0."

    # if p < float("inf"): # Distance de Minkowski (Σ|x1_i - x2_i|^p)^(1/p)
    #     pass  # À compléter
    # else: # Distance de Tchebychev max(|x1_i - x2_i|)
    #     pass  # À compléter
    d = 0
    dim = len(x1)
    if p < float("inf"):
        for i in range(dim):
            d += abs(x1[i] - x2[i]) ** p
        return d ** (1/p)
    else:
        for i in range(dim):
            di = abs(x1[i] - x2[i])
            if di > d:
                d = di
        return d

# # Test de la fonction distance2
# import math
# ## Test case 1: p=2 (Euclidean distance)
# x1 = [0, 0]
# x2 = [3, 4]
# expected = expected = math.sqrt(sum((abs(a - b) ** 2 for a, b in zip(x1, x2))))  # Euclidean distance: sqrt(3^2 + 4^2) = 5
# result = distance2(x1, x2, p=2)
# print('====================')
# print("Euclidean distance (p=2):")
# print("Expected:", expected)
# print(f"Got: {result} - {'Correct' if math.isclose(result, expected) else f'Incorrect, expected {expected}'}")

# ## Test case 2: p=1 (Manhattan distance)
# x1 = [0, 0]
# x2 = [3, 4]
# expected = sum(abs(a - b) for a, b in zip(x1, x2))  # Manhattan distance: abs(3-0) + abs(4-0) = 7
# result = distance2(x1, x2, p=1)
# print('====================')
# print("Manhattan distance (p=1):")
# print("Expected:", expected)
# print(f"Got: {result} - {'Correct' if math.isclose(result, expected) else f'Incorrect, expected {expected}'}")

# ## Test case 3: p=∞ (Chebyshev distance)
# x1 = [0, 0]
# x2 = [3, 4]
# expected = max(abs(a - b) for a, b in zip(x1, x2))  # Chebyshev distance: max(abs(3-0), abs(4-0)) = 4
# result = distance2(x1, x2, p=float("inf"))
# print('====================')
# print("Chebyshev distance (p=∞):")
# print("Expected:", expected)
# print(f"Got: {result} - {'Correct' if math.isclose(result, expected) else f'Incorrect, expected {expected}'}")


# ================== ex1.2
def distance(x, X_train, p=2):
    """Calcule la distance de Minkowski de paramètre p entre le vecteur x
       et tous les éléments de X_train.

    Paramètres
    ----------
    X_train : list[list]
        Liste de vecteurs de dimension d
    x : list
        Vecteur de dimension d
    p : float, default = 2
        Paramètre de la distance de Minkowski
        p > 0, pour la distance de Tchebychev p = float('inf')

    Sorties
    -------
    dist : list
        Distances entre x et tous les éléments de X_train
    """

    # pass  # À compléter
    dist = []
    for i in range(len(X_train)):
        dist.append(distance2(x, X_train[i], p))
    return dist

# # # Test de la fonction distance
# import math
# x = [1, 2] 
# X_train = [[3, 4], [0, 0], [5, 6]]  # Points d'entraînement
# # Calcul des distances entre x et les points d'entraînement
# distances = distance(x, X_train, p=2) # Euclidean distance comme example
# manual_distances = [
#     math.sqrt((3 - 1) ** 2 + (4 - 2) ** 2),  # Distance from [1, 2] to [3, 4]
#     math.sqrt((1 - 0) ** 2 + (2 - 0) ** 2),  # Distance from [1, 2] to [0, 0]
#     math.sqrt((5 - 1) ** 2 + (6 - 2) ** 2)   # Distance from [1, 2] to [5, 6]
# ]
# print(f"Calculated distances: {distances}")
# print(f"Manual distances: {manual_distances}")
# print(f"Results are {'correct' if distances == manual_distances else 'incorrect'}")


# ================== ex1.3
from ia01.utils import argsort
from ia01.majoritaire import vote_majoritaire

def kppv(X, X_train, y_train, k, p=2, reg=False):
    """Méthode des k plus proches voisins

    Paramètres
    ----------
    X : list[list]
        Liste de vecteurs sur lesquels appliquer la méthode des k-ppv
    X_train : list[list]
        Liste des vecteurs de l'ensemble d'apprentissage
    y_train : list
        Liste des prédictions associées aux éléments de X_train
    k : int
        Nombre de voisins
    p : float, default = 2
        Paramètre de la distance de Minkowski
        p > 0, pour la distance de Tchebychev p = float('inf')
    reg : bool, default = False
        Indique s'il s'agit d'un problème de régression (True) ou de classification (False)

    Sorties
    -------
    y_pred : list
        Liste des prédictions associées aux éléments de X
    """

    assert isinstance(k, int) and k > 0, "k doit être un entier strictement positif"

    # pass # À compléter
    y_pred = []
    for i in X:
        dist = distance(i, X_train, p)
        idx = argsort(dist)
        y_pred.append(vote_majoritaire([y_train[idx[j]] for j in range(k)], reg))
    return y_pred

# Test de la fonction kppv
# Training data (X_train) and labels (y_train)
X_train = [[1, 2], [2, 3], [3, 4], [6, 7], [7, 8]]
y_train = [0, 0, 0, 1, 1]  # 0 and 1 are two classes
# Test data (X) for which we want to predict the labels
X = [[2, 2], [5, 5]]
# Set k (number of neighbors) and p (Euclidean distance, p=2)
k = 3
p = 2
for i, xi in enumerate(X):
    print(f"\nProcessing test point {i+1}: {xi}") # Print the current test point
    dist = distance(xi, X_train, p) # Compute the distances between the test point and the training points
    print(f"Distances to training points: {dist}")
    idx = argsort(dist) # Sort the distances and get the indices
    print(f"Indices of sorted distances: {idx}")
    neighbors = [y_train[idx[j]] for j in range(k)] # Get the labels of the k nearest neighbors
    print(f"Labels of nearest neighbors: {neighbors}")
    y_pred = vote_majoritaire(neighbors, reg=False) # Predict the label of the test point
    print(f"Predicted label: {y_pred}")

# ================== ex1.3+4
# from ia01.utils import lecture_csv
# from ia01.metriques import taux_erreur

# data = lecture_csv("data/dorade.csv")
# X_train = [[float(d["longueur"]), float(d["poids"])] for d in data]
# y_train = [d["espece"] for d in data]

# for k in [3, 5, 7]:
#     y_pred = kppv(X_train, X_train, y_train, k)
#     print("Taux d'erreur pour k =", k, ":", taux_erreur(y_train, y_pred))

# for k in [1, 200]:
#     y_pred = kppv(X_train, X_train, y_train, k)
#     print("Taux d'erreurs pour k =", k, ":", taux_erreur(y_train, y_pred))
# If k is too large (e.g., more than the size of the training set), 
# then almost all points are considered as neighbors 
# the classification results are significantly degraded.