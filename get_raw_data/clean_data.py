import re
import csv


def read_triples(file_name):
    relations = []
    with open(file_name, 'r', encoding='utf-8') as f:
        line_count = 0
        data = csv.reader(f)
        for row in data:
            if line_count == 0:
                line_count += 1
            else:
                relations.append([row[0],row[3],row[1]])
    return relations


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


def clean_e(s):
    re_entities = []
    if '/' in s:
        re_entities.append(s.split('/')[1])
    elif '|' in s:
        re_entities = s.split('|')
    else:
        re_entities.append(s)
    return re_entities


def read_relations(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.readlines()
    relations = []
    for row in data:
        d = row.strip().split()
        relations.append(d)
    return relations


def read_entities(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.readlines()
    entities = []
    for row in data:
        e = row.strip().split()
        entities.append(e)
    return entities


clean_entities = []
copy_relations = []

clean_relations = read_triples('triples.csv')
# print(triples)

for item in clean_relations:
    clean_entities.append(item[0])
    clean_entities.append(item[2])

entities1 = read_entities('entities_fandom.txt')
entities2 = read_entities('entities_wiki.txt')

for item in entities1 + entities2:
    cleaned = clean_e(item[0])
    if len(cleaned) == 1:
        clean_entities.append(cleaned[0])
    else:
        for m in cleaned:
            clean_entities.append(m)

clean_entities = sorted(list(set(clean_entities)))
with open('entities_clean.txt', 'w', encoding='utf-8') as f:
    for r in clean_entities:
        f.write(r.strip() + '\n')

relations = read_relations('relations.txt')
for d in relations:
    # print(d[-1])
    # if len(d) != 3: continue
    if d[-1][-1] == ')':
        copy_relations.append(d)
        d[-1] = d[-1][:d[-1].index('(')]
    # 存在中文括号
    if d[-1][-1] == '）':
        d[-1].replace('（', '(')
        d[-1].replace('）', ')')
        copy_relations.append(d)
        d[-1] = d[-1][:d[-1].index('（')]
    clean_relations.append(d)

print(clean_relations)
with open('relations_clean.txt', 'w', encoding='utf-8') as f:
    for r in clean_relations:
        f.write('%s\t%s\t%s\n' % (r[0], r[1], r[2]))

with open('relations_copy.txt', 'w', encoding='utf-8') as f:
    for r in copy_relations:
        f.write('%s\t%s\t%s\n' % (r[0], r[1], r[2]))
