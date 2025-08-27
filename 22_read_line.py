with open('./data.txt', 'r', encoding='utf8') as fd:
    while True:
        l = fd.readline()
        if l == "": # EOF return ""
            break 
        else:
            print(l, end = "") # 去掉默认的回车