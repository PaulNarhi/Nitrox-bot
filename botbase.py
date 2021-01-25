#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Welcome to Nitrox blend bot. Use /new to start blending!')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def confirm(update, context):
    """Echo the user message."""
    update.message.reply_text("you have: " + update.message.text[0:2] + "L of volume, " + "EAN"+update.message.text[3:7]
    + " @" + update.message.text[8:10] + " bar")
    update.message.reply_text('Use /Y to confirm or /N to start again.')


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def newMix(update, context):
    """Log Errors caused by Updates."""
    update.message.reply_text("""Lets start by setting the current gas! Provide tank size, EANX, 
    and pressure in format:\n[tankTotalVolume:O2%:Bar] -> 24:32.4:54""")

def wantedMix(update, context):
    update.message.reply_text('Mix confirmed!')


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1529293775:AAHmA4yctwk4nrg6CKm-7G1j4K-1o1kjoSk", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("new", newMix))
    dp.add_handler(CommandHandler("Y", wantedMix))
    dp.add_handler(CommandHandler("N", newMix))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, confirm))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()