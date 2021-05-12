"""
06. 集合
“paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，
それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．

[Ref]
https://nlp100.github.io/ja/ch01.html
"""

x1 = "paraparaparadise"
y1 = "paragraph"


def n_gram(sentence, step):
    result = {}

    for i in range(len(sentence) - step + 1):
        if sentence[i: i+step] in result:
            result[sentence[i: i+step]] += 1
        else:
            result[sentence[i: i+step]] = 1

    return result


X = n_gram(x1, step=2)
Y = n_gram(y1, step=2)

print(X)
# {'pa': 3, 'ar': 3, 'ra': 3, 'ap': 2, 'ad': 1, 'di': 1, 'is': 1, 'se': 1}
print(Y)
# {'pa': 1, 'ar': 1, 'ra': 2, 'ag': 1, 'gr': 1, 'ap': 1, 'ph': 1}


def union(X, Y):

    dict_union = X.copy()

    for key, count in Y.items():
        if key in X:
            dict_union[key] += count
        else:
            dict_union[key] = count

    return dict_union


print(union(X, Y))
# {'pa': 4, 'ar': 4, 'ra': 5, 'ap': 3, 'ad': 1, 'di': 1, 'is': 1, 'se': 1, 'ag': 1, 'gr': 1, 'ph': 1}


def intersection(X, Y):
    dict_is = {}

    for key, count in Y.items():
        if key in X:
            dict_is[key] = count + X[key]

    return dict_is


print(intersection(X, Y))
# {'pa': 4, 'ar': 4, 'ra': 5, 'ap': 3}


def difference_set(X, Y):
    dict_ds = X.copy()

    for key, _ in Y.items():
        if key in X:
            del dict_ds[key]

    return dict_ds


print(difference_set(X, Y))
# {'ad': 1, 'di': 1, 'is': 1, 'se': 1}

print(difference_set(Y, X))
# {'ag': 1, 'gr': 1, 'ph': 1}
