import os

from settings.config import BOT_TOKEN
from handlers.handler_main import HandlerMain
from telebot import TeleBot

from settings.config import PDF_DIR, SPLITED_FILES_DIR, RAR_FILES_DIR

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

    pathes = [f'{PDF_DIR}', f'{SPLITED_FILES_DIR}', f'{RAR_FILES_DIR}']
    for path in pathes:
        if not os.path.exists(path):
            os.mkdir(path)

    print('Starting bot...')
    PDFDead().start()
