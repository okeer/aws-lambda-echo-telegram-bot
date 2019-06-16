from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from helpers.converters import download_file, compose_reply
from helpers.mlwrappers import AWSRecognizerWrapper, NumdlWrapper


def on_photo_received_handler(bot, update):
    bot.images_ids_for_chats[update.message.chat_id] = update.message.photo[-1].file_id
    update.message.reply_text("Select backend",
                              reply_markup=backend_menu_keyboard())


def on_backend_select_callback_handler(bot, update):
    query = update.callback_query
    current_backend = bot.backend_selector(query.data)

    if current_backend is None:
        query.edit_message_text(text="Backend is not supported")
        return
    elif query.message.chat_id not in bot.images_ids_for_chats:
        query.edit_message_text(text="Container was recycled due to timeout")
        return

    file_bytes = download_file(bot, bot.images_ids_for_chats[query.message.chat_id])
    data = current_backend.classify(file_bytes)

    query.edit_message_text(text=compose_reply(data, query.data), parse_mode=ParseMode.MARKDOWN)


def backend_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton(f'{NumdlWrapper.NAME}', callback_data=f'{NumdlWrapper.NAME} backend')],
        [InlineKeyboardButton(f'{AWSRecognizerWrapper.NAME}', callback_data=f'{AWSRecognizerWrapper.NAME} backend')]
    ]
    return InlineKeyboardMarkup(keyboard)
