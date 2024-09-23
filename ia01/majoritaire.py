from ia01.utils import unique, compte, moyenne

def vote_majoritaire(y, reg=False):
    """Applique le vote majoritaire à la liste y.

    Paramètres
    ----------
    y : list
        Liste des labels pour l'ensemble des données
    reg : bool, default = False
        Indique s'il s'agit d'un problème de régression (True) ou de classification (False)
        Par défaut, on considère qu'il s'agit d'un problème de classification (reg=False)

    Sorties
    -------
    label
        Classification : label le plus représenté dans la liste y
        Regression : moyenne empirique des éléments de y
    """
    if reg:
        # Problème de régression
        return moyenne(y)
    else:
        # Problème de classification
        label = unique(y)
        nombre = compte(y)
        i_max, n_max = -1, -1 # Initialisation
        for i in range(len(label)): # Parcours de tous les labels
            if nombre[i] > n_max: # Si le nombre d'occurrences est plus grand
                n_max = nombre[i] # On met à jour le nombre d'occurrences
                i_max = i # On met à jour l'indice du label majoritaire
        return label[i_max]
    
# # Exemple pour la classification
# y_classification = [1, 0, 1, 1, 0]
# print(vote_majoritaire(y_classification))
