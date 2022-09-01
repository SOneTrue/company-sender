from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from tgbot.misc.states import Name



async def user_start(message: Message, state: FSMContext):
    await state.reset_state(with_data=True)
    await message.answer("Здравствуйте, введите Имя.")
    await Name.send_name.set()


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"])