import sqlite3 as sql
import settings
import main

import string
import secrets
from random import randint

#------------------Проверка на наличие в базе------------------
def user(user_id):
    conn = sql.connect('users.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS `users` (user_id INT PRIMARY KEY, nick TEXT, number INT)")
        info = cur.execute("SELECT * FROM users WHERE user_id = (?)", (user_id,))
        return info.fetchone()
    conn.commit()
    conn.close()

#------------------Вывод рандомного промокода------------------
rand_promo_num = randint(5,7)
random_promo = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(rand_promo_num))

promo_text = f'''⏬ ТВОЙ ПРОМОКОД – {random_promo}-×××××

✅ Для того что бы открыть промокод полностью, выполни условия, затем нажми на кнопку "Выполнил".

❌ Подпишись на – {settings.telegram_link1}
❌ Подпишись на – {settings.telegram_link2}

⏬ После успешного выполнения условий, ты сможешь забрать промокод. А так же, участвовать в приватных раздачах промокодов, и получать промокоды регулярно.'''

#------------------Скамлинк------------------
Scamlink_text = f'''⏬ SCAMLINK STANDOFF2
❓ Это софт для взлома STANDOFF2 аккаунтов через токен.

💰 Цена: {settings.price} РУБЛЕЙ

⏬ Для покупи нажми кнопку "Купить".

❗ Обработка заказа происходит за несколько минут, но может длится и до 24 часов.'''

def Scamlink_buy_text(chat_id):
    return f'''✅ Счет на оплату QIWI создан, нажмите 'Оплатить QIWI'.

Сумма к оплате: {settings.price} руб

В комментарии к переводу: свой ник - {chat_id}

После оплаты нажмите кнопку 'Проверить'.'''
