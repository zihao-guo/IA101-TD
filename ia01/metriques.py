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