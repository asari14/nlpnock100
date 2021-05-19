#20
import json

filename = 'jawiki-country.json'
with open(filename, mode='r') as a:
  for line in a:
    line = json.loads(line)
    if line['title'] == 'イギリス':
      text_uk = line['text']
      break

print(text_uk)
