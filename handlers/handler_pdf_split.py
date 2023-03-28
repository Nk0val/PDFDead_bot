from handlers.handler import Handler
from services.download_pdf import Download_pdf
from services.pdf_spliter import Split
from services.create_rar import  Create_rar
from settings.utils import Clear_all
from settings.config import PDF_DIR, RAR_FILES_DIR

class HandlerSplit(Handler):

    def __init__(self, bot):
        super().__init__(bot)

    def user_send_file(self, message):
        if message.document.mime_type == 'application/pdf':

            self.status_text, self.status_code, self.file_name = Download_pdf(self.bot, message)
            self.bot.send_message(message.chat.id, self.status_text)

            if self.status_code == 0:
                self.bot.send_message(message.chat.id, "Now, send me split step")

                @self.bot.message_handler(func=lambda m: self.status_code == 0)
                def handler(message1):
                    username = message1.from_user.first_name

                    self.bot.send_message(message.chat.id, "Started splitting your file!")

                    file_path = f'./{PDF_DIR}/{username}/{self.file_name}_by_{message.from_user.first_name}.pdf'

                    status_text, status_code = Split(file_path, self.file_name, int(message1.text), username)
                    self.bot.send_message(message1.chat.id, status_text)

                    status_text = Create_rar(username)
                    self.bot.send_message(message1.chat.id, status_text)

                    self.bot.send_document(message1.chat.id, open(f'{RAR_FILES_DIR}/{username}/{username}.rar', 'rb'))
                    self.bot.send_message(message1.chat.id, "You're splitted pdf!")

                    Clear_all(username)

                    self.status_code = 1




        else:
            self.bot.send_message(message.chat.id, "Sorry, but it's not a pdf file...")

    def handle(self):

        @self.bot.message_handler(content_types='document')
        def get_pdf_file(message):
            self.user_send_file(message)
