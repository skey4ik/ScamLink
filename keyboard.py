from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from settings import qiwi_nick, price

#Кнопка регистрации
kb_reg = ReplyKeyboardMarkup(resize_keyboard=True)
reg_button = KeyboardButton("Зарегистрироваться", request_contact=True)
kb_reg.add(reg_button)

#Кнопка меню
kb_menu = ReplyKeyboardMarkup(resize_keyboard=True)
gifts_button = KeyboardButton("Бесплатные подарки")
shop_button = KeyboardButton("Магазин")
kb_menu.add(gifts_button, shop_button)

#Кнопка Беспалтные подарки
kb_gifts = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
promo_button = KeyboardButton('Промокод')
back_button = KeyboardButton('Назад')
kb_gifts.add(promo_button).insert(back_button)

#Кнопка Магазина
kb_shop = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
ScamLink_button = KeyboardButton("Scam link")
back_button = KeyboardButton('Назад')
kb_shop.add(ScamLink_button).insert(back_button)

#Кнопка Выполнил (inline)
ikb_promo = InlineKeyboardMarkup(row_width=1)
get_promo_button = InlineKeyboardButton(text="Выполнил", callback_data='get_promo')
ikb_promo.add(get_promo_button)

#меню покупки scamlink (inline)
ikb_scamlink = InlineKeyboardMarkup(row_width=1)
buy_button = InlineKeyboardButton(text='Купить', callback_data='buy')
ikb_scamlink.add(buy_button)

#Покупка scamlink (inline)
ikb_in_buy_button = InlineKeyboardMarkup(row_width=1)
qiwi_button = InlineKeyboardButton(text='Оплатить QIWI', callback_data='qiwi', url=f'https://qiwi.com/payment/form/99999?extra%5B%27account%27%5D={qiwi_nick}&amountInteger={price}&amountFraction=0&currency=643&blocked[0]=account')
oplata_check_button = InlineKeyboardButton(text='Проверить', callback_data='check')
buy_back = InlineKeyboardButton(text='Назад', callback_data='buy_back')
ikb_in_buy_button.add(qiwi_button, oplata_check_button, buy_back)
