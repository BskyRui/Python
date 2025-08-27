import json

with open('./data.json', 'r', encoding='utf8') as json_file:
    data = json.load(json_file)
    print(data)   # json.load() for file, json.loads() for string

    

with open('./data.json', 'w', encoding='utf8') as json_w:
    data['age'] = 23
    json.dump(data, json_w, ensure_ascii=False)
