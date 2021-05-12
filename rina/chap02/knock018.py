"""
18. 各行を3コラム目の数値の降順にソート
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．

[Ref]
https://nlp100.github.io/ja/ch02.html

[Unix]
"""
from operator import itemgetter, attrgetter


Lines = []
with open("inputs/popular-names.txt", encoding="utf-8") as file:
    for line in file:
        Lines.append(tuple(line.rstrip().split("	")))


for line in sorted(Lines, key=itemgetter(2), reverse=False):
    print(list(line))


#  三つ目のタプル数値にできてない
