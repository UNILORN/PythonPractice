if __name__ == "__main__":
    suzi = range(0,10)
    for i in range(0,10):
        tmp = input("input>>")
        suzi.append(tmp)
        j = i
        while j > 0 and suzi[j-1]>tmp:
            suzi[j]=suzi[j-1]
            j -= 1
        suzi[j] = tmp
    for i in range(0,10):
        print suzi[i]
