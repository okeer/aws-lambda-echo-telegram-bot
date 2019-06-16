import json
import traceback
import os

from telegram import Update
from telegram.ext import Dispatcher, MessageHandler, Filters, CallbackQueryHandler

from helpers.botext import BotExt
from helpers.handlers import on_photo_received_handler, on_backend_select_callback_handler
from helpers.mlwrappers import AWSRecognizerWrapper, NumdlWrapper

api_key = os.environ['api_key']

bot = BotExt(token=api_key, wrappers=[AWSRecognizerWrapper(), NumdlWrapper('./resources/model.pickle')])
dispatcher = Dispatcher(bot, None)

dispatcher.add_handler(MessageHandler(Filters.photo, on_photo_received_handler))
dispatcher.add_handler(CallbackQueryHandler(on_backend_select_callback_handler, pattern='.*backend'))


def webhook(event, context):
    try:
        print(f'[INFO] Request to lambda is: {event["body"]}')
        dispatcher.process_update(Update.de_json(json.loads(event["body"]), bot))
    except Exception as e:
        print("Failed to process webhook: {0}".format(e))
        traceback.print_exc()
        return {"statusCode": 500}

    return {"statusCode": 200}
