# -*- coding: utf-8 -*-
hana = input("誕生月を入力：")
print str(hana)+u"月"
color = [u"江戸桜色",u"紫峰菫色（しほうすみれいろ）",u"空色",u"白椿色",u"蓬色（よもぎいろ）",u"水色",u"薔薇色",u"朱色",u"葡萄色",u"撫子色",u"蜜柑色",u"汐色（うしおいろ）"]

for month in range(12):
    if (hana == month+1):
        print u"あなたの誕生色は"+color[month]+u"です"
        break
        
