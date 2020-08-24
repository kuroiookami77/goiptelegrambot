from bot import bot
from telebot import types
import content
import re
import database
import goip
import menu
import parserlog as pars
import pandas as pd


filename = "report.csv"
nicefile = 'file.xls'


def func_send_money(message):
    try:
        #                   Регулярные выражения для поиска паттернов сообщений
        cardnum = re.findall(r'^\d{16}\s\d{1,2}$', message.text)
        cardnumwsumm = re.findall(r'^\d{16}\s\d{3,5}\s\d{1,2}$', message.text)
        telnum = re.findall(r'^\d{11}\s\d{1,2}$', message.text)
        telnumwsum = re.findall(r'^\d{11}\s\d{3,5}\s\d{1,2}$', message.text)

        #     баланс всех симок
        if message.text == content.BUTTON_SIMBALANCE:
            bot.send_message(message.chat.id, 'Идет проверка баланса по всей симбазе, подождите 1-2 минуты')
            menu.send_money(message)
            # data - это отправка и прием ussd кодов *104# (изменить можно в content.py, arguments)
            data = goip.runner().decode('utf-8')
            # allbalanceinfo - все сообщения содержащие паттерн
            allbalanceinfo = ""
            for i in data.split('error'):
                ex = re.findall(r'^\d{1,2}\W\b', i)
                if ex != []:
                    allbalanceinfo += "simline: " + i[:-2] + "\n\n"
            bot.send_message(message.chat.id, allbalanceinfo)


        elif cardnum != []:
            menu.send_money(message)

            cardnumwsim = cardnum[0].split()
            destin = cardnumwsim[0] + " " + "14200"
            # summ(сумма), simline (симлайн), project(проект), destination(реквизит), description(описание транз), unrealsumm (неподв деньги)

            database.Database.add_transaction(database.DATABASE_NAME,'14200', content.simbase[cardnumwsim[1]],
                                              'testproj', cardnumwsim[0], 'default trans', '0')
            # requests.post('http://ip/goip/sendsms/',content.smsbody)
            bot.send_message(message.chat.id, 'Был осуществлен перевод:\n{}'.format(destin))

        elif cardnumwsumm != []:
            menu.send_money(message)

            cardandsumwsim = cardnumwsumm[0].split()
            destin = cardandsumwsim[0] + " " + cardandsumwsim[1]
            database.Database.add_transaction(database.DATABASE_NAME, cardandsumwsim[1], content.simbase[cardandsumwsim[2]],
                                              'testproj', cardandsumwsim[0],  'trans with sum', '0')

            # requests.post('http://ip/goip/sendsms/',content.smsbody)

            bot.send_message(message.chat.id, 'Был осуществлен перевод:\n{}'.format(destin))

        elif telnum != []:
            send_money(message)

            telnumwsim = telnum[0].split()
            destin = telnumwsim[0] + " " + "14200"
            database.Database.add_transaction(database.DATABASE_NAME, '14200', content.simbase[telnumwsim[1]],
                                              'testproj', telnumwsim[0], 'default trans telnumber', '0')

            # requests.post('http://ip/goip/sendsms/',content.smsbody)
            bot.send_message(message.chat.id, 'Был осуществлен перевод:\n{}'.format(destin))

        elif telnumwsum != []:
            menu.send_money(message)
            telandsumwsim = telnumwsum[0].split()

            # нужен выбор сим и проекта
            destin = telandsumwsim[0]+" "+telandsumwsim[1]

            database.Database.add_transaction(database.DATABASE_NAME, telandsumwsim[1], content.simbase[telandsumwsim[2]],
                                              'testproj', telandsumwsim[0], 'trans with sum telnumber', '0')

            # requests.post('http://ip/goip/sendsms/',content.smsbody)
            bot.send_message(message.chat.id, 'Был осуществлен перевод:\n{}'.format(destin))

        #     главное меню
        elif message.text == content.BUTTON_MAIN_MENU:
            menu.first_menu(message)
            print('hello func send money')
        elif message.text == content.BUTTON_SENDMONEY:
            menu.send_money(message)
            bot.send_message(message.chat.id, content.sendmoneymantra)
        else:
            bot.send_message(message.chat.id, 'Неправильный формат сообщения, перечитайте форму')
            menu.send_money(message)


    except Exception as e:
        bot.reply_to(message,'Error sendmoney button. Contact the administrator and please DONT use bot.')

