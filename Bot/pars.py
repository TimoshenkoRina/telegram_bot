import requests
from config import url

def get_url(subject):
    return url.get(subject)

def pars(url: str):
    try:
        s = requests.Session()
        r = s.get(url, allow_redirects=True, timeout=10)
        r.encoding = 'utf-8'
        return r.text.lower()
    except requests.RequestException:
        return ""

def english(table: str, chatid: int, users: dict):
    lastname = users.get(chatid, {}).get('name', '')
    if not lastname:
        return 'Пользователь не авторизован'
    for line in table.split('\n'):
        if lastname in line:
            try:
                line = line.split(',')
                return line[-1]
            except (IndexError, ValueError):
                return 'Ошибка обработки данных'
    return 'ты не в этой группе'

def history(table: str, chatid: int, users: dict):
    lastname = users.get(chatid, {}).get('name', '')
    if not lastname:
        return 'Пользователь не авторизован'
    for line in table.split('\n'):
        if lastname in line:
            parts = line.split(',')
            return parts[-2] if len(parts) >= 2 else 'Ошибка данных'
    return 'ты не в этой группе'

def irr(table: str, chatid: int, users: dict):
    lastname = users.get(chatid, {}).get('name', '')
    if not lastname:
        return 'Пользователь не авторизован'
    for line in table.split('\n'):
        if lastname in line:
            total = 0
            for item in line.split(','):
                clean_item = item.replace('.', '').replace('-', '')
                if clean_item.isdigit():
                    try:
                        total += int(item)
                    except ValueError:
                        continue
            return total
    return 'ты не в этой группе'

def irs(table: str, chatid: int, users: dict):
    lastname = users.get(chatid, {}).get('name', '')
    if not lastname:
        return 'Пользователь не авторизован'
    table = table.replace('сул́има', 'сулима').replace('и́онова', 'ионова')
    for line in table.split('\n'):
        if lastname in line:
            parts = [x for x in line.split(',') if x != 'н']
            try:
                return sum(int(x) for x in parts[1:-1])
            except ValueError:
                return 'Ошибка данных'
    return 'ты не в этой группе'

def org(table: str, chatid: int, users: dict):
    lastname = users.get(chatid, {}).get('name', '')
    if not lastname:
        return 'Пользователь не авторизован'
    for line in table.split('\n'):
        if lastname in line:
            try:
                line = line[12:]
                parts = line.split(',')
                return int(parts[9]) + int(parts[10])
            except (IndexError, ValueError):
                return 'Ошибка данных'
    return 'ты не в этой группе'

def menegment(table: str, chatid: int, users: dict):
    lastname = users.get(chatid, {}).get('name', '')
    if not lastname:
        return 'Пользователь не авторизован'
    for line in table.split('\n'):
        if lastname in line:
            try:
                parts = line.split('"')
                flat = str(parts)
                flat_parts = flat.split(',')
                return flat_parts[-2].strip()
            except IndexError:
                return 'Ошибка данных'
    return 'ты не в этой группе'
