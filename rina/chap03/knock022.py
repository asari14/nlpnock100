"""
22. カテゴリ名の抽出
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

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

lines = text.split("\n")

for line in lines:
    if "Category" in line:
        t = re.search(r'^\[\[Category:(.*?)(\|.*)*\]\]$', line)
        # .：改行以外の任意の一文字
        # *：直前のパターンを0回以上繰り返し
        # ?：直前のパターンを0回または1回以上繰り返し
        # []：文字の集合
        # \ ：or
        # ^：文字列の先頭
        # $：文字列の末尾
        # (.*?)：最短マッチ
        if t is not None:
            print(t.group(1))
