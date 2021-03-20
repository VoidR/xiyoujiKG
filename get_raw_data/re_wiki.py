import re

file_name = './wiki.txt'
entities = []

with open(file_name, 'r', encoding='utf-8') as f:
    data = f.readlines()
    patt1 = '\S\[\[(.*?)\]\]'  # 匹配'[[*]]
    # patt2 = ';([\u4e00-\u9fa5]+)'# 匹配;*
    patt2 = ';([\u4e00-\u9fa5、]+)'  # 匹配;*、
    for row in data:
        regex = re.compile(patt1)
        results = regex.findall(row)
        for item in results:
            entities.append(item)

        regex1 = re.compile(patt2)
        results1 = regex1.findall(row)
        if len(results1):
            if len(results1[0].split('、')) > 1:
                for mm in results1[0].split('、'):
                    entities.append(mm)
            else:
                for item in results1:
                    entities.append(item)
    print(entities)

with open('entities_wiki.txt', 'w', encoding='utf-8') as f:
    for t in entities:
        f.write(t.strip() + '\n')
