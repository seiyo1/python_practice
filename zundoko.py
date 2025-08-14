import random


zundoko_bushi = ''
# 以下に処理を記述します
while 1:
    zundoko_bushi += random.choice(['ズン','ドコ'])
    if zundoko_bushi[-10:] == "ズンズンズンズンドコ":
        zundoko_bushi += "ア・キ・ラ！"
        break

# 表示
print(zundoko_bushi)
