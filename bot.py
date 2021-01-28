import os
import telebot
from message import messages

token = os.environ.get('token', None)

if token is not None:
    bot = telebot.TeleBot(token, parse_mode=None)


    @bot.message_handler(func=lambda m: True, content_types=['new_chat_participant'])
    def on_user_joins(message):
        user = message.from_user
        if hasattr(user, 'first_name') and user.first_name is not None:
            name = user.first_name
            if hasattr(user, 'last_name') and user.last_name is not None:
                name = f'{name} {user.last_name}'
        else:
            name = 'Rockstar'

        bot.reply_to(message, messages['welcome'].format(name=name))


    @bot.message_handler(commands=['reglas'])
    def rules(message):
        bot.reply_to(message, messages['rules'])


    @bot.message_handler(commands=['proyectos'])
    def projects(message):
        bot.reply_to(message, messages['projects'])
        for project in messages['current_projects']:
            bot.reply_to(message, project)


    @bot.message_handler(commands=['donaciones'])
    def donations(message):
        bot.reply_to(message, messages['donations'])


    bot.polling()
else:
    print('[!] Please, ensure to provide a the token using the enviroment variables.')
