import doctest

def pair(a):
    return not a%2

def appliquer_fonction_liste(liste, fonction):
    '''
    Appliquer une fonction à tous les éléments d'une liste
    -----
    Params
      liste : list
      fonction : function
    -----
    Return
      liste
    -----
    Examples
    >>> appliquer_fonction_liste([1, 2, 3, 4], lambda x : x**2)
    [1, 4, 9, 16]
    >>> appliquer_fonction_liste([1, 2, 3, 4], pair)
    [False, True, False, True]
    '''
    return [fonction(i) for i in liste]

def transfo_liste_dico(liste):
    '''
    Transformer une liste de tuples en dictionnaire
    -----
    Example
    >>> transfo_liste_dico([("key1",12),("key2",4)])
    {'key1': 12, 'key2': 4}
    '''
    return dict(liste)

def ordonner_et_supprimer_doublons(liste, ascendant):
    '''
    Ordonner une liste et supprimer les doublons
    -----
    Params
      liste : list
      ascendant : boolean (True pour ASC, False pour DESC)
    -----
    Examples
    >>> ordonner_et_supprimer_doublons([3, 1, 1, 2, 3], True)
    [1, 2, 3]
    >>> ordonner_et_supprimer_doublons([3, 1, 1, 2, 3], False)
    [3, 2, 1]
    '''
    return sorted(list(set(liste)), reverse = not ascendant)



if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = True)