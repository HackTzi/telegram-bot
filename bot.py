import os
import telebot
from message import messages

token = os.environ.get('token', None)

if token is not None:
    bot = telebot.TeleBot(token, parse_mode=None)


    @bot.message_handler(func=lambda message: True, content_types=['new_chat_members'])
    def on_user_joins(message):
        user = message.json['new_chat_member']
        first_name = user.get('first_name', None)
        last_name = user.get('last_name', None)
        if first_name is not None:
            name = first_name
        elif last_name is not None:
            name = f'{first_name} {last_name}'

        bot.reply_to(message, messages['welcome'].format(name=name))


    @bot.message_handler(commands=['reglas', 'rules'])
    def rules(message):
        bot.reply_to(message, messages['rules'])


    @bot.message_handler(commands=['proyectos', 'projects'])
    def projects(message):
        bot.reply_to(message, messages['projects'])
        for project in messages['current_projects']:
            bot.reply_to(message, project)


    @bot.message_handler(commands=['donaciones', 'donations'])
    def donations(message):
        bot.reply_to(message, messages['donations'])

    @bot.message_handler(commands=['discord'])
    def discord(message):
        bot.reply_to(message, messages['discord'])


    bot.polling()
else:
    print('[!] Please, ensure to provide a the token using the enviroment variables.')
