import requests
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import F
import time
import random
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

keyboardStart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Royhatdan o\'tish boshlash'),
        ]
    ],
    resize_keyboard=True
)

API_TOKEN = '8124154284:AAHrXkW5RxaVrsJL_afJjiQfiyCqJVfEvzM'

# O'quvchilarning login va parollari
user_credentials = [
    { "username": "sherzodiusupova", "password": "11esinf" },
    { "username": "mavjudashokirova", "password": "11esinf" },
    { "username": "malika.yunusova12198", "password": "11esinf" },
    { "username": "nilufar_xoshimova", "password": "11esinf" },
    { "username": "gulixodjaxanova", "password": "11esinf" },
    { "username": "muborakturdiyeva", "password": "11esinf" },
    { "username": "mukhlisa.turdieva198", "password": "11esinf" },
    { "username": "tashmatovashaxnoza", "password": "11esinf" },
    { "username": "zulayxotadjibayeva", "password": "11esinf" },
    { "username": "dilnoza.riksiyeva", "password": "11esinf" },
    { "username": "myazzam", "password": "11esinf" },
    { "username": "muzaffar.nizamov", "password": "11esinf" },
    { "username": "azizjonnarmatov", "password": "11esinf" },
    { "username": "gulsara.muxamedova", "password": "11esinf" },
    { "username": "abduvsamad", "password": "11esinf" },
    { "username": "murodjonmirsaidov", "password": "11esinf" },
    { "username": "ulugbekkrimov", "password": "11esinf" },
    { "username": "movludakasimova", "password": "11esinf" },
    { "username": "etibor.kasimova", "password": "11esinf" },
    { "username": "gulyamovamarxamat", "password": "11esinf" },
    { "username": "zilolaashirmetova", "password": "11esinf" },
    { "username": "dilorom.azimova08198", "password": "11esinf" },
    { "username": "atabayevazubayda", "password": "11esinf" },
    { "username": "zubaydaatabayeva", "password": "11esinf" },
    { "username": "nigora.atabayeva", "password": "11esinf" },
    { "username": "abduvoxidatabayev", "password": "11esinf" },
    { "username": "abdusattoratabayev", "password": "11esinf" },
    { "username": "oynisaabduqayumova", "password": "11esinf" }
]



user_credentials_family = [
   {}
]


dp = Dispatcher()

# Start komandasi uchun handler
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer("Royhatdan o'tish boshlash uchun bosing.", reply_markup=keyboardStart)

# Login Student tugmasi bosilganda ishlovchi handler
@dp.message(F.text == 'Royhatdan o\'tish boshlash')
async def handle_login_student(message: types.Message):
    for credentials in user_credentials:
        login_data = {
            'login': credentials['username'],
            'password': credentials['password']
        }
        response = requests.post('https://login.emaktab.uz/', data=login_data)
        
        if response.status_code == 200:
            await message.answer(f"{credentials['username']} foydalanuvchisi ✅ 😃.")
        else:
            await message.answer(f"{credentials['username']} foydalanuvchisi ❌ ☹️")

        time.sleep(random.uniform(1,3))

# Login Family tugmasi bosilgand
@dp.message(F.text == 'Login Family')
async def handle_login_family(message: types.Message):
    for credentials in user_credentials_family:
        login_data = {
            'login': credentials['login'],
            'password': credentials['password']
        }
        response = requests.post('https://login.emaktab.uz/', data=login_data)
        
        if response.status_code == 200:
            await message.answer(f"{credentials['name']} foydalanuvchisi ✅ 😃.")
        else:
            await message.answer(f"{credentials['name']} foydalanuvchisi ❌ ☹️")
            
        time.sleep(random.uniform(3, 6))


# Asinxron ishga tushirish
async def main():
    bot = Bot(token=API_TOKEN)
    await dp.start_polling(bot)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())