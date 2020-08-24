from database import database
import content
import bot
import menu


from_chat = {}

# Система авторизации пользователя по white list при использовании метода share contact
# база данных whitelist - sqlite3

class AuthorizationSystem:
    def __init__(self):

        self.white_list = database.get_whitelist()
        self.authorizated_users = database.get_user_sessions()

    def is_authorization(self, user_id):
        if user_id in self.authorizated_users:
            return True

        return False

    def authorization(self, user_id, phone_number):
        if phone_number[0] != "+":
            phone_number = "+{}".format(phone_number)

        if phone_number in self.white_list:
            database.add_user_session(user_id, phone_number)
            self.authorizated_users[user_id] = {
                "phone": phone_number,
            }
            return True
        else:
            return False

    def get_contact(self, user_id):
        phone_number = self.authorizated_users[user_id]["phone"]
        name = self.white_list[phone_number]["name"]
        second_name = self.white_list[phone_number]["last_name"]
        return {"phone_number": phone_number, 
                "name": name, 
                "last_name": second_name}


    def get_name_user(self, user_id):
        phone_number = self.authorizated_users[user_id]["phone"]
        return self.white_list[phone_number]["name"]

    def get_full_name_user(self, user_id):
        phone_number = self.authorizated_users[user_id]["phone"]
        name = self.white_list[phone_number]["name"]
        second_name = self.white_list[phone_number]["last_name"]
        return "{} {}".format(name, second_name)

    def validation(self, message):
        chat_id = message.chat.id
        user_id = message.from_user.id

        if message.contact is None:
            msg = bot.bot.send_message(chat_id, content.AUTH_BOTTON())
            bot.bot.register_next_step_handler(msg, authorization)
            return

        phone_number = message.contact.phone_number

        if phone_number == "":
            msg = bot.bot.send_message(chat_id, content.AUTH_BOTTON())
            bot.bot.register_next_step_handler(msg, authorization)
        else:
            if self.is_authorization(user_id) == True:
                return

            if self.authorization(user_id, phone_number) == True:
                name = auth.get_name_user(user_id)
                bot.bot.send_message(chat_id, content.MAIN_MENU_MESSAGE().format(name))
                print('all ok')
                menu.first_menu(message)
            else:
                bot.bot.send_message(chat_id, "Тебя нет в Whitelist")



auth = AuthorizationSystem()

