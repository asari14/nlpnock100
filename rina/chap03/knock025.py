"""
25. テンプレートの抽出
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．

[Ref]
https://nlp100.github.io/ja/ch03.html
"""

import json
import re

text = ""
with open('inputs/jawiki-country.json') as f:
    for i in f:
        dic = json.loads(i)
        if dic["title"] == "イギリス":
            text = dic["text"]


lists = text.split("\n")

for i in lists:
    t = re.search(r'^{{基礎情報 (.*?)}}$', i)

    if t is not None:
        print(t)

# .：改行以外の任意の一文字
# *：直前のパターンを0回以上繰り返し
# ?：直前のパターンを0回または1回以上繰り返し
# []：文字の集合
# \ ：or
# ^：文字列の先頭
# $：文字列の末尾
# (.*?)：最短マッチ
