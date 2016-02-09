#sosu program
if __name__ == "__main__":
    sosu = [2]
    sosu_yoso = 1
    for i in range(3,input('input >>')):
        cnt = 0
        for j in range(0,sosu_yoso):
            if i % sosu[j] == 0:
                cnt += 1
                break
        if cnt == 0:
            sosu.append(i)
            sosu_yoso += 1
    print sosu
