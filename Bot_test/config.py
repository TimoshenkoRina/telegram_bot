TOKEN = '8325763973:AAFOr4FwgtZTrXATle2tkqYBms_W7WAASNo'

url = {'орг 1.2': 'https://docs.google.com/spreadsheets/d/1XQpCvLT5Nf-aQ8Mz-3VYDw0uyk-8QVKv98gLKSEQg9A/export?format=csv&id=1XQpCvLT5Nf-aQ8Mz-3VYDw0uyk-8QVKv98gLKSEQg9A&gid=0',
       'орг 2.3': 'https://docs.google.com/spreadsheets/d/1DTkjRozRpijVK0Je9iZjLkpvbLAA-l6-WGnktJGlraU/export?format=csv&id=1DTkjRozRpijVK0Je9iZjLkpvbLAA-l6-WGnktJGlraU&gid=0',
       'орг 2.1': 'https://docs.google.com/spreadsheets/d/1q9spgoTIUEbpwTqBuY5ml-Q5tSmDpuHTMx2QJnIZIBk/export?format=csv&id=1q9spgoTIUEbpwTqBuY5ml-Q5tSmDpuHTMx2QJnIZIBk&gid=0',

       'история россии и мира':'https://docs.google.com/spreadsheets/d/1re6oAKcCWZPF1clxEKoffyu3zZgTiSQ5Zq-YAo0vzrI/export?format=csv&id=1re6oAKcCWZPF1clxEKoffyu3zZgTiSQ5Zq-YAo0vzrI&gid=132554553',

       'история современные международные отношения': 'https://docs.google.com/spreadsheets/d/1ZnR6uFz1t_uCdMLAMYRPaT8CpsQB8ALK/export?format=csv&id=1ZnR6uFz1t_uCdMLAMYRPaT8CpsQB8ALK&gid=1753157777',

       'история реформы и реформаторы': 'https://docs.google.com/spreadsheets/d/1AVP0_usl0u4d1VJ-W9dY83Z9XDXrfklK_OlxNc3oEbU/export?format=csv&id=1AVP0_usl0u4d1VJ-W9dY83Z9XDXrfklK_OlxNc3oEbU&gid=0',

       'менеджмент 1.1':'https://docs.google.com/spreadsheets/d/1unVwdDM0pBJEUeO6tCCZowzM8at2Db4HCVz_8zpEJms/export?format=csv&id=1unVwdDM0pBJEUeO6tCCZowzM8at2Db4HCVz_8zpEJms&gid=0',
       'менеджмент 1.2':'https://docs.google.com/spreadsheets/d/1BVhEkOZ7Yp7AuVSLIYAg9al3FVcBepVG76z2hDqm7Pg/export?format=csv&id=1BVhEkOZ7Yp7AuVSLIYAg9al3FVcBepVG76z2hDqm7Pg&gid=0',
       'менеджмент 1.3':'https://docs.google.com/spreadsheets/d/1JS8C1dBMrIqDKV6Or_iaoSasA7wnG67xNs72nlGuXtE/export?format=csv&id=1JS8C1dBMrIqDKV6Or_iaoSasA7wnG67xNs72nlGuXtE&gid=0',
       'менеджмент 1.4':'https://docs.google.com/spreadsheets/d/1RO9Z8TonVmE01S67zwRZbNY0TbeE21Z8ZXY5RQmn71c/export?format=csv&id=1RO9Z8TonVmE01S67zwRZbNY0TbeE21Z8ZXY5RQmn71c&gid=0',
       'менеджмент 1.5':'https://docs.google.com/spreadsheets/d/1thf6a69OaRzbuxT76CQBgr1BGrQCq7OGy88ck3EBuaE/export?format=csv&id=1thf6a69OaRzbuxT76CQBgr1BGrQCq7OGy88ck3EBuaE&gid=0',

       'английский b1.2 7':'https://docs.google.com/spreadsheets/d/1hHUUdHhO7uMSr-kFrAed1NVeA2vD-2NNVqyJQCJ2X9w/export?format=csv&id=1hHUUdHhO7uMSr-kFrAed1NVeA2vD-2NNVqyJQCJ2X9w&gid=474547065',
       'английский a2':'https://docs.google.com/spreadsheets/d/1XvdFQUgAZqOZ4onHpVUDGlw3jDKmhC_Gm7IV0cbPprE/export?format=csv&id=1XvdFQUgAZqOZ4onHpVUDGlw3jDKmhC_Gm7IV0cbPprE&gid=474547065'}

