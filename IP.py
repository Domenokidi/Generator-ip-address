import random
import time
from tqdm import tqdm
import os
#from progress.bar import IncrementalBar
#from itertools import islice
text = 0

#HELP
def help():
    print("""
    Генератор Ip адресов работает по принципу рандомизации случайных значений.
    Изменению поддаются только крайние два блока, например 192.168.[110.21]  
    Для начала генерации укажите ваши адреса IP в файле ip.txt

    Очистка файла от дубликатов не является обязательной по умолчанию.
    Как только вы окончили генерацию диапазонов, повторно запустите скрипт,
    выполните команду -r для выполнения очистки файла от повторов.

    [!] Обратите внимание, очистка дубликатов занимает некоторое время.
    Методы удаления дублей в linux реализованы гораздо лучше и выполняют
    очистку в разы быстрее!
    """)
    time.sleep(10)
    back = input('Вернуться в меню? | y/n\n')
    if back == 'y':
        os.system("cls")
        menu()
    elif back == 'n':
        exit(0)
    else:
        exit(0)
#Generation ip
def gener():

    os.system("cls")
    print('Меню запуска генератора: \n\n\n')
    time.sleep(1)
    colvo = input('\n[*]Укажите количество вариаций от одной строки: \n')
    time.sleep(1)
    block = input('\n[*]Ниже укажите, рандомизация одного или двух блоков? [!](На данный момент только два блока!)\n')

    if block == ('1'):
        print('Вы указали рандомизацию 1')
        print('Сейчас он не реализован, будет в ближайшее время :з')
        exit(0)
    else:
        print('\n\nВы указали рандомизацию двух блоков.\n\n')
        dep = open("ip.txt", "r")

        colvo = int(colvo)
        print('[*]Запускаю машину рандома...\n\n')

        sec = 0
        time.sleep(1)
        sec += 1

        strok = sum(1 for line in open('ip.txt', 'r'))
        colvo = int(colvo)
        strok = int(strok)
        times = (colvo * strok)  # строка на вариант
        timescals = (times // 200)
        print("[*]Ожидаемое время ~ " + str(timescals) + '\n')
        time.sleep(1)
        print('\nНа разном железе - разное время)\n \nГенерация будет окончена на второй загрузке.')

        c = int(0)

        while True:
            line = dep.readline()
            if not line:
                break
            a = (line.strip())

            i = 0
            r = int(0)

            if c == 0:
                c = (c + 1)
                while r < 1:
                    r = r + 1
                    timescals = str(timescals)
                    mytime = [timescals]

                for i in tqdm(timescals):
                    time.sleep(0.3)
            else:
                i = int(i)
                while i < colvo:
                    ip1 = random.randint(1, 255)
                    ip2 = random.randint(1, 255)
                    a = str(a)
                    z = (a.split('.'))
                    result = (z[0] + '.' + z[1] + '.' + str(ip1) + '.' + str(ip2))
                    with open("Result\list.txt", "a") as file:
                        i = str(i)
                        file.write(result + '\n')

                    i = int(i) + 1
                    colvo = int(colvo)
                    if i == colvo:
                        break
            dep.close

        mylist = [1, 2, 3]
        for i in tqdm(mylist):
            time.sleep(1)

        if 0 == 0:
            os.system("cls")
            print('\n\n\nГенерация пар окончена.\nРезультаты : Result\list.txt\n\n\n')
            menu()

def randoms():
    os.system("cls")
    print("""
        Генератор случайных пар Ip адресов, от 100.0.0.0 до 250.0.0.0

        [!]Внимательно отнеситесь к данному варианту генерации адресов,
        в список могут попасть Ip стран, которые вас категорически 
        не привлекают.
        """)


    time.sleep(5)
    ss = input('Укажите ниже количество адресов: \n')

    s = int(1)
    ss = int(ss)

    while s < ss:
        ip1 = random.randint(100, 255)
        ip2 = random.randint(1, 255)
        ip3 = random.randint(1, 255)
        ip4 = random.randint(1, 255)

        result = (str(ip1) + '.' + str(ip2) + '.' + str(ip3) + '.' + str(ip4))
        with open("Result\Randomlist.txt", "a") as file:
            file.write(result + '\n')

        s = s + 1
    os.system("cls")
    print('Генерация пар окончена.\nРезультаты : Result\Randomlist.txt')
    menu()


#Menu
def menu():
    os.system("cls")
    print("""
                                                
                        ██████╗░░█████╗░███╗░░░███╗███████╗███╗░░██╗░█████╗░██╗░░██╗██╗██████╗░██╗
                        ██╔══██╗██╔══██╗████╗░████║██╔════╝████╗░██║██╔══██╗██║░██╔╝██║██╔══██╗██║
                        ██║░░██║██║░░██║██╔████╔██║█████╗░░██╔██╗██║██║░░██║█████═╝░██║██║░░██║██║
                        ██║░░██║██║░░██║██║╚██╔╝██║██╔══╝░░██║╚████║██║░░██║██╔═██╗░██║██║░░██║██║
                        ██████╔╝╚█████╔╝██║░╚═╝░██║███████╗██║░╚███║╚█████╔╝██║░╚██╗██║██████╔╝██║
                        ╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝╚═╝╚═════╝░╚═╝
                                                         2021  

                                         Генератор IP-пар для сканирования. 

                                         [!] -h [Справка]
                                         [!] -c [Настройка и запуск генерации]
                                         [!] -s [Случайные пары адресов]                     
    	""")

    print()
    text = input('Вы в главном меню. Выберите команду. \n')
    if text == "-h":
        help()
    elif text == "-c":
        gener()
    elif text == "-s":
        randoms()



menu()
