# -*- coding: utf-8 -*-
if __name__ == "__main__":

    class Car():
        def __init__(self,name,color):
            self.name  = name
            self.color = color
        def Run(self):
            print u"%sは走った！" %self.name

    Purius = Car("purius","White")

    Purius.Run()