answers = {
    "ОРГ": {
        "new": 0,
        "address": "ОРГ",
        "answer": "Теперь выберите поток ОРГ",
        "keyboard": "potokiORG",
        "start": "org"
    },
    "Основы менеджмента": {
        "new": 0,
        "address": "менеджмент",
        "answer": "Теперь выберите поток основ менеджмента",
        "keyboard": "potokimenegment",
        "start": "menegment"
    },
    "История": {
        "new": 0,
        "address": "история",
        "answer": "Теперь выберите раздел истории",
        "keyboard": "H_Types",
        "start": "history"
    },
    "Английский язык": {
        "new": 0,
        "address": "английский",
        "answer": "Теперь выберите уровень английского языка",
        "keyboard": "E_level",
        "start": "english"
    },

    "B1.2": {
        "new": 1,
        "address": " B1.2",
        "answer": "Теперь выберите группу",
        "keyboard": "E_B12_groups",
        "start": "english"
    },
    "A2": {
        "new": 1,
        "address": " A2",
        "answer": "Теперь выберите группу",
        "keyboard": "E_A2_groups",
        "start": "english"
    },

    "A2 d4": {
        "new": 2,
        "address": " d4",
        "answer": "Супер! вот ваши баллы:",
        "start": "english"
    },
    "B1.2 7": {
        "new": 2,
        "address": " 7",
        "answer": "Супер! вот ваши баллы:",
        "start": "english"
    },

    "орг 1.2": {
        "new": 2,
        "address": " 1.2",
        "answer": "Супер! вот ваши баллы:",
        "start": "org"
    },
    "орг 2.1": {
        "new": 2,
        "address": " 2.1",
        "answer": "Супер! вот ваши баллы:",
        "start": "org"
    },
    "орг 2.3": {
        "new": 2,
        "address": " 2.3",
        "answer": "Супер! вот ваши баллы:",
        "start": "org"
    },

    "ом 1.1": {
        "new": 2,
        "address": " 1.1",
        "answer": "Супер! вот ваши баллы:",
        "start": "menegment"
    },
    "ом 1.2": {
        "new": 2,
        "address": " 1.2",
        "answer": "Супер! вот ваши баллы:",
        "start": "menegment"
    },
    "ом 1.3": {
        "new": 2,
        "address": " 1.3",
        "answer": "Супер! вот ваши баллы:",
        "start": "menegment"
    },
    "ом 1.4": {
        "new": 2,
        "address": " 1.4",
        "answer": "Супер! вот ваши баллы:",
        "start": "menegment"
    },
    "ом 1.5": {
        "new": 2,
        "address": " 1.5",
        "answer": "Супер! вот ваши баллы:",
        "start": "menegment"
    },

    "России и мира": {
        "new": 1,
        "address": " россии и мира",
        "answer": "Теперь выберите время начала практики",
        "keyboard": "H_time",
        "start": "history"
    },
    "Реформы и реформаторы": {
        "new": 1,
        "address": " реформ и реформаторов",
        "answer": "Теперь выберите поток",
        "keyboard": "IRR_Potok",
        "start": "irr"
    },
    "Современные международные отношения": {
        "new": 1,
        "address": " современных международных отношений",
        "answer": "Теперь выберите поток",
        "keyboard": "IRS_Potok",
        "start": "irs"
    },

    "ирр 3.2": {
        "new": 2,
        "address": " 3.2",
        "answer": "Супер! вот ваши баллы:",
        "start": "irr"
    },

    "ирс 3.1": {
        "new": 2,
        "address": " 3.1",
        "answer": "Супер! вот ваши баллы:",
        "start": "irs"
    },

    "8:10":  {
        "new": 1,
        "address": " 8:10",
        "answer": "Теперь выбери преподавателя, который ведёт практику",
        "keyboard": "H_Teachers",
        "start": "history"
    },
    "9:50":  {
        "new": 1,
        "address": " 9:50",
        "answer": "Теперь выбери преподавателя, который ведёт практику",
        "keyboard": "H_Teachers",
        "start": "history"
    },
    "11:30":  {
        "new": 1,
        "address": " 11:30",
        "answer": "Теперь выбери преподавателя, который ведёт практику",
        "keyboard": "H_Teachers",
        "start": "history"
    },
    "13:30":  {
        "new": 1,
        "address": " 13:30",
        "answer": "Теперь выбери преподавателя, который ведёт практику",
        "keyboard": "H_Teachers",
        "start": "history"
    },
    "15:30":  {
        "new": 1,
        "address": " 15:30",
        "answer": "Теперь выбери преподавателя, который ведёт практику",
        "keyboard": "H_Teachers",
        "start": "history"
    },

    "Павловская":  {
        "new": 2,
        "address": " Павловская",
        "answer": "Супер! вот ваши баллы:",
        "start": "history"
    },
    "Пригодич":  {
        "new": 2,
        "address": " Пригодич",
        "answer": "Супер! вот ваши баллы:",
        "start": "history"
    }
}