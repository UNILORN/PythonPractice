# -*- coding: utf-8 -*-
if __name__ == "__main__":
    name = raw_input(u"name ? >>")
    age  = input(u"age ?  >>")
    sex  = input(u"sex ? (Man:0,Woman:1) >>")
    print u"name is  " + name
    print u"age is  " + str(age)
    if sex == 0:
        print u"Man"
    else:
        print u"Woman"
