import requests
#
# def pars(url):
#     url = f'{url}'
#     s = requests.Session()
#     r = s.get(url, allow_redirects=True)
#     r.encoding = 'utf-8'
#     table = r.text.lower()
#     return table
#
#
# url='https://docs.google.com/spreadsheets/d/1hHUUdHhO7uMSr-kFrAed1NVeA2vD-2NNVqyJQCJ2X9w/export?format=csv&id=1hHUUdHhO7uMSr-kFrAed1NVeA2vD-2NNVqyJQCJ2X9w&gid=474547065'
# table=pars(url)
# # print (table)
#
# def irr(table):
#     lastname = input()
#     for a in table.split('\n'):
#         if lastname in a:
#
#             a = a[6:]
#             a = a.split('"')
#             s1 = float(a[0].count('1'))
#             s2 = float(a[1].replace(',', '.'))
#             s3 = float((a[-1].split(',')[-2]).replace(',', '.'))
#
#             return s1 + s2 + s3
#
#     return 'ты не в этой группе'
#
# print (irr(pars(url)))
#


url = {'ОРГ 1.2': 'https://docs.google.com/spreadsheets/d/1XQpCvLT5Nf-aQ8Mz-3VYDw0uyk-8QVKv98gLKSEQg9A/export?format=csv&id=1XQpCvLT5Nf-aQ8Mz-3VYDw0uyk-8QVKv98gLKSEQg9A&gid=0',
       'ОРГ 2.3': 'https://docs.google.com/spreadsheets/d/1DTkjRozRpijVK0Je9iZjLkpvbLAA-l6-WGnktJGlraU/export?format=csv&id=1DTkjRozRpijVK0Je9iZjLkpvbLAA-l6-WGnktJGlraU&gid=0',
       'ОРГ 2.1': 'https://docs.google.com/spreadsheets/d/1q9spgoTIUEbpwTqBuY5ml-Q5tSmDpuHTMx2QJnIZIBk/export?format=csv&id=1q9spgoTIUEbpwTqBuY5ml-Q5tSmDpuHTMx2QJnIZIBk&gid=0',

       'история россии и мира 8:10 Павловская':'https://docs.google.com/spreadsheets/d/1re6oAKcCWZPF1clxEKoffyu3zZgTiSQ5Zq-YAo0vzrI/export?format=csv&id=1re6oAKcCWZPF1clxEKoffyu3zZgTiSQ5Zq-YAo0vzrI&gid=132554553',
       'история россии и мира 8:10 Пригодич':'https://docs.google.com/spreadsheets/d/1re6oAKcCWZPF1clxEKoffyu3zZgTiSQ5Zq-YAo0vzrI/export?format=csv&id=1re6oAKcCWZPF1clxEKoffyu3zZgTiSQ5Zq-YAo0vzrI&gid=0',
       'история россии и мира 11:30 Пригодич':'https://docs.google.com/spreadsheets/d/1re6oAKcCWZPF1clxEKoffyu3zZgTiSQ5Zq-YAo0vzrI/export?format=csv&id=1re6oAKcCWZPF1clxEKoffyu3zZgTiSQ5Zq-YAo0vzrI&gid=1821313907',
       'история россии и мира 15:30 Пригодич':'https://docs.google.com/spreadsheets/d/1re6oAKcCWZPF1clxEKoffyu3zZgTiSQ5Zq-YAo0vzrI/export?format=csv&id=1re6oAKcCWZPF1clxEKoffyu3zZgTiSQ5Zq-YAo0vzrI&gid=605593543',
       'история россии и мира 9:50 Павловская':'https://docs.google.com/spreadsheets/d/1re6oAKcCWZPF1clxEKoffyu3zZgTiSQ5Zq-YAo0vzrI/export?format=csv&id=1re6oAKcCWZPF1clxEKoffyu3zZgTiSQ5Zq-YAo0vzrI&gid=669992992',
       'история россии и мира 11:30 Павловская':'https://docs.google.com/spreadsheets/d/1re6oAKcCWZPF1clxEKoffyu3zZgTiSQ5Zq-YAo0vzrI/export?format=csv&id=1re6oAKcCWZPF1clxEKoffyu3zZgTiSQ5Zq-YAo0vzrI&gid=517652382',
       'история россии и мира 13:30 Павловская':'https://docs.google.com/spreadsheets/d/1re6oAKcCWZPF1clxEKoffyu3zZgTiSQ5Zq-YAo0vzrI/export?format=csv&id=1re6oAKcCWZPF1clxEKoffyu3zZgTiSQ5Zq-YAo0vzrI&gid=332322934',
       'история россии и мира 15:30 Павловская':'https://docs.google.com/spreadsheets/d/1re6oAKcCWZPF1clxEKoffyu3zZgTiSQ5Zq-YAo0vzrI/export?format=csv&id=1re6oAKcCWZPF1clxEKoffyu3zZgTiSQ5Zq-YAo0vzrI&gid=1487346128',

       'история современных международных отношений 3.1': 'https://docs.google.com/spreadsheets/d/1ZnR6uFz1t_uCdMLAMYRPaT8CpsQB8ALK/export?format=csv&id=1ZnR6uFz1t_uCdMLAMYRPaT8CpsQB8ALK&gid=1753157777',

       'история реформ и реформаторов 3.2': 'https://docs.google.com/spreadsheets/d/1AVP0_usl0u4d1VJ-W9dY83Z9XDXrfklK_OlxNc3oEbU/export?format=csv&id=1AVP0_usl0u4d1VJ-W9dY83Z9XDXrfklK_OlxNc3oEbU&gid=0',

       'менеджмент 1.1':'https://docs.google.com/spreadsheets/d/1unVwdDM0pBJEUeO6tCCZowzM8at2Db4HCVz_8zpEJms/export?format=csv&id=1unVwdDM0pBJEUeO6tCCZowzM8at2Db4HCVz_8zpEJms&gid=0',
       'менеджмент 1.2':'https://docs.google.com/spreadsheets/d/1BVhEkOZ7Yp7AuVSLIYAg9al3FVcBepVG76z2hDqm7Pg/export?format=csv&id=1BVhEkOZ7Yp7AuVSLIYAg9al3FVcBepVG76z2hDqm7Pg&gid=0',
       'менеджмент 1.3':'https://docs.google.com/spreadsheets/d/1JS8C1dBMrIqDKV6Or_iaoSasA7wnG67xNs72nlGuXtE/export?format=csv&id=1JS8C1dBMrIqDKV6Or_iaoSasA7wnG67xNs72nlGuXtE&gid=0',
       'менеджмент 1.4':'https://docs.google.com/spreadsheets/d/1RO9Z8TonVmE01S67zwRZbNY0TbeE21Z8ZXY5RQmn71c/export?format=csv&id=1RO9Z8TonVmE01S67zwRZbNY0TbeE21Z8ZXY5RQmn71c&gid=0',
       'менеджмент 1.5':'https://docs.google.com/spreadsheets/d/1thf6a69OaRzbuxT76CQBgr1BGrQCq7OGy88ck3EBuaE/export?format=csv&id=1thf6a69OaRzbuxT76CQBgr1BGrQCq7OGy88ck3EBuaE&gid=0',

       'английский B1.2 7':'https://docs.google.com/spreadsheets/d/1hHUUdHhO7uMSr-kFrAed1NVeA2vD-2NNVqyJQCJ2X9w/export?format=csv&id=1hHUUdHhO7uMSr-kFrAed1NVeA2vD-2NNVqyJQCJ2X9w&gid=474547065',
       'английский A2 d4':'https://docs.google.com/spreadsheets/d/1XvdFQUgAZqOZ4onHpVUDGlw3jDKmhC_Gm7IV0cbPprE/export?format=csv&id=1XvdFQUgAZqOZ4onHpVUDGlw3jDKmhC_Gm7IV0cbPprE&gid=474547065'}

def get_url(subject):
    return url.get(subject)

def pars(url):
    url = f'{url}'
    s = requests.Session()
    r = s.get(url, allow_redirects=True)
    r.encoding = 'utf-8'
    table = r.text.lower()
    return table

print (type(get_url('ОРГ 1.2')), get_url('ОРГ 1.2'))