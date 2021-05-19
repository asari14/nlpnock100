"""
21. カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ．

[Ref]
https://nlp100.github.io/ja/ch03.html
"""

import json

text = ""
with open('inputs/jawiki-country.json') as file:
    for i in file:
        dic = json.loads(i)

        if dic["title"] == "イギリス":
            text = dic["text"]

lists = text.split("\n")

for i in lists:
    if "Category" in i:
        print(i)
