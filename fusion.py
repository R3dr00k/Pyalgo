#!/usr/bin/python3

def fusion(tab1, tab2):
    if len(tab1) == 0:
        return tab2
    if len(tab2) == 0:
        return tab1

    if tab1[0] < tab2[0]:
        return [tab1[0]] + fusion(tab1[1:], tab2)
    else:
        return [tab2[0]] + fusion(tab1, tab2[1:])


def tri_fusion(tab):
    size = len(tab)
    # cas arret = si len 1 ou 2
    if len(tab) == 2:
        if tab[1] < tab[0]:
            return [tab[1], tab[0]]
        else:
            return tab
    if len(tab) == 1:
        return tab

    return fusion(tri_fusion(tab[:size//2]), tri_fusion(tab[size//2:]))

print(tri_fusion([5, 3, 5, 8, 9, 19, 3, 6, 18, 17, 10]))

