import os
import telebot


token = os.environ.get('token', None)

if token is not None:
    bot = telebot.TeleBot(token, parse_mode=None)
else:
    print('Please, ensure to provide a token using the enviroment variables.')

@bot.message_handler(func=lambda m: True, content_types=['new_chat_members'])
def on_user_joins(message):
    user_name = message.new_chat_participants.first_name
    print(user_name)

@bot.message_handler(commands=['help'])
def send_help_message(message):
    import pdb; pdb.set_trace()
    bot.reply_to(message, 'Hi , you need help?')


bot.polling()
