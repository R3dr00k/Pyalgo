def tri_selection(tab):
    for i in range(len(tab)):
        min = i
        for j in range(i, len(tab)):
            if tab[j] < tab[min]:
                min = j

        tab[i], tab[min] = tab[min], tab[i]

    return tab

print(tri_selection([5, 3, 8, 0, 10]))
