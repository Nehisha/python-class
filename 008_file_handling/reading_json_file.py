import json

content = '{"name :": "nehisha","age :": 20,"city :": "Pokhara"}'
content_ko_dictionary = json.loads(content)
print(content_ko_dictionary)

pair = content_ko_dictionary.items()
print(pair) 

for key, value in pair:
    print(key, value)
