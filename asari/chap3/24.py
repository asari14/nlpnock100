pattern = r'\[\[ファイル:(.+?)\|'
#resultに結合
#re.findall=全部を検索して一致するもののみ抽出
result = '\n'.join(re.findall(pattern, text_uk))
print(result)
