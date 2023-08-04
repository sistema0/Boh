import telebot
from deep_translator import GoogleTranslator
from telebot import types

# Inserisci il token del tuo bot Telegram qui
TOKEN = '5699790983:AAEnaPi0keC0eLVGYo0llGSSwD-Xsh7zSTw'

bot = telebot.TeleBot(TOKEN)

# Definisci la tastiera inline
markup = types.InlineKeyboardMarkup()
button = types.InlineKeyboardButton('Clicca qui', url='https://google.com')
markup.add(button)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Ciao! Sono un bot che traduce messaggi. Inviami un messaggio in qualsiasi lingua e ti risponderò con la traduzione in italiano.", reply_markup=markup)

@bot.message_handler(commands=['traduci','translate'])
def translate(message):
    if message.reply_to_message is None:
        bot.send_message(message.chat.id, "Per favore, rispondi ad un messaggio con /traduci per tradurlo in italiano.")
        return
    translation = GoogleTranslator(source='auto', target='it').translate(message.reply_to_message.text)
    bot.send_message(message.chat.id, translation)

bot.infinity_polling()