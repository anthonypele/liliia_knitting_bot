from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

import logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Paste your token from BotFather here
TOKEN = "8243307294:AAH5PZRbvrFpgW6HbETlQrFwPyGskgCab7U"

# /start command → show button
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("👋 Introduce Me!", callback_data="intro")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Welcome to Liliia's Knitting Bot! 🧶\nPress the button below:",
        reply_markup=reply_markup
    )

# Handle button press
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "intro":
        with open("photo_2025-09-19_15-40-00.jpg", "rb") as photo:  # <-- put your local file here
            await query.message.reply_photo(
                photo=photo,
                caption="Привет, я Лиля 🤗\nЯ провожу встречи по вязанию для начинающих и более опытных!"
            )

def main():
    app = Application.builder().token(TOKEN).build()

    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    # Run bot until Ctrl+C
    app.run_polling()

if __name__ == "__main__":
    main()
