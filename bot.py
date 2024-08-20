from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Updater, CommandHandler

def start(update, context):
    keyboard = [[InlineKeyboardButton("Play Guess the Number", web_app=WebAppInfo(url="YOUR_WEB_APP_URL"))]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Welcome to the Guess the Number game!', reply_markup=reply_markup)

def main():
    updater = Updater("6398685157:AAGKnMJm3oRHxavLY-MHbXTVa4HeDu_7H-E", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
  
