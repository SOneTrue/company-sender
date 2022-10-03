import asyncio
import random

from aiogram import Dispatcher, Bot, types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from tgbot.config import load_config
from tgbot.keyboards.reply import old_years, orders
from tgbot.misc.states import Name

config = load_config(".env")
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')


async def add_user_name(message: Message, state: FSMContext):
    if not message.text == '/start':
        await state.update_data(name_user=message.text)
        await message.answer(f'Дата заказа?\n'
                             f'Формат - дд.мм.гг.')
        await Name.send_date_order.set()
    else:
        await message.answer("⛔️Не верное имя или неправильно заполнено поле, повторите ввод ФИО!")
        await Name.send_name.set()


async def add_date_order(message: Message, state: FSMContext):
    if message.text != '/start':
        await state.update_data(data_order=message.text)
        await message.answer(f'Время подачи транспорта?\n'
                             f'Формат - чч.мм.')
        await Name.send_time_order.set()
    else:
        await message.answer("Вы начали заново - введите Имя для дальнейшей работы.")
        await Name.send_name.set()


async def add_address_start(message: Message, state: FSMContext):
    if not message.text == '/start':
        await state.update_data(time_car=message.text)
        await message.answer(f'Адрес подачи транспорта?\n'
                             f'Формат - Город, улица, дом если есть. Ссылка отметки на карте, (по возможности)')
        await Name.send_address_start.set()
    else:
        await message.answer("Вы начали заново - введите Имя для дальнейшей работы.")
        await Name.send_name.set()


async def add_address_end(message: Message, state: FSMContext):
    if not message.text == '/start':
        await state.update_data(address_start=message.text)
        await message.answer(f'Адрес места назначения?\n'
                             f'Формат - Город, улица, дом если есть. Ссылка отметки на карте, (по возможности).')
        await Name.send_address_end.set()
    else:
        await message.answer("Вы начали заново - введите Имя для дальнейшей работы.")
        await Name.send_name.set()


async def add_time_end(message: Message, state: FSMContext):
    if not message.text == '/start':
        await state.update_data(address_end=message.text)
        await message.answer(f'Время окончания заказа?\n'
                             f'Формат - чч.мм.')
        await Name.send_time_end.set()
    else:
        await message.answer("Вы начали заново - введите Имя для дальнейшей работы.")
        await Name.send_name.set()


async def add_quantity_people(message: Message, state: FSMContext):
    if not message.text == '/start':
        await state.update_data(time_end=message.text)
        await message.answer(f'Количество пассажиров?')
        await Name.send_quantity_people.set()
    else:
        await message.answer("Вы начали заново - введите Имя для дальнейшей работы.")
        await Name.send_name.set()


async def add_age(message: Message, state: FSMContext):
    if not message.text == '/start':
        await state.update_data(quantity_people=message.text)
        await message.answer(f'Дети или взрослые?', reply_markup=old_years)
        await Name.send_age.set()
    else:
        await message.answer("Вы начали заново - введите Имя для дальнейшей работы.")
        await Name.send_name.set()


async def add_comments(message: Message, state: FSMContext):
    if not message.text == '/start':
        reply_markup = types.ReplyKeyboardRemove()
        await state.update_data(age=message.text)
        await message.answer(
            f'Примечания по маршруту (здесь вы можете указать остановочные пункты или места куда еще надо заехать)?',
            reply_markup=reply_markup)
        await Name.send_comments.set()
    else:
        await message.answer("Вы начали заново - введите Имя для дальнейшей работы.")
        await Name.send_name.set()


async def add_others_options(message: Message, state: FSMContext):
    if not message.text == '/start':
        await state.update_data(comments=message.text)
        await message.answer(f'Дополнительные опции (багажник, микрофон и т.д.)?')
        await Name.send_personal_info.set()
    else:
        await message.answer("Вы начали заново - введите Имя для дальнейшей работы.")
        await Name.send_name.set()


