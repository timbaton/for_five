import logging

from aiogram import types
from aiogram.utils import executor

from bot.config import *

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


async def on_startup(dp):
    logging.basicConfig(level=logging.INFO)
    # db.create_tables()

    await bot.delete_webhook()
    await bot.set_webhook(WEBHOOK_URL)


async def on_shutdown():
    logging.warning("Shutting down..")
    await bot.delete_webhook()
    await dp.storage.close()
    await dp.storage.wait_closed()
    logging.warning("Bot down")


if __name__ == '__main__':
    if mode == "dev":
        executor.start_polling(dp, on_startup=on_startup, skip_updates=False)
    else:
        executor.start_webhook(
            dispatcher=dp,
            webhook_path=WEBHOOK_PATH,
            skip_updates=True,
            on_startup=on_startup,
            on_shutdown=on_shutdown,
            host=WEBAPP_HOST,
            port=WEBAPP_PORT,
        )
