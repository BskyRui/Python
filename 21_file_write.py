with open('./data.txt', 'w', encoding='utf8') as fd:
    fd.write('hello')

# 追加
with open('./data.txt', 'a', encoding='utf8') as fd:
    fd.write('222')