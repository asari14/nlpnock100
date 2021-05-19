"""
13. col1.txtとcol2.txtをマージ
12で作ったcol1.txtとcol2.txtを結合し，
元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
確認にはpasteコマンドを用いよ．

[Ref]
https://nlp100.github.io/ja/ch02.html

[Unix]
"""

col1s = []
col2s = []


with open("outputs/knock012/col1.txt", encoding="utf-8") as col1:
    for line in col1:
        col1s.append(line.rstrip())

with open("outputs/knock012/col2.txt", encoding="utf-8") as col2:
    for line in col2:
        col2s.append(line.rstrip())

with open("outputs/knock012/col1_col2.txt", "w") as new_txt:
    for i in range(len(col1s)):
        new_txt.write(f"{col1s[i]}\t{col2s[i]}\n")
