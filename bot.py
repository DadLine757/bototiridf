import telebot, hashlib, secrets, json, os

API_TOKEN = "7743912048:AAHrpMW-UdYmYANOjOANs1bm5jDRyC1-p_8"
ADMIN_IDS = [8079695166, 5772226790]

bot = telebot.TeleBot(API_TOKEN)

KEYS_FILE = "keys.json"

def save_key(hash_key):
    if not os.path.exists(KEYS_FILE):
        with open(KEYS_FILE, 'w') as f:
            json.dump([], f)

    with open(KEYS_FILE, 'r+') as f:
        keys = json.load(f)
        keys.append(hash_key)
        f.seek(0)
        json.dump(keys, f)

@bot.message_handler(commands=['getkey'])
def getkey(message):
    if message.from_user.id not in ADMIN_IDS:
        bot.reply_to(message, "⛔ Доступ запрещен. Вы не админ.")
        return

    key = secrets.token_hex(16)
    hash_key = hashlib.sha256(key.encode()).hexdigest()
    save_key(hash_key)
    bot.send_message(message.chat.id, f"🔐 Ваш ключ:
`{key}`", parse_mode="Markdown")

bot.polling()