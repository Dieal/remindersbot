import os
from dotenv import load_dotenv
import logging
import promemoriaAdder
from telegram import Update
from telegram.ext import (
    Application,
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

# Env File and Api Key
load_dotenv()
API_KEY = os.getenv('API_KEY')

# Logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Init Application
TIME, DAY, TEXT = range(3)
def initApplication():

    # Application
    application = ApplicationBuilder().token(API_KEY).build()

    # Command Handlers
    start_handler = CommandHandler('start', start)

    # Conversation Handler
    # promemoria_handler = CommandHandler('promemoria', promemoriaAdder.promemoria)
    conv_handler = promemoriaAdder.conversationHandler

    application.add_handler(conv_handler)


    application.add_handler(start_handler)
    # application.add_handler(promemoria_handler)

    return application

# Start Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="""
    Benvenuto nel Reminder Bot!
    Digita /promemoria per salvare un promemoria
    """)

if __name__ == '__main__':
    application = initApplication()
    application.run_polling(allowed_updates=Update.ALL_TYPES)