# функция информации вытаскивания из базы данных
def func_history_menu(message):
    try:
        bot.send_message(message.chat.id, "Ты нажал кнопку {}".format(message.text))
        if message.text == content.BUTTON_MAIN_MENU:
             menu.first_menu(message)
        #      показать 15 переводов
        elif message.text == content.BUTTON_LOW:
             menu.history_menu(message)
             data = database.Database.show_transaction(database.DATABASE_NAME, content.BUTTON_LOW)
             for dat in data:
                 bot.send_message(message.chat.id, "Индекс: {}; Simline: {}; Сумма: {};\n Дата: {}; Реквизиты: {}\n Описание: {}".format(dat['id'],
                                                                                                                          dat['simline'],
                                                                                                                          dat['summ'],
                                                                                                                          dat['date'],
                                                                                                                          dat['destination'],
                                                                                                                          dat['description']))
        #    показать 30 переводов
        elif message.text == content.BUTTON_MIDDLE:
             menu.history_menu(message)
             data = database.Database.show_transaction(database.DATABASE_NAME, content.BUTTON_MIDDLE)
             for dat in data:
                 bot.send_message(message.chat.id, "Индекс: {}; Simline: {}; Сумма: {};\n Дата: {}; Реквизиты: {}\n Описание: {}".format(dat['id'],
                                                                                                                          dat['simline'],
                                                                                                                          dat['summ'],
                                                                                                                          dat['date'],
                                                                                                                          dat['destination'],
                                                                                                                          dat['description']))
        #    показать 50 переводов
        elif message.text == content.BUTTON_HIGH:
             menu.history_menu(message)
             data = database.Database.show_transaction(database.DATABASE_NAME, content.BUTTON_HIGH)
             print(data)
             for dat in data:
                 bot.send_message(message.chat.id, "Индекс: {}; Simline: {}; Сумма: {};\n Дата: {}; Реквизиты: {}\n Описание: {}".format(dat['id'],
                                                                                                                          dat['simline'],
                                                                                                                          dat['summ'],
                                                                                                                          dat['date'],
                                                                                                                          dat['destination'],
                                                                                                                          dat['description']))
        else:
             menu.history_menu(message)
    except Exception as e:
             bot.reply_to(message, 'Error history button. Contact the administrator and please DONT use bot.')
             menu.main_menu(message)

# функция создания отчета
def func_create_report(message):
    try:
        if message.text == content.BUTTON_MAIN_MENU:
            menu.first_menu(message)
        elif message.text == content.BUTTON_GENREPORT:
            menu.create_report(message)
            data = database.Database.show_transaction(database.DATABASE_NAME, '9999999')
            print(data[0]['summ'])
            # calculate summ and add human
            comment = {'':'Сумма всех транзакций в рублях:'}
            datawsumm = {'': 0}
            for pay in data:
                if pay['summ'] != '':
                   datawsumm[''] += pay['summ']

            data.append(comment)
            data.append(datawsumm)
            # format to human

            file = open(filename, "w", newline='')
            with file as f:
                 df = pd.DataFrame(data)  # transpose to look just like the sheet above
                 df.to_csv(filename)
                 df.to_excel(nicefile)
            file.close()

            # send to user

            file = open(nicefile, 'rb')
            bot.send_document(message.chat.id, file)
            file.close()

            print('Отчет сгенерирован')

        else:
            bot.send_message(message.chat.id, 'Неправильный формат сообщения, перечитайте форму')
            menu.create_report(message)



    except Exception as e:
        # print(e)
        bot.reply_to(message, 'Error create report button. Contact the administrator and please DONT use bot.')

# функция для добавления дохода или расхода

def func_unrealsum(message):
    try:

        addunrsum = re.findall(r'^\d{1,7}\sдоход$', message.text)
        addunrexp = re.findall(r'^\d{1,7}\sрасход$', message.text)

        if message.text == content.BUTTON_MAIN_MENU or message.text == "/start":
            menu.first_menu(message)
            # добавить сумму, если сообщение подходит под рег выражение добавления дохода/расхода

        elif addunrsum != []:
            menu.unrealsum_menu(message)
            income = addunrsum[0].split()[0]
            # summ(сумма), simline (симлайн), project(проект), destination(реквизит), description(описание транз), unrealsumm (неподв деньги)

            bot.send_message(message.chat.id, 'Ты добавил доход {} р.'.format(income))
            database.Database.add_transaction(database.DATABASE_NAME, income, 'nosimline', 'testproj', '0',
                                              'доходная ручная транза', income)

        elif addunrexp != []:
            menu.unrealsum_menu(message)
            expenses = addunrexp[0].split()[0]
            bot.send_message(message.chat.id, 'Ты добавил расход {} р.'.format(expenses))
            database.Database.add_transaction(database.DATABASE_NAME, '-{}'.format(expenses), 'nosimline', 'testproj',
                                              '0', 'расходная ручная транза', '-{}'.format(expenses))

        else:
            menu.unrealsum_menu(message)
            bot.send_message(message.chat.id,
                             'Твое сообщение {} не подходит под условие. Прочитай подсказку'.format(message.text))

    except Exception as e:
        print(e)
        bot.reply_to(message, 'Error add unrealsum button. Contact the administrator and please DONT use bot.')