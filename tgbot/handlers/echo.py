from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from tgbot.middlewares.throttling import rate_limit


async def bot_echo(message: types.Message, state: FSMContext):
    text = [
        f'⛔️ Введены неверные данные, перепроверьте что требуется отправить, текст или фотографию!\n'
        f'Для того что бы начать сначала нажмите /start'
    ]

    await message.answer('\n'.join(text))


async def bot_echo_all(message: types.Message, state: FSMContext):
    text = [
        f'⛔️ Введены неверные данные, перепроверьте что требуется отправить, текст или фотографию!\n'
        f'Для того что бы начать сначала нажмите /start'
    ]
    await message.answer('\n'.join(text))


def register_echo(dp: Dispatcher):
    dp.register_message_handler(bot_echo, rate_limit(5))
    dp.register_message_handler(bot_echo_all, rate_limit(5), state="*", content_types=types.ContentTypes.ANY)
