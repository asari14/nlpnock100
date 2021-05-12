"""
15. 末尾のN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．
確認にはtailコマンドを用いよ．

[Ref]
https://nlp100.github.io/ja/ch02.html

[Unix]
"""

import sys

N = int(sys.argv[1])

with open("inputs/popular-names.txt", encoding="utf-8") as file:
    Lines = file.readlines()[-(N+1):-1]
    for line in Lines:
        print(line.rstrip())
