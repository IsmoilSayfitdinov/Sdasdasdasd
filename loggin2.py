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

API_TOKEN = '7714739555:AAFHLlDAuRedGZHl_H2WcIZz4d-7MJO_i70'

# O'quvchilarning login va parollari
user_credentials = [
    {'username': 'azimovamavluda', 'password': '320maktab1'},
    {'username': 'arofatabdullayeva', 'password': '320maktab'},
    {'username': 'nodira.adilova300819', 'password': '320maktab'},
    {'username': 'nodiraxonbakirova', 'password': '320maktab'},
    {'username': 'f_ismailova', 'password': '320maktab'},
    {'username': 'umida.karimova040419', 'password': '320maktab'},
    {'username': 'mutalova.nodira', 'password': '320maktab1'},
    {'username': 'pulatova_nodira', 'password': '320maktab'},
    {'username': 'gulnozaqayumova', 'password': '320maktab'},
    {'username': 'malikaxonqurbonova', 'password': '320maktab'},
    {'username': 'layloraimova', 'password': '320maktab'},
    {'username': 'gozalsalixova', 'password': '320maktab'},
    {'username': 'muxlisasalixova', 'password': '320maktab'},
    {'username': 'saidasoipjonova', 'password': '320maktab'},
    {'username': 'nargizatashxodjayeva', 'password': '320maktab1'},
    {'username': 'xikmatoy', 'password': '320maktab'},
    {'username': 'shaxnoza_usmanova', 'password': '320maktab'},
    {'username': 'nargiza.usmanova0419', 'password': '320maktab'},
    {'username': 'xudayeberganova', 'password': '320maktab'},
    {'username': 'muyassaryoqubova', 'password': '320maktab'},
    {'username': 'yuldashevas', 'password': '320maktab'},
    {'username': 'ynilufar', 'password': '320maktab'},
    {'username': 'nodira.shermatova', 'password': '320maktab'},
    {'username': 'lakromxodjayeva', 'password': '320maktab1'},
    {'username': 'umida.alimova2303199', 'password': '320maktab1'},
    {'username': 'abdulazizzoirov12201', 'password': '320maktab2'},
    {'username': 'umida_imomaliyeva', 'password': '320maktab1'},
    {'username': 'z_sharipxodjayeva', 'password': '320maktab1'},
    {'username': 'feruzaxon.xolmirzaye', 'password': '320maktab1'},
    {'username': 'nazokat.yakubova0706', 'password': '320maktab'},
    {'username': 'kamola.ataxodjayeva', 'password': '320maktab'},
    {'username': 'shaxnozaabidova06198', 'password': '320maktab'},
    {'username': 'dilafruznurmatova069', 'password': '320maktab'},
    {'username': 'isxakova_guzal', 'password': '320maktab'},
    {'username': 'nargiza.usmanova0607', 'password': '320maktab'},
    {'username': 'dildoratuakova', 'password': '320maktab'},
    {'username': 'maxkamboyevgayrat', 'password': '320maktab'},
    {'username': 'dilshodjon.rasulov01', 'password': '320maktab'},
    {'username': 'shamsiyevdurbek', 'password': '320maktab'},
    {'username': 'joxongirpazilov', 'password': '320maktab'}
]


user_credentials_family = [
   {}
]


dp = Dispatcher()

# Start komandasi uchun handler
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer("Kundalik tizimiga kirish uchun 'Login Student' yoki 'Login Family' yozing.", reply_markup=keyboardStart)

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