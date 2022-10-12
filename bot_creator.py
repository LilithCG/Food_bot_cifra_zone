import configparser

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

config = configparser.ConfigParser()
config.read("config.ini")

TOKEN = config["BOT"]["TOKEN"]

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)