# -*- coding: utf-8 -*-
import multiprocessing as mp

L = 8000
proc = 4

def subcalc(p):
    subtotal = 0

    ini = L * p / proc
    fin = L * (p+1) / proc

    for i in range(ini,fin):
        for j in range(L):
            subtotal += i * j
    return subtotal

pool = mp.Pool(proc)

callback = pool.map(subcalc,range(proc))

total = sum(callback)

print (total)
