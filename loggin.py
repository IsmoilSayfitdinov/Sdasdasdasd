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
            KeyboardButton(text='Login Student'),
            KeyboardButton(text='Login Family')
        ]
    ],
    resize_keyboard=True
)

API_TOKEN = '7939396004:AAGzmCZ10PmzFFGejdDvgk-VLHvvQhqYeIU'

# O'quvchilarning login va parollari
user_credentials = [
    {"name": "Abduaxadov Abdulloh", "login": "abduaxadov", "password": "10asinf1"},
    {"name": "Abdumutalova Gulziyo", "login": "gulziyoa", "password": "10asinf1"},
    {"name": "Abdurazzoqova Muxsina", "login": "muxsinaabdurazzoqova", "password": "10asinf1"},
    {"name": "Abduxamidova Muxlisa", "login": "muxlisaabduxamidova", "password": "10asinf1"},
    {"name": "Abdushoxidov Bekzod", "login": "abdushoxidov", "password": "10asinf1"},
    {"name": "Alimov Ibrohim", "login": "ibroximalimov", "password": "10asinf1"},
    {"name": "Daminov Muzammil", "login": "muzammil", "password": "10asinf1"},
    {"name": "Hoshimova Sabina", "login": "sabina.hoshimova0820", "password": "10asinf1"},
    {"name": "Isamuxammedova Ziyoda", "login": "ziyodaxongofurova", "password": "10asinf1"},
    {"name": "Isroilov Bexruz", "login": "bexruzisroilov", "password": "10asinf1"},
    {"name": "Mahmudjonova Mohinur", "login": "mohinurmaxmudjonova", "password": "10asinf1"},
    {"name": "Mirkomilova Muxlisa", "login": "muxlisamirkomilova", "password": "10asinf"},
    {"name": "Mirpayziyev Azamat", "login": "mirpayziyev", "password": "10asinf1"},
    {"name": "Murodova Soliha", "login": "solihamurodova", "password": "10asinf1"},
    {"name": "Nuraliyev Yunusbek", "login": "yunusbek.nuraliyev", "password": "10asinf1"},
    {"name": "Nurullayev Abdulloh", "login": "abdullohnurullayev", "password": "10asinf11"},
    {"name": "Ortiqov Alixon", "login": "alixon.ortiqov", "password": "10asinf11"},
    {"name": "Qurbonov Suxrob", "login": "suxrob.qurbonov", "password": "10asinf"},
    {"name": "Samukjanova Mushtaribonu", "login": "samukjanova", "password": "10asinf1"},
    {"name": "Sayfitdinov Ismoil", "login": "ismoilsayfitdinov", "password": "10asinf1"},
    {"name": "Sayfullayev Xabibulla", "login": "xabibullasayfullayev", "password": "10asinf11"},
    {"name": "Sobitjonov Muhammad Ali", "login": "suxrobjonsobitjonov", "password": "10asinf1"},
    {"name": "Sobitova Farangiz", "login": "sobitova.farangiz200", "password": "10asinf1"},
    {"name": "Talipova E‘zoza", "login": "tolipovaezozaxon", "password": "10asinf1"},
    {"name": "Tojixo‘jayev Muhammad Yusuf", "login": "mtojixojayev", "password": "10asinf1"},
    {"name": "Toxirov Bilolxo‘ja", "login": "bilolxojatoxirov", "password": "10asinf1"},
    {"name": "Usmonbekov A‘zambek", "login": "azambekusmonbekov", "password": "10asinf1"},
    {"name": "Xusniddinova Ominaxon", "login": "ominaxonxusniddinova", "password": "10asinf1"},
    {"name": "Zabixullayev Firdavs", "login": "firdavszabixullayev", "password": "10asinf1"},
    {"name": "Shukrullayeva Ruxshona", "login": "ruxshonashukrullaeva", "password": "10asinf1"},
    {"name": "Shukritdinov Ayubxon", "login": "shukuritdinov", "password": "10asinf1"},
]

