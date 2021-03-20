from requests_html import HTMLSession


root = 'https://www.wiki-wiki.top/baike-%E8%A5%BF%E6%B8%B8%E8%AE%B0%E8%A7%92%E8%89%B2%E5%88%97%E8%A1%A8'

all_entities = []

print('visiting...')
url = root
session = HTMLSession()
response = session.get(url)
output = response.html.find('div.mw-parser-output',first=True)
print(output.text)
a_list = response.html.find('dt')

    # cur_ents = []
    # for a in a_list:
    #     if a.attrs.get('class', '') == ('category-page__member-link', ):
    #         cur_ents.append(a.attrs['title'])
    # for t in cur_ents:
    #     if 'Template' in t: continue
    #     if 'Category' in t:
    #         if t not in have_seen_categories:
    #             current_category.append(t)
    #             have_seen_categories.add(t)
    #     else:
    #         all_entities.append(t)

all_entities = sorted(list(set(all_entities)))
with open('entities_wiki1.txt', 'w', encoding='utf-8') as f:
    for t in all_entities:
        f.write(t.strip() + '\n')
