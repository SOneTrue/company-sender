import asyncio
import random

from aiogram import Dispatcher, Bot, types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from tgbot.config import load_config
from tgbot.middlewares.throttling import rate_limit
from tgbot.misc.states import Name

config = load_config(".env")
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')


async def add_user_name(message: Message, state: FSMContext):
    if not message.text == '/start':
        name_user = message.text
        await state.update_data(name_user=name_user)
        await message.answer(f'Дата заказа?')
        await Name.send_date_order.set()
    else:
        await message.answer("⛔️Не верное имя или неправильно заполнено поле, повторите ввод ФИО!")
        await Name.send_name.set()


async def add_date_order(message: Message, state: FSMContext):
    if message.text != '/start':
        data_order = message.text
        await state.update_data(data_order=data_order)
        await message.answer(f'Время подачи транспорта?')
        await Name.send_time_order.set()
    else:
        await message.answer("Вы начали заново - введите Имя для дальнейшей работы.")
        await Name.send_name.set()


async def add_address_car(message: Message, state: FSMContext):
    if not message.text == '/start':
        time_car = message.text
        await state.update_data(time_car=time_car)
        await message.answer(f'Адрес подачи транспорта?')
        await Name.send_address_car.set()
    else:
        await message.answer("Вы начали заново - введите Имя для дальнейшей работы.")
        await Name.send_name.set()


async def add_address_site(message: Message, state: FSMContext):
    if not message.text == '/start':
        address_car = message.text
        await state.update_data(address_car=address_car)
        await message.answer(f'Адрес места назначения?')
        await Name.send_address_site.set()
    else:
        await message.answer("Вы начали заново - введите Имя для дальнейшей работы.")
        await Name.send_name.set()


async def add_comments_site(message: Message, state: FSMContext):
    if not message.text == '/start':
        address_site = message.text
        await state.update_data(address_site=address_site)
        await message.answer(
            f'Уточнения по маршруту (здесь вы можете указать остановочные пункты или места куда еще надо заехать)?')
        await Name.send_comments_site.set()
    else:
        await message.answer("Вы начали заново - введите Имя для дальнейшей работы.")
        await Name.send_name.set()


async def add_time_end(message: Message, state: FSMContext):
    if not message.text == '/start':
        comments_site = message.text
        await state.update_data(comments_site=comments_site)
        await message.answer(f'Время окончания заказа?')
        await Name.send_time_end.set()
    else:
        await message.answer("Вы начали заново - введите Имя для дальнейшей работы.")
        await Name.send_name.set()


async def add_quantity_people(message: Message, state: FSMContext):
    if not message.text == '/start':
        time_end = message.text
        await state.update_data(time_end=time_end)
        await message.answer(f'Количество пассажиров?')
        await Name.send_quantity_people.set()
    else:
        await message.answer("Вы начали заново - введите Имя для дальнейшей работы.")
        await Name.send_name.set()


async def add_age(message: Message, state: FSMContext):
    if not message.text == '/start':
        quantity_people = message.text
        await state.update_data(quantity_people=quantity_people)
        await message.answer(f'Дети или взрослые?')
        await Name.send_age.set()
    else:
        await message.answer("Вы начали заново - введите Имя для дальнейшей работы.")
        await Name.send_name.set()


async def add_phone_number(message: Message, state: FSMContext):
    if not message.text == '/start':
        age = message.text
        await state.update_data(age=age)
        await message.answer(f'Имя и номер телефона, с кем связаться по заказу?')
        await Name.send_phone_number.set()
    else:
        await message.answer("Вы начали заново - введите Имя для дальнейшей работы.")
        await Name.send_name.set()


async def add_others_options(message: Message, state: FSMContext):
    if not message.text == '/start':
        phone_number = message.text
        await state.update_data(phone_number=phone_number)
        await message.answer(f'Дополнительные опции (багажник, микрофон и т.д.)?')
        await Name.send_others_options.set()
    else:
        await message.answer("Вы начали заново - введите Имя для дальнейшей работы.")
        await Name.send_name.set()


async def add_find_us(message: Message, state: FSMContext):
    if not message.text == '/start':
        others_options = message.text
        await state.update_data(others_options=others_options)
        await message.answer(f'Откуда о нас узнали?')
        await Name.send_find_us.set()
    else:
        await message.answer("Вы начали заново - введите Имя для дальнейшей работы.")
        await Name.send_name.set()


async def add_send_comments(message: Message, state: FSMContext):
    if not message.text == '/start':
        number_order = random.randint(1, 10000)
        await message.answer(f'Успешно заполнено, ваш уникальный номер заказа <b>№ {number_order}</b>.')
        user_data = await state.get_data()
        text_user = f'Заказ <b>№ {number_order}</b>. \n' \
                    f'Имя заказчика: {user_data["name_user"]}\n' \
                    f'Дата заказа: {user_data["data_order"]}\n' \
                    f'Время подачи: {user_data["time_car"]}\n' \
                    f'Адрес подачи: {user_data["address_car"]}\n' \
                    f'Адрес места назначения: {user_data["address_site"]}\n' \
                    f'Уточнения по маршруту: {user_data["comments_site"]}\n' \
                    f'Время окончания заказа: {user_data["time_end"]}\n' \
                    f'Количество пассажиров: {user_data["quantity_people"]}\n' \
                    f'Дети или взрослые: {user_data["age"]}\n' \
                    f'Номер телефона: {user_data["phone_number"]}\n' \
                    f'Дополнительные опции: {user_data["others_options"]}\n' \
                    f'Откуда о нас узнали: {message.text}'
        await bot.send_message(chat_id=config.tg_bot.group, text=text_user)
        await state.reset_state(with_data=True)
        await state.finish()
    else:
        await message.answer("Вы начали заново - Имя для дальнейшей работы.")
        await Name.send_name.set()


def register_info(dp: Dispatcher):
    dp.register_message_handler(add_user_name, state=Name.send_name)
    dp.register_message_handler(add_date_order, state=Name.send_date_order)
    dp.register_message_handler(add_address_car, state=Name.send_time_order)
    dp.register_message_handler(add_address_site, state=Name.send_address_car)
    dp.register_message_handler(add_comments_site, state=Name.send_address_site)
    dp.register_message_handler(add_time_end, state=Name.send_comments_site)
    dp.register_message_handler(add_quantity_people, state=Name.send_time_end)
    dp.register_message_handler(add_age, state=Name.send_quantity_people)
    dp.register_message_handler(add_phone_number, state=Name.send_age)
    dp.register_message_handler(add_others_options, state=Name.send_phone_number)
    dp.register_message_handler(add_find_us, state=Name.send_others_options)
    dp.register_message_handler(add_send_comments, state=Name.send_find_us, )
