from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# اینجا توکن ربات خودت رو قرار بده
TOKEN = '7841808992:AAFiEM_Nid_lJRA4yMkDaHGRn-Wr5KsA8lY'

# دستور شروع
def start(update: Update, context: CallbackContext):
    update.message.reply_text('سلام! من ربات تلگرام هستم.')

# دستور کمک
def help_command(update: Update, context: CallbackContext):
    update.message.reply_text('دستورات من:\n/start - شروع\n/help - کمک')

# تنظیمات ربات
def main():
    updater = Updater(TOKEN)

    # دریافت دیسپچر
    dispatcher = updater.dispatcher

    # اضافه کردن دستورات
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help_command))

    # شروع ربات
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()