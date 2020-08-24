import random
# database simbase config
# GSM ip address set default 192.168.1.2 for 16 sim-lines

# sms server (!) parameters dbhost and dbpass
dbhost = ""
dbpass = ""

# внешний вид кнопок

BUTTON_MAIN_MENU = "Главное меню " + u'\U000027A1'

BUTTON_MONEY = "Сделать перевод " + u'\U0001F4B8'
BUTTON_HISTORY = "История последних транзакций " + u'\U0001F4C3'
BUTTON_UNREALSUM = "Добавить транзацию" + u'\U0001F4DD'
BUTTON_REPORT = "Отчет " + u'\U0001F4CA'
BUTTON_SIMBALANCE = "Узнать баланс всех симкарт" + u'\U0001F4B0'

BUTTON_LOW = "15"
BUTTON_MIDDLE = "30"
BUTTON_HIGH = "50"
BUTTON_GENREPORT = "Сгенерировать отчет"
BUTTON_SENDMONEY = "Отправить деньги"

BUTTON_ADDUNRSUM = "Добавить доход"
BUTTON_ADDUNREXP = "Добавить расход"


BUTTON_PARSPROFIT = "Отчет по всем проектам по боту tribunal" + u'\U0001F4B0'

# Сообщения для конкретных меню
sendmoneymantra = '''Чтобы сделать перевод кратный 14200 нужно написать сообщение боту в таком формате (номер и симлайн):\nAAAABBBBCCCCDDDD N или 79123456789 N\n
Чтобы сделать перевод с другой суммой нужно после номера карты (или номера телефона) указать сумму (мин. 100 макс. 14200 и симлайн ):
\nAAAABBBBCCCCDDDD EEEEE N или 79123456789 EEEEE N\n'''

addexporsum = "Чтобы добавить расход или доход нужно отравить сообщение\nВ таком формате: СУММА доход (расход)\n\nПример1: 350 доход\nПример2: 14200 расход"

''' Конфигурация '''

# конфигурация тела сообщения (Пример)
smsbody = {"username": "user1", "password": "12345",
           "content": "", "prov_name": "test", "line": "new1sms2",
           "number": "145"}

# конфигурация соответствия
simbase = {'1':'new1', '2':'new2', '3':'new3',
           '4':'new4', '5':'new5', '6':'new6',
           '7':'new7', '8':'new8', '9':'new9',
           '10':'new1sms10', '11':'new1sms11', '12':'new1sms12',
           '13':'new1sms13', '14':'new1sms14', '15':'new1sms15',
           '16':'new1sms16'}

# конфигурация simbase
arguments = {
    'user' : 'admin',  # gsm gateway web-GUI login
    'passwd' : 'admin',  # gsm gateway web-GUI password
    'balance_tel_number1' : '*104#',  # balance number for line 1
    'balance_tel_number2' : '*104#',  # balance number for line 2
    'balance_tel_number3' : '*104#',  # balance number for line 3
    'balance_tel_number4' : '*104#',  # balance number for line 4
    'balance_tel_number5' : '*104#',  # balance number for line 5
    'balance_tel_number6' : '*104#',  # balance number for line 6
    'balance_tel_number7' : '*104#',  # balance number for line 7
    'balance_tel_number8' : '*104#',  # balance number for line 8
    'balance_tel_number9' : '*104#',  # balance number for line 9
    'balance_tel_number10' : '*104#',  # balance number for line 10
    'balance_tel_number11' : '*104#',  # balance number for line 11
    'balance_tel_number12' : '*104#',  # balance number for line 12
    'balance_tel_number13' : '*104#',  # balance number for line 13
    'balance_tel_number14' : '*104#',  # balance number for line 14
    'balance_tel_number15' : '*104#',  # balance number for line 15
    'balance_tel_number16' : '*104#',  # balance number for line 16
    'our_gsm_gateway_ip' : '192.168.1.2',
    'ussdports' : '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16'
    }

# логи на сервере с названием их директорий (излишний функционал, тест)
projectdirs = {'check':'skylog2.txt', 'easy':'skylog2.txt',
               'eco':'logTESTNEW.txt', 'skycash':'logTESTsky.txt',
               'spravkachang':'logTESTNEW.txt', 'sweet':'logTESTNEW.txt',
               'vipch':'logTESTNEW.txt'}

# сумма дефолтная для отправки
defaultsum = "14200"

# функции сообщений (возможность добавления для рандомного ответа)
def AUTH_BOTTON():
    return random.choice(["Для авторизации нажмите на кнопку"])
def STR_CANCEL_REQUEST():
    return random.choice(["Не хочешь, как хочешь:)"])
def STR_NEED_INPUT_ANYTHINK():
    return random.choice(["Нужно что-нибудь ввести...", "Ты не можешь отправить пустой запрос"])
def MAIN_MENU_MESSAGE():
    return random.choice(["Привет {} " + u'\U0000270C' + "\nЧем я могу быть полезен?"])
def HISTORY_MAIN():
    return random.choice(["Выберете сколько вы хотите вывести последних транзакций:"])
def STR_SELECT_FROM_LIST():
    return random.choice(["Выбери из списка"])
def STR_SOMETHING_ELSE():
    return random.choice(["Что нибудь еще", "Еще что-нибудь"])
def STR_DONT_UNDESTAND_YOU():
    return random.choice(["Не понимаю, о чем ты?", "Прости, но я не понимаю тебя :("])



