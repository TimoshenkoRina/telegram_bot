import requests

def pars(url):
    url = f'{url}'
    s = requests.Session()
    r = s.get(url, allow_redirects=True)
    r.encoding = 'utf-8'
    table = r.text.lower()
    return table


url='https://docs.google.com/spreadsheets/d/1hHUUdHhO7uMSr-kFrAed1NVeA2vD-2NNVqyJQCJ2X9w/export?format=csv&id=1hHUUdHhO7uMSr-kFrAed1NVeA2vD-2NNVqyJQCJ2X9w&gid=474547065'
table=pars(url)
print (table)

def irr(table):
    lastname = input()
    if not lastname:
        return 'Пользователь не авторизован'
    for line in table.split('\n'):
        if lastname in line:
            try:
                line=line.split(',')
                return line[-1]
            except (IndexError, ValueError):
                return 'Ошибка обработки данных'
    return 'ты не в этой группе'

print (irr(pars(url)))

