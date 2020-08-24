from telebot import types
import content
from auth import auth
from bot import bot
import menu

@bot.message_handler(commands=['start'])
# обработка команды /start, запуск бота
def first_message(message):

    chat_id = message.chat.id
    user_id = message.from_user.id

    # Авторизация. Если пользователь есть в White List отправляем меню.
    if auth.is_authorization(user_id) == True:
        menu.first_menu(message)
        return
    print(user_id)

    markup = types.ReplyKeyboardMarkup(True, True)
    markup.add(types.KeyboardButton('Share contact', request_contact=True))

    msg = bot.send_message(chat_id, content.AUTH_BOTTON(), reply_markup=markup)
    bot.register_next_step_handler(msg, auth.validation)

# start
bot.polling()