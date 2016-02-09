# -*- coding: utf-8 -*-
import sqlite3

#テーブル作成クラス
#self.sql=[テーブル作成SQL文]
class C_Table:

    def __init__(self,Tablename):
        self.Tablename = Tablename
        self.Taplename = []
        self.Tapleindex = []
        self.sql = """ """

    def TableAddName(self):
        taplename = []
        i = 0
        while True:
            name = raw_input("Create Taple >> ")
            taplename.append(name)
            if taplename[i] == "@end":
                break
            i += 1
        self.Taplename = taplename

    def TapleAddIndex(self):
        tapleindex = []
        print u"文字列：1　整数：2"
        for index,value in enumerate(self.Taplename):

            if value == "@end":
                break

            print value + u":の型 >> "

            suu = input()

            if suu == 1:
                tapleindex.append("varchar(50)")
            elif suu == 2:
                tapleindex.append("integer")
            else:
                pass

        self.Tapleindex = tapleindex

    def SQLAdd(self):
        sql = "CREATE TABLE "
        sql = sql + self.Tablename + " ("

        for index,value in enumerate(self.Taplename):
            if value == "@end":
                break
            else:
                if index != 0:
                    sql = sql + ","
                sql = sql + value + " "
                sql = sql + str(self.Tapleindex[index])

        sql = sql + ");"

        self.sql = sql

if __name__ == "__main__":

    #データベースファイル読み込みor作成
    connector = sqlite3.connect("sqlite_practice1.db")

    #カーソルの作成
    cur = connector.cursor()

    #テーブルの作成プログラム


    #cur.execute(sql)

    #情報追加
    #cur.executemany(u"INSERT INTO 言語 VALUES(?,?)",
    #[("1",u"パイソン","2",u"C言語","3",u"JAVA","4",u"javascript","5",u"Ruby")])

    aa = cur.execute(u"SELECT * FROM 言語")

    for i in aa:
        print i

    #終了の儀式
    connector.commit()
    connector.close()
