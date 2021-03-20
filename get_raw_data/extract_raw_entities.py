from requests_html import HTMLSession

seeds = ['Category:神仙',
         'Category:佛门神仙',
         'Category:主要角色',
         'Category:凡人',
         'Category:妖怪']


root = 'https://xiyouji.fandom.com/zh/wiki/'

all_entities = []
current_category = [x for x in seeds]
have_seen_categories = set([x for x in seeds])

while len(current_category) >= 1:
    seed = current_category.pop(0)
    print('visiting', seed)
    url = root + seed
    session = HTMLSession()
    response = session.get(url)
    a_list = response.html.find('a')
    cur_ents = []
    for a in a_list:
        if a.attrs.get('class', '') == ('category-page__member-link', ):
            cur_ents.append(a.attrs['title'])
    for t in cur_ents:
        if 'Template' in t: continue
        if 'Category' in t:
            if t not in have_seen_categories:
                current_category.append(t)
                have_seen_categories.add(t)
        else:
            all_entities.append(t)

all_entities = sorted(list(set(all_entities)))
with open('entities_fandom.txt', 'w', encoding='utf-8') as f:
    for t in all_entities:
        f.write(t.strip() + '\n')
