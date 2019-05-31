import json
import os
import traceback

from telegram import Bot, Update
from telegram.ext import Dispatcher

from helpers.handlers import *

bot = Bot(token=os.environ['api_key'])

dispatcher = Dispatcher(bot, None)
dispatcher.add_handler(CustomConvHandler())


def webhook(event, context):
    try:
        dispatcher.process_update(Update.de_json(json.loads(event["body"]), bot))
    except Exception as e:
        print("Failed to process webhook: {0}".format(e))
        traceback.print_exc()
        return {"statusCode": 500}

    return {"statusCode": 200}
