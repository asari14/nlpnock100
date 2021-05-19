"""
24. ファイル参照の抽出
記事から参照されているメディアファイルをすべて抜き出せ．

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
    t = re.search(r'{{(.*?)}}', i)

    if t is not None:
        print(t.group(1))
