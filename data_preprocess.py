import json
import requests
from bs4 import BeautifulSoup as bs
import time


# from urllib3 import PoolManager
# manager = PoolManager(10)


def load_json(file):
    data = {}
    with open(file) as json_file:
        data = json.load(json_file)
    return data


def dump_json(data, file):
    with open(file, 'w') as outfile:
        json.dump(data, outfile)


def get_text_bs(html):
    tree = bs(html, 'lxml')

    body = tree.body
    if body is None:
        return None

    for tag in body.select('script'):
        tag.decompose()
    for tag in body.select('style'):
        tag.decompose()

    text = body.get_text(separator='\n')

    return text


def get_text(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    # r = manager.request('GET', url, headers=headers)
    r = requests.get(url, headers=headers)
    soup = bs(r.text, "lxml")
    text = ''
    for hit in soup.findAll(attrs={'class': "content-list-component yr-content-list-text text"}):
        text += ' ' + hit.text
    r.close()
    return text

def get_text2(url):
    print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    # r = manager.request('GET', url, headers=headers)
    r = requests.get(url, headers=headers)
    soup = bs(r.text, "lxml")
    text = ''
    for hit in soup.findAll(attrs={'class': "primary-cli cli cli-text"}):
        text += ' ' + hit.text
    for hit in soup.findAll(attrs={'class': "primary-cli cli cli-text "}):
        text += ' ' + hit.text
    r.close()
    print(text)
    return text


def get_text3(url):
    print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    # r = manager.request('GET', url, headers=headers)
    r = requests.get(url, headers=headers)
    soup = bs(r.text, "lxml")
    text = ''
    for hit in soup.findAll(attrs={'class': "primary-cli cli cli-text "}):
        text += ' ' + hit.text
    r.close()
    print(text)
    return text

'''
# five_news_category = {"COMEDY": [], "BUSINESS": [], "FOOD & DRINK": [], "HEALTHY LIVING": [], "SPORTS": []}
# 30170 30235 55811 56876
processed_count = 0
count = 0
for line in open('News_Category_Dataset_v2.json', 'r'):
    if count <= processed_count:
        count += 1
        continue
    doc_dict = json.loads(line)
    doc_category = doc_dict['category']
    print(doc_category)
    if doc_category in ["FOOD & DRINK"]:
        #["COMEDY", "BUSINESS", "FOOD & DRINK", "HEALTHY LIVING", "SPORTS"]:
        # for i in range(10000):
        try:
            #if doc_category == "FOOD & DRINK":
            doc_dict['text'] = get_text2(doc_dict['link'])
            #elif doc_category == "HEALTHY LIVING":
            #    doc_dict['text'] = get_text3(doc_dict['link'])
            #else:
            #    doc_dict['text'] = get_text(doc_dict['link'])
        except:
            with open("falied docs2.txt", 'a+') as f:
                f.write(str(count) + '\n')
        doc_str = json.dumps(doc_dict)
        with open('{}.json'.format(doc_category), 'a+') as f:
            f.write(doc_str + '\n')
    count += 1
    print(count)

'''
five_categories_dict = {"COMEDY": [],
                        "BUSINESS": [],
                        "FOOD & DRINK": [],
                        "HEALTHY LIVING": [],
                        "SPORTS": []}

for k in five_categories_dict:
    for doc in open("{}.json".format(k), 'r'):
        tmp = json.loads(doc)
        if 'text' in tmp and len(tmp['text']) > 10:
            five_categories_dict[k].append(doc)

dump_json(five_categories_dict, "five_categories.json")

