def taux_erreur(y_true, y_pred):
    '''Calcule le taux d'erreur entre y_true et y_pred'''
    n = len(y_true)
    err = 0 
    for i in range(n): # Parcours de tous les éléments
        if y_true[i] != y_pred[i]: # Si la prédiction est fausse
            err += 1 # On incrémente le nombre d'erreurs
    return err / n

# y_true = [1, 1, 1, 1, 1 ]
# y_pred = [1, 0, 0, 1, 0 ]
# print(taux_erreur(y_true, y_pred))


def eqm(y_true, y_pred):
    '''Calcule l'erreur quadratique moyenne entre y_true et y_pred'''
    n = len(y_true)
    err = 0
    for i in range(n): # Parcours de tous les éléments
        err += (y_true[i] - y_pred[i]) ** 2 # On ajoute l'erreur au carré
    return err / n

# # Liste des valeurs réelles
# y_true = [1.0, 0.0, 2.0, 8.0]
# # Liste des valeurs prédites
# y_pred = [1.0, 0.0, 2.0, 8.0]
# print(eqm(y_true, y_pred))

def reqm(y_true, y_pred):
    return eqm(y_true, y_pred) ** 0.5

# TD04
## EX1.3
def repartition(x, X):
    n = len(X)
    F = 0
    for i in range(n):
        if X[i] <= x:
            F = F + 1
    return F / n

# X = [1, 2, 3, 4, 5]
# x = 3
# print(repartition(x, X))

## EX1.4
def quantile(X, alpha):
    qx = []
    for x in X:
        if repartition(x, X) >= alpha:
            qx.append(x)
    return min(qx)
# X = [1, 2, 3, 4, 5]
# alpha = 0.5
# print(quantile(X, alpha))

## EX1.5
def valeurs_lim(X):
    q1 = quantile(X, 0.25)
    q3 = quantile(X, 0.75)
    IQR = q3 - q1
    x_min, x_max = [], []
    for x in X:
        if x >= q1 - 1.5 * IQR:
            x_min.append(x)
        if x <= q3 + 1.5 * IQR:
            x_max.append(x)
    v_min = min(x_min)
    v_max = max(x_max)

    return v_min, v_max

# X = [1, 2, 3, 4, 5, 6, 7, 100, 150]
# print(valeurs_lim(X)) 



## EX2.5
def precision(y_true, y_pred, label_pos):
    VP = 0
    FP = 0
    for yt, yp in zip(y_true, y_pred):
        if yp == label_pos:
            if yt == label_pos:
                VP += 1
            else:
                FP += 1
    if VP + FP == 0:
        return 0
    else:
        return VP / (VP + FP)
    
def rappel(y_true, y_pred, label_pos):
    VP = 0
    FN = 0
    for yt, yp in zip(y_true, y_pred):
        if yt == label_pos:
            if yp == label_pos:
                VP += 1
            else:
                FN += 1
    if VP + FN == 0:
        return 0
    else:
        return VP / (VP + FN)

def f_score(y_true, y_pred, label_pos, beta=1):
    prec = precision(y_true, y_pred, label_pos)
    rap = rappel(y_true, y_pred, label_pos)
    if prec + rap == 0:
        return 0
    else:
        return ((1 + beta**2)*(prec * rap)) / (beta**2 * prec + rap)
    
y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]  # Vraies étiquettes
y_pred = [1, 0, 1, 0, 0, 1, 1, 0, 0, 0]  # Étiquettes prédites
# label_pos = 1  # Étiquette positive

# prec = precision(y_true, y_pred, label_pos)
# print(f"precision: {prec:.2f}")
# rap = rappel(y_true, y_pred, label_pos)
# print(f"rappel: {rap:.2f}")
# f1 = f_score(y_true, y_pred, label_pos, beta=1)
# print(f"f_score: {f1:.2f}")


    
# EX2.7
def matrice_confusion(y_true, y_pred, labels):
    idx = dict(zip(labels, range(len(labels))))
    K = len(labels)
    mat = []
    for k in range(K):
        mat.append([0] * K)
    for yt, yp in zip(y_true, y_pred):
        mat[idx[yp]][idx[yt]] += 1
    return mat

labels = [0, 1]  # Étiquettes possibles
conf_matrix = matrice_confusion(y_true, y_pred, labels)
print("Matrice de confusion:")
for row in conf_matrix:
    print(row)