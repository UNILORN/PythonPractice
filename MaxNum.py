# -*- coding: utf-8 -*-
if __name__ == "__main__":
    i_max = 0
    suji = []
    for i in range(0,10):
        suji.append(input("input>>"))
        if i_max < suji[i]:
            i_max = suji[i]
    print suji
    print i_max
