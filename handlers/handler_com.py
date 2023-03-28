from handlers.handler import Handler


# The handler class responsible for handling all commands
class HandlerCom(Handler):

    def __init__(self, bot):
        super().__init__(bot)

    # Functions when the handler is triggered
    def pressed_start_btn(self, message):
        self.bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}, i ready to work!')

    def pressed_help_btn(self, message):
        self.bot.send_message(message.chat.id, 'Send me the pdf file and then the step to split the file.')

    # Handle function
    def handle(self):
        @self.bot.message_handler(commands=['start', 'help'])
        def handle(message):
            if message.text == '/start':
                self.pressed_start_btn(message)
            if message.text == '/help':
                self.pressed_help_btn(message)

