from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging
from telegram import Bot

class CjsBot:
    __location_key = '/home/augusto/.telegramapi/key'
    __location_id = '/home/augusto/.telegramapi/id'
    def __init__(self):
        token = open(self.__location_key).read()
        self.id_user = int(open(self.__location_id).read())
        self.bot = Bot(token = token)
        self.updater = Updater(token=token, use_context=True)
        self.dispatcher = self.updater.dispatcher
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
        
        #start_handler = CommandHandler('start', start)
        #dispatcher.add_handler(start_handler)

    def start(self, updater):
        updater.start_polling()
    
    
    def send_message(self, message):
        self.bot.send_message(self.id_user, message)
    
        



