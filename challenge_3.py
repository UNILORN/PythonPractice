# -*- coding: utf-8 -*-
if __name__ == "__main__":
    i = 0
    name = []
    while True:
        name.append(raw_input("name>>"))
        if name[i] == "stop":
            break
        i += 1
    print name
