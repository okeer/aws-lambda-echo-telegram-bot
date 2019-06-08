from helpers.converters import download_file, compose_reply


def on_aws_cmd_handler(bot, update):
    bot.switch_backend()


def on_photo_received_handler(bot, update):
    file_bytes = download_file(bot, update.message.photo[-1].file_id)
    data = bot.current_backend.classify(file_bytes)

    repl = "Nice image! Looks like it has:\n"
    repl += compose_reply(data)
    repl += f">>> Brought to you by {type(bot.current_backend).NAME} backend"

    update.message.reply_text(repl)
