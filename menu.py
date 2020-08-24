from bot import bot
from telebot import types
import content
import re
import database
import goip

import parserlog as pars
import pandas as pd
import funcmenu


# функция самого первого меню
def first_menu(message):
    try:
        chat_id = message.chat.id
        markup = types.ReplyKeyboardMarkup(True, True)

        history = types.InlineKeyboardButton(content.BUTTON_HISTORY)
        duty = types.InlineKeyboardButton(content.BUTTON_MONEY)
        report = types.InlineKeyboardButton(content.BUTTON_REPORT)
        unreal = types.InlineKeyboardButton(content.BUTTON_UNREALSUM)

        markup.add(history)
        markup.add(duty)
        markup.add(report)
        markup.add(unreal)

        bot.send_message(chat_id, content.STR_SELECT_FROM_LIST(), reply_markup=markup)
        bot.register_next_step_handler(message, main_menu)

        return
    except Exception as e:
        bot.reply_to(message, 'error first menu. Contact the administrator and please DONT use bot.')

# функция главного меню выступает в роли сплиттера
def main_menu(message):
    try:
        chat_id = message.chat.id
        if message.text == content.BUTTON_HISTORY:
            history_menu(message)
            return
        elif message.text == content.BUTTON_MONEY:
            bot.send_message(chat_id, content.sendmoneymantra)
            send_money(message)
            return
        elif message.text == content.BUTTON_REPORT:
            bot.send_message(chat_id, 'Вы в меню создании отчета')
            create_report(message)
            return
        elif message.text == content.BUTTON_UNREALSUM:
            bot.send_message(chat_id, content.addexporsum)
            unrealsum_menu(message)
            return
        else:
            first_menu(message)
            return
    except Exception as e:
        bot.reply_to(message, 'Error main menu. Contact the administrator and please DONT use bot.')

# функция отправки меню для отчетов
def history_menu(message):
    try:
        chat_id = message.chat.id
        markup = types.ReplyKeyboardMarkup(True, True)
        low = types.InlineKeyboardButton(content.BUTTON_LOW)
        middle = types.InlineKeyboardButton(content.BUTTON_MIDDLE)
        high = types.InlineKeyboardButton(content.BUTTON_HIGH)
        homepage = types.InlineKeyboardButton(content.BUTTON_MAIN_MENU)

        markup.add(low)
        markup.add(middle)
        markup.add(high)
        markup.add(homepage)

        bot.send_message(chat_id, content.HISTORY_MAIN(), reply_markup=markup)
        bot.register_next_step_handler(message, funcmenu.func_history_menu)
    except Exception as e:
        bot.reply_to(message, 'Error history menu')

# функция отправки меню для переводов
def send_money(message):
    try:
        chat_id = message.chat.id

        send = types.InlineKeyboardButton(content.BUTTON_SENDMONEY)
        homepage = types.InlineKeyboardButton(content.BUTTON_MAIN_MENU)
        simbalance = types.InlineKeyboardButton(content.BUTTON_SIMBALANCE)



        markup = types.ReplyKeyboardMarkup(True, True)
        markup.add(send)
        markup.add(simbalance)
        markup.add(homepage)


        bot.send_message(chat_id,'Для того чтобы узнать баланс нажмите кнопку\nЕсли баланс получить не удалось - можете попробовать еще раз.', reply_markup=markup)
        bot.register_next_step_handler(message, funcmenu.func_send_money)


        #отправить деньги сделать перевод (реквест)

    except Exception as e:
        bot.reply_to(message,'Error sendmoney menu. Contact the administrator and please DONT use bot.')

# функция отправки меню для отчета
def create_report(message):
    try:
        chat_id = message.chat.id

        genrep = types.InlineKeyboardButton(content.BUTTON_GENREPORT)
        homepage = types.InlineKeyboardButton(content.BUTTON_MAIN_MENU)

        # отчет по всем проектам bot tribunal
        # parsprofit = types.InlineKeyboardButton(content.BUTTON_PARSPROFIT)
        # markup.add(parsprofit)

        markup = types.ReplyKeyboardMarkup(True, True)

        markup.add(genrep)
        markup.add(homepage)


        bot.send_message(chat_id, "Чтобы сгенерировать отчет нажмите кнопку", reply_markup=markup)

        bot.register_next_step_handler(message, funcmenu.func_create_report)

        # отправить деньги сделать перевод (реквест)

    except Exception as e:
        bot.reply_to(message, 'Error createreport menu. Contact the administrator and please DONT use bot.')

# функция отправки меню для
def unrealsum_menu(message):
    try:
        chat_id = message.chat.id
        main = types.InlineKeyboardButton(content.BUTTON_MAIN_MENU)

        markup = types.ReplyKeyboardMarkup(True, True)
        markup.add(main)

        bot.send_message(chat_id, "Чтобы добавить расход или доход нажмите кнопку", reply_markup=markup)
        bot.register_next_step_handler(message, funcmenu.func_unrealsum)


    except Exception as e:
        bot.reply_to(message, 'Error unrealsum menu. Contact the administrator and please DONT use bot.')
