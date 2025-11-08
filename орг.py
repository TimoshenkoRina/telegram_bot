import requests

def pars(url):
    url = f'{url}'
    s = requests.Session()
    r = s.get(url, allow_redirects=True)
    r.encoding = 'utf-8'
    table = r.text.lower()
    return table


url ='https://docs.google.com/spreadsheets/d/1unVwdDM0pBJEUeO6tCCZowzM8at2Db4HCVz_8zpEJms/export?format=csv&id=1unVwdDM0pBJEUeO6tCCZowzM8at2Db4HCVz_8zpEJms&gid=0'
table=pars(url)
print (table)

def irr(table):
    lastname = input()
    if not lastname:
        return 'Пользователь не авторизован'
    for line in table.split('\n'):
        if lastname in line:
            try:
                if '"' in line:
                    line=line.split('"')
                    res=line[-2]
                else:
                    line=line.split(',')
                    res=line[-2]
                return res

            except (IndexError, ValueError):
                return 'Ошибка обработки данных'
    return 'ты не в этой группе'

print (irr(pars(url)))

