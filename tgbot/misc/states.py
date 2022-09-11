from aiogram.dispatcher.filters.state import StatesGroup, State


class Name(StatesGroup):
    # Текстовая информация выезд
    send_name = State()
    send_date_order = State()
    send_time_order = State()
    send_address_car = State()
    send_address_site = State()
    send_comments_site = State()
    send_time_end = State()
    send_quantity_people = State()
    send_age = State()
    send_phone_number = State()
    send_others_options = State()
    send_payment = State()
    send_quantity_order = State()
    send_find_us = State()