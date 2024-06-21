"""
This is the main script which contains the framework code for the bot.
"""

# Import Modules
import telebot
import os
from dotenv import load_dotenv

# Bot Configuration
load_dotenv()
BOT_TOKEN = os.getenv("TELEBOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN, parse_mode='markdown')

# Echo everything.
@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)

if __name__ == "__main__":
    # Start the bot.
    print("[Started Bot]")
    bot.infinity_polling()