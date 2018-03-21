Token = ""

#!/usr/bin/env python
# -*- coding: utf-8 -*-



from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import random
from btc_price.btc_price import get_btc_price

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)



def start(bot, update):
    update.message.reply_text('De útil ate agora so faço café')


def falar(bot, update):
    """Adiciona falas comuns ao bot ao digitar o comando /falar

    Args:
        bot (bot): bot em execuçao
        update (Updater): objeto de atualizaçao do chat
    """
    dialogo = ["Vocês querem café?", "Não entendi", "Petrini explica para min isso daqui",
               "Tomei pau denovo", " (assobio)", "O que que foi fi?",
               "Esse tarique tem que deixar de ser vagabundo", "Café está pronto", "Comprou minha placa de video?"]
    bot.send_message(chat_id=update.message.chat_id,
                     text=random.choice(dialogo))


def help(bot, update):



def echo(bot, update):
    
    update.message.reply_text(update.message.text)


def error(bot, update, error):
   
    logger.warning('Update "%s" caused error "%s"', update, error)


def btc(bot, update):
    price = get_btc_price(convert="BRL", limit=10)
    message = f"Colé olha o preço ae:\n{price}\nDaora né? "
    update.message.reply_text(message)


def main():
 
    updater = Updater(Token)

    dp = updater.dispatcher

   
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("falar", falar))
    dp.add_handler(CommandHandler("btc", btc))
   
    dp.add_handler(MessageHandler(Filters.text, echo))

    
    dp.add_error_handler(error)

  
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()