async def add_personal_info(message: Message, state: FSMContext):
    if not message.text == '/start':
        await state.update_data(others_options=message.text)
        await message.answer(f'Контактное лицо?\n'
                             f'Формат - Имя, Фамилия.')
        await Name.send_others_options.set()
    else:
        await message.answer("Вы начали заново - введите Имя для дальнейшей работы.")
        await Name.send_name.set()


async def add_phone_number(message: Message, state: FSMContext):
    if not message.text == '/start':
        await state.update_data(personal_info=message.text)
        await message.answer(f'Номер телефона, с кем связаться по заказу?\n'
                             f'Формат - +7(9хх)ххх-хх-хх')
        await Name.send_phone_number.set()
    else:
        await message.answer("Вы начали заново - введите Имя для дальнейшей работы.")
        await Name.send_name.set()


async def add_find_us(message: Message, state: FSMContext):
    if not message.text == '/start':
        await state.update_data(phone_number=message.text)
        await message.answer(f'Откуда о нас узнали?')
        await Name.send_find_us.set()
    else:
        await message.answer("Вы начали заново - введите Имя для дальнейшей работы.")
        await Name.send_name.set()



async def add_payment(message: Message, state: FSMContext):
    if not message.text == '/start':
        await state.update_data(times_order=message.text)
        await message.answer(f'Способ оплаты?', reply_markup=orders)
        await Name.send_payment.set()
    else:
        await message.answer("Вы начали заново - введите Имя для дальнейшей работы.")
        await Name.send_name.set()


async def send_group_info(message: Message, state: FSMContext):
    if not message.text == '/start':
        reply_markup = types.ReplyKeyboardRemove()
        number_order = random.randint(10000, 10000000)
        await message.answer(f'Успешно заполнено, ваш уникальный номер заказа <b>№ {number_order}</b>.', reply_markup=reply_markup)
        user_data = await state.get_data()
        text_user = f'Заказ <b>№ {number_order}</b>. \n' \
                    f'Заказчик: {user_data["name_user"]}\n' \
                    f'Дата: {user_data["data_order"]}\n' \
                    f'Время выезда: {user_data["time_car"]}\n' \
                    f'Откуда: {user_data["address_start"]}\n' \
                    f'Куда: {user_data["address_end"]}\n' \
                    f'Время окончания заказа: {user_data["time_end"]}\n' \
                    f'Количество пассажиров: {user_data["quantity_people"]}\n' \
                    f'Дети или взрослые: {user_data["age"]}\n' \
                    f'Уточнения по маршруту: {user_data["comments"]}\n' \
                    f'Дополнительные опции: {user_data["others_options"]}\n'
        await bot.send_message(chat_id=config.tg_bot.group, text=text_user)

        text_group = f'Контактное лицо: {user_data["personal_info"]}\n' \
                     f'Номер телефона: {user_data["phone_number"]}\n' \
                     f'Количество часов заказа: {user_data["times_order"]}\n' \
                     f'Оплата: {message.text}\n'
        await bot.send_message(chat_id=config.tg_bot.group, text=text_group)
        await state.reset_state(with_data=True)
    else:
        await message.answer("Вы начали заново - Имя для дальнейшей работы.")
        await Name.send_name.set()


def register_info(dp: Dispatcher):
    dp.register_message_handler(add_user_name, state=Name.send_name)
    dp.register_message_handler(add_date_order, state=Name.send_date_order)
    dp.register_message_handler(add_address_start, state=Name.send_time_order)
    dp.register_message_handler(add_address_end, state=Name.send_address_start)
    dp.register_message_handler(add_time_end, state=Name.send_address_end)
    dp.register_message_handler(add_quantity_people, state=Name.send_time_end)
    dp.register_message_handler(add_age, state=Name.send_quantity_people)
    dp.register_message_handler(add_comments, state=Name.send_age)
    dp.register_message_handler(add_others_options, state=Name.send_comments)
    dp.register_message_handler(add_personal_info, state=Name.send_personal_info)
    dp.register_message_handler(add_phone_number, state=Name.send_others_options)
    dp.register_message_handler(add_find_us, state=Name.send_phone_number)
    dp.register_message_handler(add_payment, state=Name.send_find_us)
    dp.register_message_handler(send_group_info, state=Name.send_payment)
