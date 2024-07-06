import requests  # pip install requests
import csv
from bs4 import BeautifulSoup  # pip install bs4

# pip install lxml

count = 0
while True:
    url = f'https://manufacturers.ru/companies?cat=6899&page={count}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    data = requests.get(url, headers=headers).text
    block = BeautifulSoup(data, 'lxml')
    heads = block.find_all('div', class_='sim-right')
    print(len(heads))
    for i in heads:
        w = i.find_next('a').get('href')
        # print('https://manufacturers.ru'+w)
        get_url = ('https://manufacturers.ru' + w)
        bout = requests.get(get_url).text
        spon = BeautifulSoup(bout, 'lxml')
        head = spon.find('h1', class_='like-h1')
        print(head.text.strip())
        name = (head.text.strip())
        haract = spon.find('div', id='category').find_all('tr')
        print(' '.join(haract[0].text.strip().split()))
        categ_1 = (' '.join(haract[0].text.strip().split()))
        print(' '.join(haract[1].text.strip().split()))
        categ_2 = (' '.join(haract[1].text.strip().split()))
        print(' '.join(haract[2].text.strip().split()))
        categ_3 = (' '.join(haract[2].text.strip().split()))
        try:
            params = spon.find('div', id='company').find_all('tr')
        except Exception:
            continue
        try:
            print(' '.join(params[0].text.strip().split()))
            param_1 = (' '.join(params[0].text.strip().split()))
            print(' '.join(params[1].text.strip().split()))
            param_2 = (' '.join(params[1].text.strip().split()))
        except:
            param_1 = 'None'
            param_2 = 'None'
            print('None')

        try:
            print(' '.join(params[2].text.strip().split()))
            param_3 = (' '.join(params[2].text.strip().split()))
        except:
            param_3 = 'None'
            print('None')
        try:
            print(' '.join(params[3].text.strip().split()))
            param_4 = (' '.join(params[3].text.strip().split()))
        except:
            param_4 = 'None'
            print('None')
        try:
            print(' '.join(params[4].text.strip().split()))
            param_5 = (' '.join(params[4].text.strip().split()))
        except:
            param_5 = 'None'
            print('None')
        contacts = spon.find('div', id='contact-list').find_all('tr')
        try:
            print(' '.join(contacts[0].text.strip().split()))
            cont_1 = (' '.join(contacts[0].text.strip().split()))
        except:
            cont_1 = 'none'
            print('None')
        try:
            print(' '.join(contacts[1].text.strip().split()))
            cont_2 = (' '.join(contacts[1].text.strip().split()))
        except:
            cont_2 = 'None'
            print('None')
        try:
            print(' '.join(contacts[2].text.strip().split()))
            cont_3 = (' '.join(contacts[2].text.strip().split()))
        except:
            cont_3 = 'None'
            print('None')
        try:
            print(' '.join(contacts[3].text.strip().split()))
            cont_4 = (' '.join(contacts[3].text.strip().split()))
        except:
            cont_4 = 'None'
            print('None')
        print('\n')

        storage = {'name': name, 'categ_1': categ_1, 'categ_2': categ_2, 'categ_3': categ_3, 'param_1': param_1,
                   'param_2': param_2, 'param_3': param_3, 'param_4': param_4, 'param_5': param_5, 'cont_1': cont_1,
                   'cont_2': cont_2, 'cont_3': cont_3, 'cont_4': cont_4}

        with open('medicine.csv', 'a+', encoding='utf-16') as file:
            pisar = csv.writer(file, delimiter=';', lineterminator='\r')
            pisar.writerow(
                [storage['name'], storage['categ_1'], storage['categ_2'], storage['categ_3'], storage['param_1'],
                 storage['param_2'], storage['param_3'], storage['param_4'], storage['param_5'], storage['cont_1'],
                 storage['cont_2'], storage['cont_3'], storage['cont_4']])
    count += 1