user_credentials_family = [
    {"name": "Abduraxmonov Rustambek (A'zambek)", "login": "rabduraxmanov", "password": "10asinf"},
    {"name": "Abdushoxidov Muzaffar (Bekzod)", "login": "abdushaxidov", "password": "10asinf"},
    {"name": "Adilov Alisher  (A.Muxlisa)", "login": "adilovalisher", "password": "10asinf"},
    {"name": "Adilova Sharofatxon (Mushtaribonu)", "login": "sharofatxonadilova", "password": "10asinf"},
    {"name": "Alimov Ravshan (Ibrohim)", "login": "alimov.ravshan", "password": "10asinf"},
    {"name": "Aminjonova Dildora (E‘zoza)", "login": "dildoraaminjonova", "password": "10asinf"},
    {"name": "Avezov Ismoil (Ruxshona)", "login": "avezov.ismoil", "password": "10asinf"},
    {"name": "Daminov Kamoliddin (Muzammil)", "login": "kamoliddindaminov", "password": "10asinf"},
    {"name": "Irgashev Jamshiddin (Ismoil)", "login": "jamshiddinirgashov", "password": "10asinf"},
    {"name": "Isamuxammedov Jamshidjon (Ziyoda)", "login": "jamshidjoni", "password": "10asinf"},
    {"name": "Israilov Ma'mur (Mohinur)", "login": "israilovmamur", "password": "10asinf1"},
    {"name": "Isroilova Gullola (Behruz)", "login": "gullolaisroilova", "password": "10asinf"},
    {"name": "Jalolova Zulxumor (Muhammadyusuf)", "login": "jalolovazulxumor", "password": "10asinf1"},
    {"name": "Maxamedov Abdujabbor (Muxsina)", "login": "abdujabbormaxamedov", "password": "10asinf"},
    {"name": "Minavarov Olimjon (Muhammad Ali)", "login": "olimjonminavarov", "password": "10asinf"},
    {"name": "Mirpayziyev Mirkamol (Azamat)", "login": "mirkamolmirpayziyev", "password": "10asinf"},
    {"name": "Nazirbekov To‘rabek (Ayubxon)", "login": "turabeknazirbekov", "password": "10asinf"},
    {"name": "Qo‘chqorov Shukrulla (N.Abdulloh)", "login": "qochkorov", "password": "10asinf"},
    {"name": "Qo‘chqorov Sanjar (Xabibulla)", "login": "sajarqochqorov", "password": "10asinf"},
    {"name": "Sagdullayev Kamoliddin (Omina)", "login": "sagdullayevk", "password": "10asinf"},
    {"name": "Umarov Davron (Soliha)", "login": "udavron", "password": "10asinf"},
    {"name": "Usmanov Ziyodilla (Firdavs)", "login": "ziyodillausmanov", "password": "10asinf"},
    {"name": "Usmonov Fozil (Bilolxo‘ja)", "login": "fozilusmonov", "password": "10asinf"},
    {"name": "Xudoyberdiyev Asror (A.Abdulloh)", "login": "asrorxudoyberdiyev", "password": "10asinf"},
    {"name": "Ilyasova Mamura (M.Muxlisa)", "login": "mamura.ilyasova12198", "password": "10asinf"},
    {"name": "Eshmamatova Sabohat (Yunusbek)", "login": "sabohat.eshmamatova", "password": "10asinf"},
    {"name": "Alimov Avazxon (Alixon)", "login": "avazxon_alimov", "password": "10asinf"},
    {"name": "Hudoyberdiyeva Dilfuza (Gulziyo)", "login": "d.xudayberdiyeva1309", "password": "10asinf"},
    {"name": "Tursunboyev Shuxrat (Farangiz)", "login": "shuxrat.tursunboyev8", "password": "10asinf"},
    {"name": "Qurbonova Dilfuza (Suhrob)", "login": "dilfuzaqurbonova0602", "password": "10asinf"},
    {"name": "Hayitova Anorxol (Sabina)", "login": "hayitovaanorxol", "password": "10asinf"}

]


dp = Dispatcher()

# Start komandasi uchun handler
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer("Kundalik tizimiga kirish uchun 'Login Student' yoki 'Login Family' yozing.", reply_markup=keyboardStart)

# Login Student tugmasi bosilganda ishlovchi handler
@dp.message(F.text == 'Login Student')
async def handle_login_student(message: types.Message):
    for credentials in user_credentials:
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

# Login Family tugmasi bosilganda ishlovchi handler
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