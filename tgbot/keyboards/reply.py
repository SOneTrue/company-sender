from tgbot.filters.settings_buttons import ListOfButtons

old_years = ListOfButtons(text=['Дети', 'Взрослые'],
                              callback=['kid', 'adults'],
                              align=[2]).reply_keyboard

orders = ListOfButtons(text=['По карте', 'По счёту'],
                              callback=['card', 'score'],
                              align=[2]).reply_keyboard