from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackContext
# import test

from test2 import give_it_out
from datetime import datetime

TOKEN: Final = "6518477245:AAH9xy4VL3QChqvXV67rPTUKMuBFmiAqyuQ"
BOT_USERNAME: Final = "@dailybites_bot"
time = datetime.now()
# Commands
async def start_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hey there Rupali!!, let's get your daily bites😉")

async def dailybite_command(update: Update, context:ContextTypes.DEFAULT_TYPE):

    bite = give_it_out()
    await update.message.reply_text(bite)


async def help_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Use the daily bite command to get your daily bites.")


async def meaning_command(update: Update, context: CallbackContext) -> None:
    # Extract the word from the command
    word = context.args[0] if context.args else None

    if word:
        # Run your function to get the meaning (replace with your logic)
        meaning = get_word_definition(word, AllAPI.API)

        # Send the meaning back to the user
        await update.message.reply_text(f'The meaning of "{word}" is:\n{meaning}')
    else:
        await update.message.reply_text('Please provide a word. Example: /meaning apple')

# Responses
def handle_responses(text: str)->str:
    beautify: str = text.lower()
    if 'hey' in beautify:
        return "hey there!!"

    return "i don't understand what you wrote."


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f"User ({update.message.chat.id}) in {message_type} put the daily bite at {time}.")

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_responses(new_text)
        else:
            return
    else:
        return handle_responses(text)

    print('Bot: ', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"update {update} caused error {context.error}")




if __name__ == '__main__':
    print("Starting Bot......")
    app = Application.builder().token(TOKEN).build()

    #Command handler
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('dailybite', dailybite_command))
    app.add_handler(CommandHandler('meaning', meaning_command))


    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))


    # Eroor Handler
    app.add_error_handler(error)

    print("Polling now....")
    app.run_polling(poll_interval=3)
