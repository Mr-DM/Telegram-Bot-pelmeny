import telebot
from text import *
from config import Token
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton



bot = telebot.TeleBot(Token)

def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(InlineKeyboardButton("1", callback_data="1"),
            InlineKeyboardButton("2", callback_data="2"),
            InlineKeyboardButton("3", callback_data="3"))
    
    markup.add(InlineKeyboardButton("4", callback_data="4"),
            InlineKeyboardButton("5", callback_data="5"))
    
    return markup



def gen_markup_1():
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(InlineKeyboardButton("🥟 Пельмени", callback_data="cb_Pelmeni"),
            InlineKeyboardButton("🥟 Вареники", callback_data="cb_Vareniki"),
            InlineKeyboardButton("🥟 Хинкали", callback_data="cb_Hinkali"))
    markup.add(InlineKeyboardButton("🥟 Манты", callback_data="cb_Manti"),
            InlineKeyboardButton("🥟 Буузы", callback_data="cb_Buuz"))
    
    return markup


def gen_markup_2():

    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(InlineKeyboardButton("🥟 Цзяоцзы ", callback_data="cb_szaosz"),
            InlineKeyboardButton("🥟 Гедза", callback_data="cb_gedza"),
            InlineKeyboardButton("🥟 Дим-самы", callback_data="cb_dimSams"))
    markup.add(InlineKeyboardButton("🥟 Момо", callback_data="cb_momo"),
            InlineKeyboardButton("🥟Вонтоны ", callback_data="cb_votons"))
    
    return markup

def gen_markup_3():
    """
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(InlineKeyboardButton("🥟 ", callback_data="cb_"),
            InlineKeyboardButton("🥟 ", callback_data="cb_"),
            InlineKeyboardButton("🥟 ", callback_data="cb_"))
    markup.add(InlineKeyboardButton("🥟 ", callback_data="cb_"),
            InlineKeyboardButton("🥟 ", callback_data="cb_"))
    
    return markup
"""
    pass
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, text_start)
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Список Пельмени", reply_markup=gen_markup())
@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, text_info)
    


@bot.callback_query_handler(func=lambda call: call.data in ["1", "2", "3", "4", "5"])
def callback_query(call):
    if call.data == "1":
        first(call.message)
    elif call.data == "2":
        second(call.message)
    elif call.data == "3":
        pass
        
        

# Handle submenu callbacks
@bot.callback_query_handler(func=lambda call: call.data in ["cb_Pelmeni", "cb_Vareniki", "cb_Hinkali", "cb_Manti", "cb_Buuz"])
def submenu_callback_query(call):
    if call.data == "cb_Pelmeni":
            bot.send_photo(call.message.chat.id, open('img/pelmeni.jpg', 'rb'), text_pelmeni)
    elif call.data == "cb_Vareniki":
        bot.send_photo(call.message.chat.id, open('img/vareniki.jpg', 'rb'), text_vareniki)
    elif call.data == "cb_Hinkali":
        bot.send_photo(call.message.chat.id, open('img/Hinkali.jpg', 'rb'), text_hinkali)
    elif call.data == "cb_Manti":
        bot.send_photo(call.message.chat.id, open('img/Manti.jpg', 'rb'), text_manti)
    elif call.data == "cb_Buuz":
        bot.send_photo(call.message.chat.id, open('img/Buzz.jpg', 'rb'), text_buuz)

@bot.callback_query_handler(func=lambda call: call.data in ["cb_szaosz","cb_gedza" , "cb_dimSams", "cb_momo", "cb_votons"])
def submenu_callback_query(call):
    if call.data == "cb_szaosz":
        bot.send_photo(call.message.chat.id, open('img/szasz.jpg', 'rb'), text_szaosz)
    elif call.data == "cb_gedza":
        bot.send_photo(call.message.chat.id, open('img/gedza.jpg', 'rb'), text_gedza)
    elif call.data == "cb_dimSams":
        bot.send_photo(call.message.chat.id, open('img/dimSams.jpg', 'rb'), text_dimSams)
    elif call.data == "cb_momo":
        bot.send_photo(call.message.chat.id, open('img/momo.jpg', 'rb'), text_momo)
    elif call.data == "cb_votons":
        bot.send_photo(call.message.chat.id, open('img/votons.jpg', 'rb'), text_votons)
# First menu action
def first(message):
    bot.send_message(message.chat.id, "Список Пельмени", reply_markup=gen_markup_1())

def second(message):
    bot.send_message(message.chat.id, "Список Пельмени", reply_markup=gen_markup_2())

bot.infinity_polling()

