import telebot
import random
import threading
from flask import Flask

TOKEN = 9214904316:AAECofBCSq3xEpShpftVSUbSR3FyuYNoMW0
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "البوت شغال"

replies = [
    "ازيك ي صاحبي عامل ايه",
    "اهلا اهلا نورتنا والله",
    "حبيبي عامل ايه اخبارك",
    "ازيك ي وحش وحشني",
    "اهلا بيك ي غالي",
    "نورت الدنيا كلها",
    "ازيك ي صاحبي طمني عليك",
    "حبيب قلبي عامل ايه",
    "اهلا ي بطل",
    "ازيك ي جدع",
    "منور يا صاحبي",
    "اخبارك ايه طمني",
    "اهلا وسهلا بيك",
    "ازيك ي غالي عامل ايه",
    "حبيبي نورت",
    "يا هلا يا هلا",
    "ازيك ي عم الناس",
    "عامل ايه ي صاحبي",
    "اهلا ي وحش",
    "نورتنا يا غالي",
    "ازيك ي حبيبي",
    "طمني عليك عامل ايه",
    "اهلا بيك نورت",
    "ازيك ي رايق",
    "حبيبي عامل ايه فينك",
    "اهلا اهلا يا غالي",
    "ازيك ي صاحبي وحشني والله",
    "نورت يا وحش",
    "عامل ايه يا بطل",
    "اهلا بيك يا جدع",
    "ازيك يا عم",
    "حبيب قلبي نورت",
    "ازيك ي صاحبي اخبارك ايه",
    "اهلا يا حبيبي",
    "منور الدنيا يا صاحبي",
    "ازيك ي غالي وحشني",
    "عامل ايه يا حبيب قلبي",
    "اهلا وسهلا نورت",
    "ازيك ي صاحبي فينك كده",
    "حبيبي اهلا بيك",
    "نورت يا غالي والله",
    "ازيك يا جدع عامل ايه",
    "اهلا يا عم الناس",
    "طمني عليك يا صاحبي",
    "ازيك يا وحش عامل ايه",
    "حبيبي منور",
    "اهلا بيك يا بطل",
    "ازيك ي صاحبي الدنيا عاملة ايه معاك",
    "نورتنا يا حبيبي",
    "اهلا يا غالي عامل ايه"
]

contact_text = """لو عايز تتواصل معايا يا صاحبي ❤️

1- تيك توك: @hamody.59
2- انستجرام: @ahmed_3_7_2009
3- سناب شات: @hamody.59
4- واتساب: 01158705959

مستنيك يا وحش 🔥"""

@bot.message_handler(commands=['start', 'hi', 'hello'])
def start(message):
    bot.reply_to(message, random.choice(replies) + "\n\nلو عايز تتواصل معايا ابعت /تواصل")

@bot.message_handler(commands=['تواصل', 'contact'])
def contact(message):
    bot.reply_to(message, contact_text)

@bot.message_handler(func=lambda m: True)
def reply_all(message):
    text = message.text.lower()
    if "تواصل" in text or "اتكلم" in text or "كلمك" in text or "رقمك" in text or "انستا" in text or "تيك توك" in text:
        bot.reply_to(message, contact_text)
    else:
        bot.reply_to(message, random.choice(replies))

def run_bot():
    bot.infinity_polling()

threading.Thread(target=run_bot).start()

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
