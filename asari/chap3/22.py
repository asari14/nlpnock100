wiki = pd.read_json('jawiki-country.json', lines = True)
uk = wiki[wiki['title']=='イギリス'].text.values
ls = uk[0].split('\n')
for line in ls:
    if re.search(pattern, line):
        line = line.replace('[[','').replace('Category:','').replace(']]','').replace('|*','').replace('|元','')
        print (line)
