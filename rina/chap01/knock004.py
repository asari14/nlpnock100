"""
04. 元素記号
"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭の2文字を取り出し，
取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．

[Ref]
https://nlp100.github.io/ja/ch01.html
"""

import re

string = re.sub(
    "[,\.]", "", "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.")

arr = string.split(" ")

acc = {}


def calc(idx):
    if idx in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        acc[idx] = arr[idx][0]
    else:
        acc[idx] = arr[idx][0]


for i in range(len(arr)):
    calc(i)

print(acc)
