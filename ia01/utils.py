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
