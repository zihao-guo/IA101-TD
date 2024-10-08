from ia01.utils import moyenne, unique

## TD01
# ==============


def taux_erreur(y_true, y_pred):
    """Taux d'erreur pour un problème de classification

    Paramètres
    ----------
    y_true : list
        Liste contenant les vraies valeurs
    y_pred : list
        Liste contenant les valeurs prédites par un classifieur

    Sorties
    -------
    err : float [0,1]
        Ratio (entre 0 et 1) d'éléments où y_true et y_pred sont différents.
    """
    n = len(y_true)
    err = 0
    for i in range(n):
        if y_true[i] != y_pred[i]:
            err += 1
    return err / n


def eqm(y_true, y_pred):
    """Erreur quadratique moyenne pour un problème de regression

    Paramètres
    ----------
    y_true : list
        Liste contenant les vraies valeurs
    y_pred : list
        Liste contenant les valeurs prédites

    Sorties
    -------
    e : float
        Erreur quadratique moyenne
    """
    n = len(y_true)
    err = 0
    for i in range(n):
        err += (y_true[i] - y_pred[i]) ** 2
    return err / n


def reqm(y_true, y_pred):
    """Racine de l'erreur quadratique moyenne pour un problème de regression

    Paramètres
    ----------
    y_true : list
        Liste contenant les vraies valeurs
    y_pred : list
        Liste contenant les valeurs prédites

    Sorties
    -------
    e : float
        Racine de l'erreur quadratique moyenne
    """
    return eqm(y_true, y_pred) ** 0.5


## TD04
# ==============

