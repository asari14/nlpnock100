#07テンプレートによる文生成
#引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y=”気温”, z=22.4として，実行結果を確認せよ．

def a(x, y, z):
  print(f'{x}時のとき{y}は{z}')

a(12, '気温', 22.4)

#08暗号文
#与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
#英小文字ならば(219 - 文字コード)の文字に置換その他の文字はそのまま出力この関数を用い，英語のメッセージを暗号化・復号化せよ．

#str=数値を文字列に置き換える機能
#rep=繰り返し処理をfor文よりも完結に書くための関数
#ord=Unicodeポイントをord関数を使用して取得し、出力する関数
def cipher(str):
  rep = [chr(219 - ord(x)) if x.islower() else x for x in str]

  return ''.join(rep)

message = 'NLP 100 exercise'
message = cipher(message)
#繰り返し処理なので奇数回は暗号、偶数回は複合化される
print('暗号', message)
message = cipher(message)
print('復号', message)
message = cipher(message)

#09Typoglycemia

import random
s = 'I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'
ans = []
#単語ごとに分割
text = s.split()

for word in text:
    #len=要素数の習得
    if (len(word)>4):
        #mid = list(word[開始インデックス:終了インデックス])
        mid = list(word[1:-1])
        random.shuffle(mid)
        word = word[0] + ''.join(mid) + word[-1]
        ans.append(word)
    else:
        ans.append(word)
print (' '.join(ans))

#10行数のカウント

import pandas as pd

#sep='\t'=タブ区切り
df = pd.read_table('popular-names.txt', header=None, sep='\t')
print(len(df))

#11タブをスペースに変換
with open('popular-names.txt', "r") as f:
    # 一行ずつ読み込む
    for data in f:
        #タブを空白へ置換
        #データ名.strip()で空白除去
        print(data.strip().replace("\t"," "))

#12 1列目をcol.txtに、2列目をcol2.txtに保存

with open('popular-names.txt', "r") as r:
            with open("col1.txt", "w") as w1:
            with open("col2.txt", "w") as w2:
              #一行ずつ読み込む
            　for data in r:
                　#タブ区切り、文字で配列化
                  col = data.strip().split("\t")
                  w1.writelines(col[0] + "\n")
                  w2.writelines(col[1] + "\n")

#13col1.txtとcol2.txtをマージ
df1 = pd.read_csv('col1.txt', delimiter='\t', header=None)
df2 = pd.read_csv('col2.txt', delimiter='\t', header=None)
df = pd.concat([df1, df2], axis=1)
df.to_csv('col1_2.txt', sep='\t',header=False, index=False)

#14 先頭からN列を出力
def output_head(N):
  print(df.head(N))

output_head(5)

#15 末尾のN行を出力
def output_tail(N):
  print(df.tail(N))

output_tail(5)


#18各行を3コラム目の数値の降順にソート
import pandas as pd
df = pd.read_csv('popular-names.txt', delimiter='\t', header=None)
#デフォルトが昇順なので降順にするときはascending=False
new = df[2].sort_values(ascending=False)
print (new)

#19各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
df = pd.read_csv('popular-names.txt', delimiter='\t', header=None)
vc = df[0].value_counts()
vc = pd.DataFrame(vc)
vc = vc.reset_index()
vc.columns = ['name','count']
vc = vc.sort_values(['count','name'],ascending=[False,False])
print (vc)
