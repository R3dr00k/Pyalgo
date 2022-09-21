#!/usr/bin/python3

def tri_bulles(tab):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(tab)-1):
            if tab[i] > tab[i+1]:
                tab[i], tab[i+1] = tab[i+1], tab[i]
                sorted = False
    return tab

print(tri_bulles([3, 3, 3, 3, 3]))
