from telegram import Bot

from helpers.mlwrappers import AWSRecognizer, NumdlWrapper


class BotExt(Bot):
    def __init__(self, token):
        super().__init__(token=token)
        self.aws_wrapper = AWSRecognizer()
        self.numdl_wrapper = NumdlWrapper('./resources/model.pickle')
        self.current_backend = self.numdl_wrapper

    def switch_backend(self):
        if self.current_backend != self.aws_wrapper:
            self.current_backend = self.aws_wrapper
        else:
            self.current_backend = self.numdl_wrapper
