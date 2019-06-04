import json
import traceback

from telegram import Bot, Update
from telegram.ext import Dispatcher, MessageHandler, Filters

from helpers.handlers import *

api_key = os.environ['api_key']

bot = Bot(token=api_key)
handler = MessageHandler(Filters.photo, photo)


dispatcher = Dispatcher(bot, None)
dispatcher.add_handler(handler)


def webhook(event, context):
    try:
        dispatcher.process_update(Update.de_json(json.loads(event["body"]), bot))
    except Exception as e:
        print("Failed to process webhook: {0}".format(e))
        traceback.print_exc()
        return {"statusCode": 500}

    return {"statusCode": 200}
