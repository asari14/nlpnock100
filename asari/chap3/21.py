import re

#正規表現パターンでコンパイル→search()で使えるようにする
pattern = re.compile('Category')
wiki = pd.read_json('jawiki-country.json', lines = True)
uk = wiki[wiki['title']=='イギリス'].text.values
#split('\n')→改行
ab = uk[0].split('\n')
for line in ab:
    if re.search(pattern, line):
        print (line)
