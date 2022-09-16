#!/usr/bin/python3.9
import time
import random

def tri_insertion(tab):
    for i in range(1,len(tab)):
        for j in range(0, i):
            if tab[i] <= tab[j]:
                tab.insert(j, tab.pop(i))
                break
    return tab


print("Time To Test (TTT)")
array_test1 = [3, 19, 2, 5, 21, 14, 30, 2, 7, 11]
print("on a little array: ")
print("array : ", array_test1, " len : ", len(array_test1))

t1_start = time.perf_counter()
sorted_array = tri_insertion(array_test1)
t1_end = time.perf_counter()

print("=>", sorted_array ," in ", t1_end - t1_start, "s")

print("On A Big One ...")
array_test2 = [random.randint(0, 1000) for i in range(0, 10000)]
print("len : ", len(array_test2))
        
t2_start = time.perf_counter()
tri_insertion(array_test2)
t2_end = time.perf_counter()

print("may be sorted in ", t2_end - t2_start, "s")
