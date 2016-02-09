if __name__ == "__main__":
    suzi = range(0,10)
    j = 0
    for i in range(0,10):
        tmp = input("input>>")
        suzi.append(tmp)
        for j in list(reversed(range(i))):
            if j > 0 and suzi[j-1]>tmp:
                suzi[j]=suzi[j-1]
            else:
                break
        suzi[j] = tmp
    for i in range(0,10):
        print suzi[i]
