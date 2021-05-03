"""
02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

[Ref]
https://nlp100.github.io/ja/ch01.html
"""

str1 = "パトカー"
str2 = "タクシー"

print("".join(list(map(lambda idx: str1[idx] + str2[idx], [0, 1, 2, 3]))))
