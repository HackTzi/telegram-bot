import os
import telebot
import random
from message import messages

token = os.environ.get('TELEGRAM_TOKEN', None)

if token is not None:
    bot = telebot.TeleBot(token, parse_mode=None)
    DISCORD_LINK = os.environ.get('DISCORD_LINK', 'Comunicate con el staff para que de te el link, crack!')

    @bot.message_handler(func=lambda message: True, content_types=['new_chat_members'])
    def on_user_joins(message):
        user = message.json['new_chat_member']
        first_name = user.get('first_name', None)
        last_name = user.get('last_name', None)
        if first_name is not None:
            name = first_name
            if last_name is not None:
                name = f'{first_name} {last_name}'

        bot.reply_to(message, messages['welcome'].format(name=name, discord=DISCORD_LINK))


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
        bot.reply_to(message, messages['discord'].format(discord=DISCORD_LINK))

    @bot.message_handler(commands=['bug', 'error'])
    def bug(message):
        bot.reply_to(message, messages['bug'])

    @bot.message_handler(commands=['HelloWorld', 'HolaMundo', 'CiaoMondo'])
    def hello_world(message):
        random_hello_world = random.choice(messages['hello_world'])
        bot.reply_to(message, f'`{random_hello_world}`', parse_mode='Markdown')

    @bot.message_handler(commands=['convocatoria', 'call'])
    def call(message):
        bot.reply_to(message, messages['call'])

    bot.polling()
else:
    print('[!] Please, ensure to provide a the token using the enviroment variables.')
