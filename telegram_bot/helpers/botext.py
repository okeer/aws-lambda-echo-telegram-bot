from telegram import Bot


class BotExt(Bot):
    def __init__(self, token, wrappers):
        super().__init__(token=token)
        self.wrappers = wrappers
        self.images_ids_for_chats = {}

    def backend_selector(self, query):
        return next((wrapper for wrapper in self.wrappers if type(wrapper).NAME in query), None)
