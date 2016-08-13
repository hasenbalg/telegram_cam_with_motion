from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup
import logging
import requests


#setup keyboard
keyboard = [
			['/resume', '/pause'  ],
		   	['/status', '/restart']
			]

kb = ReplyKeyboardMarkup(keyboard)
kb.resize_keyboard =  True
kb.one_time_keyboard = False


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
					level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def status(bot, update):
	bot.sendMessage(update.message.chat_id, text=parse_answers(requests.get("http://r2.local:8080/0/detection/status").content), reply_markup=kb)

def restart(bot, update):
	bot.sendMessage(update.message.chat_id, text=parse_answers(requests.get("http://r2.local:8080/0/action/restart").content), reply_markup=kb)

def resume(bot, update):
	bot.sendMessage(update.message.chat_id, text=parse_answers(requests.get("http://r2.local:8080/0/detection/start").content), reply_markup=kb)

def pause(bot, update):
	bot.sendMessage(update.message.chat_id, text=parse_answers(requests.get("http://r2.local:8080/0/detection/pause").content), reply_markup=kb)

def help(bot, update):
	bot.sendMessage(update.message.chat_id, text='Help!')


def echo(bot, update):
	bot.sendMessage(update.message.chat_id, text=update.message.text)


def error(bot, update, error):
	logger.warn('Update "%s" caused error "%s"' % (update, error))

def parse_answers(answer):
	first = '</b>'
	last = '</body>'
	try:
		start = answer.rindex( first ) + len( first )
		end = answer.rindex( last, start )
		print answer[start:end] + '\n'
		return answer[start:end]
	except ValueError:
		return answer

def main():
	# Create the EventHandler and pass it your bot's token.
	updater = Updater('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

	# Get the dispatcher to register handlers
	dp = updater.dispatcher

	# on different commands - answer in Telegram
	dp.add_handler(CommandHandler("help", help))
	dp.add_handler(CommandHandler("resume", resume))
	dp.add_handler(CommandHandler("restart", restart))
	dp.add_handler(CommandHandler("status", status))
	dp.add_handler(CommandHandler("pause", pause))

	# on noncommand i.e message - echo the message on Telegram
	dp.add_handler(MessageHandler([Filters.text], echo))

	# log all errors
	dp.add_error_handler(error)

	# Start the Bot
	updater.start_polling()

	# Run the bot until the you presses Ctrl-C or the process receives SIGINT,
	# SIGTERM or SIGABRT. This should be used most of the time, since
	# start_polling() is non-blocking and will stop the bot gracefully.
	updater.idle()


if __name__ == '__main__':
	main()
