import logging
import time

from aiogram import types
from aiogram.utils import executor

from bot.config import *
from bot.keyboards.inline.job_type import categories_markup, jobs
from bot.messages.messages import MESSAGES
from bot.states.states import TestStates


@dp.callback_query_handler(lambda c: jobs.__contains__(c.data))
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, f'Нажата кнопка! {callback_query.data}')


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(MESSAGES.start.value)
    await show_typing(message)
    await bot.send_message(message.chat.id, MESSAGES.choose_job.value, reply_markup=categories_markup())


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(MESSAGES['help'])


async def on_startup(dp):
    logging.basicConfig(level=logging.INFO)
    # db.create_tables()

    await bot.delete_webhook()
    await bot.set_webhook(WEBHOOK_URL)


async def on_shutdown(dp):
    logging.warning("Shutting down..")
    await bot.delete_webhook()
    await dp.storage.close()
    await dp.storage.wait_closed()
    logging.warning("Bot down")


@dp.message_handler(state='*', commands=['setstate'])
async def process_setstate_command(message: types.Message):
    argument = message.get_args()
    state = dp.current_state(user=message.from_user.id)
    if not argument:
        await state.reset_state()
        return await message.reply(MESSAGES['state_reset'])

    if (not argument.isdigit()) or (not int(argument) < len(TestStates.all())):
        return await message.reply(MESSAGES['invalid_key'].format(key=argument))

    await state.set_state(TestStates.all()[int(argument)])
    await message.reply(MESSAGES['state_change'], reply=False)


@dp.message_handler(state=TestStates.TEST_STATE_1)
async def first_test_state_case_met(message: types.Message):
    await message.reply('Первый!', reply=False)


@dp.message_handler(state=TestStates.TEST_STATE_2[0])
async def second_test_state_case_met(message: types.Message):
    await message.reply('Второй!', reply=False)


@dp.message_handler(state=TestStates.TEST_STATE_3 | TestStates.TEST_STATE_4)
async def third_or_fourth_test_state_case_met(message: types.Message):
    await message.reply('Третий или четвертый!', reply=False)


@dp.message_handler(state=TestStates.all())
async def some_test_state_case_met(message: types.Message):
    with dp.current_state(user=message.from_user.id) as state:
        text = MESSAGES['current_state'].format(
            current_state=await state.get_state(),
            states=TestStates.all()
        )
    await message.reply(text, reply=False)


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


async def show_typing(message, wait=1):
    await bot.send_chat_action(message.chat.id, "typing")
    time.sleep(wait)


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
