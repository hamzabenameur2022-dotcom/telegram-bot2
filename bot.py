from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [["📦 منتجات", "💰 ربح"], ["📞 تواصل"]]
    reply_markup = ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    await update.message.reply_text("اختار 👇", reply_markup=reply_markup)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "📦 منتجات":
        await update.message.reply_text("قريب نبعثلك منتجات رابحة 😎")
    elif text == "💰 ربح":
        await update.message.reply_text("تنجم تربح بالدروبشيبينغ 💸")
    elif text == "📞 تواصل":
        await update.message.reply_text("تواصل معنا على @hamza_dropshop")

app = ApplicationBuilder().token("8732588517:AAGzwNWGKDfr9dFwwgcBwqV9SC7A4Ur75uk").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
