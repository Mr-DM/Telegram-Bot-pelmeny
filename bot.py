import config
import telebot
import random

list_fact = ["Пельмени имеют легендарную историю, которая уходит корнями в Сибирь в XV веке",
            "В Сибири пельмени традиционно замораживают на улице зимой и используют как консервированную пищу ",
            "Считается, что слово «пельмени» происходит от финно-угорского слова «pelm», означающего хлеб или выпечку в форме уха — намек на характерную форму пельменей."]

API_TOKEN = config.token

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=[ 'start', 'info'])
def send_welcome(message):
    bot.reply_to(message, """\
        Привет 👋 
    я бот пельмени 2024 я разказываю интересные факты про пельмени разказываю про рецепты пельменей  \
""")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message,'''Command: 
/start - start the bot 
/help - help command 
/info info about bot 
/fact - Расказывает радомный факты про пельмени
                 ''')

@bot.message_handler(commands=['fact'])
def send_info(message):
    bot.reply_to(message,random.choice(list_fact))

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
