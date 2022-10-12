import asyncio
import logging

from bot_creator import dp, bot
from handlers.help import *
from handlers.basket import *
from handlers.order_history import *
from handlers.order_start import *
from handlers.start import *
from handlers.order_close import *
from handlers.delivery_menu import *
from modules import database

logger = logging.getLogger(__name__)




async def main():
    # Database
    database.connect_database()

    # Logs
    logging.basicConfig(level=logging.INFO)
    logger.info("Bot Activated")

    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot Deactivated")
