from settings.config import BOT_TOKEN
from handlers.handler_main import HandlerMain
from telebot import TeleBot


class PDFDead:

    def __init__(self):
        self.bot = TeleBot(BOT_TOKEN)

        self.main_handler = HandlerMain(self.bot)

    def run_handlers(self):
        self.main_handler.handle()

    def start(self):
        self.run_handlers()
        self.bot.polling(none_stop=True)


if __name__ == '__main__':
    print('Starting bot...')
    PDFDead().start()
