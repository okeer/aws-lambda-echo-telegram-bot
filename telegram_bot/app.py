import json
import traceback
import os

from telegram import Update
from telegram.ext import Dispatcher, MessageHandler, Filters, CommandHandler

from helpers.botext import BotExt
from helpers.handlers import on_photo_received_handler, on_aws_cmd_handler

api_key = os.environ['api_key']

bot = BotExt(token=api_key)
photo_handler = MessageHandler(Filters.photo, on_photo_received_handler)
aws_cmd_handler = CommandHandler('aws', on_aws_cmd_handler)


dispatcher = Dispatcher(bot, None)
dispatcher.add_handler(photo_handler)
dispatcher.add_handler(aws_cmd_handler)


def webhook(event, context):
    try:
        print(f'[INFO] Request to lambda is: {event["body"]}')
        dispatcher.process_update(Update.de_json(json.loads(event["body"]), bot))
    except Exception as e:
        print("Failed to process webhook: {0}".format(e))
        traceback.print_exc()
        return {"statusCode": 500}

    return {"statusCode": 200}
