from handlers.handler_com import HandlerCom
from handlers.handler_pdf_split import HandlerSplit

# The class responsible for running all handlers
class HandlerMain:

    def __init__(self, bot):
        self.handler_com = HandlerCom(bot)
        self.handler_split = HandlerSplit(bot)

    def handle(self):
        self.handler_com.handle()
        self.handler_split.handle()