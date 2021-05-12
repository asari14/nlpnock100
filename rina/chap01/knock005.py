"""
05. n-gram
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．

[Ref]
https://nlp100.github.io/ja/ch01.html
"""

sentence = "I am an NLPer"


def word_n_gram(sentence, step):
    words = sentence.split()
    result = []

    for i in range(len(words) - step + 1):
        result.append(words[i: i + step])
    return result


print(word_n_gram(sentence, step=2))
print(word_n_gram(sentence, step=3))


def char_n_gram(sentence, step):
    words = sentence.split()
    chars = "".join(words)
    result = []

    for i in range(len(chars) - step + 1):
        result.append(chars[i: i + step])
    return result


print(char_n_gram(sentence, step=2))
print(char_n_gram(sentence, step=3))
