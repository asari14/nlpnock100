"""
16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．
同様の処理をsplitコマンドで実現せよ．

[Ref]
https://nlp100.github.io/ja/ch02.html

[Unix]
"""

import sys

N = int(sys.argv[1])

with open("inputs/popular-names.txt", encoding="utf-8") as file:
    Lines = file.readlines()

    for line in range(0, len(Lines), N):
        print(int(len(Lines)/N))
        print(Lines[line * int(len(Lines)/N):line])

    # for line in Lines:
    #     print(line.rstrip())
