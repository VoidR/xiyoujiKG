import re


#def clean_entites():


def clean_r(s):
    s = re.sub(r'\(', '', s)
    s = re.sub(r'\)', '', s)
    s = re.sub(r'\[', '', s)
    s = re.sub(r'\]', '', s)
    s = re.sub(r'\d+', '', s)
    s = re.sub(r'†', '', s)
    if '/' in s:
        s = s.split('/')[0]
    if '，' in s:
        s = s.split('，')[0]
    return s


def read_relations(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.readlines()
    relations = []
    for row in data:
        d = row.strip().split()
        relations.append(d)
    return relations


relations = read_relations('relations.txt')
clean_relations = []
for d in relations:
    if len(d) != 3: continue
    if d[-1][0] == '(' and d[-1][-1] == ')': continue
    if d[-1] == '-': continue
    d[1] = clean_r(d[1])
    if d[1] == '可能': continue
    clean_relations.append(d)


with open('relations_clean.txt', 'w', encoding='utf-8') as f:
    for r in clean_relations:
        f.write('%s\t%s\t%s\n' % (r[0], r[1], r[2]))

