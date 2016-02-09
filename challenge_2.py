# -*- coding: utf-8 -*-

def sexprint(self):
    if self.sex == 0:
        return u"男"
    elif self.sex == 1:
        return u"女"
    else:
        return u"不明"
        
class Parson():
    def __init__(self):
        self.name = raw_input(u"input name>>")
        self.age  = input(u"input age>>")
        self.sex  = input(u"input sex>>")

    def printout(self):
        print u"名前：" + self.name
        print u"年齢: " + str(self.age)
        print u"性別: " + sexprint(self)

if __name__ == "__main__":

    Parson_Menber = input(u"ninzu >>")

    Menber = []
    for i in range(0,Parson_Menber):
        Menber.append(Parson())

    for i in range(0,Parson_Menber):
        print Menber[i].printout()
