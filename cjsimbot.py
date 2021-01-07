from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging
from telegram import Bot

class CjsBot:
    

    def __init__(self):
        location_key = '/home/augusto/.telegramapi/key'
        location_id = '/home/augusto/.telegramapi/id'
        token = open(location_key).read()
        self.id_user = int(open(location_id).read())
        self.bot = Bot(token)
        self.updater = Updater(token, use_context=True)
        self.dispatcher = self.updater.dispatcher
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
        self.commands = {}


    def start(self):
        self.updater.stop()
        self.create_commandMessages()
        self.updater.start_polling()
    
    def create_commandMessages(self):
        if self.commands == {}: return False
        for command in self.commands.keys():
            handler = CommandHandler(command, lambda update,context: 
                context.bot.send_message(chat_id=update.effective_chat.id, text=self.commands[command]))
            self.dispatcher.add_handler(handler)

   
    def add_commandMessage(self, command, message):
        self.commands[command] = message
    
    def send_message(self, message):
        self.bot.send_message(self.id_user, message)
    
    
        



