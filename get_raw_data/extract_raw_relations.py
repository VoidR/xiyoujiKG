from bs4 import BeautifulSoup
import requests
import re
import time

root = 'https://xiyouji.fandom.com/zh/wiki/'


def clean_string(s):
    s = re.sub(r'\[\d*\]', '', s)
    return s


def extract_entity(ent):
    url = root + ent
    response = requests.get(url=url).content
    soup = BeautifulSoup(response, 'html.parser')
    e1 = ent
    relations = []
    for p in soup.find_all('h2', class_='pi-item pi-header pi-secondary-font pi-item-spacing pi-secondary-background'):
        if p.text == '人物关系':
            # print("成功找到")
            temp = 0
            for np in p.next_siblings:
                temp += 1
                if temp & 1:
                    continue
                r = np.find_all('h3')[0].text
                m = np.find_all('div')[0].text
                members = m.split('、')
                if len(m.split('、')) > 1:
                    for mm in m.split('、'):
                        relations.append((e1, r, mm))
                else:
                    relations.append((e1, r, m))
    print(relations)
    # relations = [(e1, r[0], r[1]) for r in relations]
    return relations


time_start = time.time()

all_relations = set()

with open('entities_fandom.txt', 'r', encoding='utf-8') as f:
    ents = [e.strip() for e in f.readlines()]
    for e in ents:
        print('processing', e)
        relations = extract_entity(e)
        for r in relations:
            all_relations.add(r)

all_relations = sorted(list(all_relations))
with open('relations.txt', 'w', encoding='utf-8') as f:
    for r in all_relations:
        f.write('%s\t%s\t%s\n' % (r[0], r[1], r[2]))

time_end = time.time()
print('totally cost', time_end - time_start)
