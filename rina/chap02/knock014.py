"""
14. 先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．
確認にはheadコマンドを用いよ．

[Ref]
https://nlp100.github.io/ja/ch02.html

[Unix]
"""

import sys

N = int(sys.argv[1])

with open("inputs/popular-names.txt", encoding="utf-8") as file:
    Lines = file.readlines()[0:N]
    for line in Lines:
        print(line.rstrip())
