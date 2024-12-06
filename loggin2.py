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
    { 'username': 'azimovamavluda', 'password': '320maktab1'},
    { 'username': 'arofatabdullayeva', 'password': '320maktab'},
    { 'username': 'nodira.adilova300819', 'password': '320maktab'},
    { 'username': 'nodiraxonbakirova', 'password': '320maktab'},
    { 'username': 'f_ismailova', 'password': '320maktab'},
    { 'username': 'umida.karimova040419', 'password': '320maktab'},
    { 'username': 'mutalova.nodira', 'password': '320maktab1'},
    { 'username': 'pulatova_nodira', 'password': '320maktab'},
    { 'username': 'gulnozaqayumova', 'password': '320maktab'},
    { 'username': 'malikaxonqurbonova', 'password': '320maktab'},
    { 'username': 'layloraimova', 'password': '320maktab'},
    { 'username': 'gozalsalixova', 'password': '320maktab'},
    { 'username': 'muxlisasalixova', 'password': '320maktab'},
    { 'username': 'saidasoipjonova', 'password': '320maktab'},
    { 'username': 'nargizatashxodjayeva', 'password': '320maktab1'},
    { 'username': 'xikmatoy', 'password': '320maktab'},
    { 'username': 'shaxnoza_usmanova', 'password': '320maktab'},
    { 'username': 'nargiza.usmanova0419', 'password': '320maktab'},
    { 'username': 'xudayeberganova', 'password': '320maktab'},
    { 'username': 'muyassaryoqubova', 'password': '320maktab'},
    { 'username': 'yuldashevas', 'password': '320maktab'},
    { 'username': 'ynilufar', 'password': '320maktab'},
    { 'username': 'nodira.shermatova', 'password': '320maktab'},
    { 'username': 'lakromxodjayeva', 'password': '320maktab1'},
    { 'username': 'umida.alimova2303199', 'password': '320maktab1'},
    { 'username': 'abdulazizzoirov12201', 'password': '320maktab2'},
    { 'username': 'umida_imomaliyeva', 'password': '320maktab1'},
    { 'username': 'z_sharipxodjayeva', 'password': '320maktab1'},
    { 'username': 'feruzaxon.xolmirzaye', 'password': '320maktab1'},
    { 'username': 'nazokat.yakubova0706', 'password': '320maktab'},
    { 'username': 'kamola.ataxodjayeva', 'password': '320maktab'},
    { 'username': 'shaxnozaabidova06198', 'password': '320maktab'},
    { 'username': 'dilafruznurmatova069', 'password': '320maktab'},
    { 'username': 'isxakova_guzal', 'password': '320maktab'},
    { 'username': 'nargiza.usmanova0607', 'password': '320maktab'},
    { 'username': 'dildoratuakova', 'password': '320maktab'},
    { 'username': 'maxkamboyevgayrat', 'password': '320maktab'},
    { 'username': 'dilshodjon.rasulov01', 'password': '320maktab'},
    { 'username': 'shamsiyevdurbek', 'password': '320maktab'},
    { 'username': 'joxongirpazilov', 'password': '320maktab'},
    { "username": "babdunasirov", "password": "1asinf" },
    { "username": "abdurahmanovaimona", "password": "1asinf" },
    { "username": "amronabduraximov", "password": "1asinf" },
    { "username": "sunnatullohakmalov", "password": "1asinf" },
    { "username": "baxtiyorovamubina301", "password": "1asinf" },
    { "username": "komiljon.botirov0920", "password": "1asinf" },
    { "username": "iymona.boxodirova201", "password": "1asinf" },
    { "username": "doniyorovsalohiddin", "password": "1asinf" },
    { "username": "iymona.farxodova0520", "password": "1asinf" },
    { "username": "a.fatxullayev2109201", "password": "1asinf" },
    { "username": "solihaibobekova", "password": "1asinf" },
    { "username": "sharizodamexridinova", "password": "1asinf" },
    { "username": "mraliyeva", "password": "1asinf" },
    { "username": "umarmirhakimov", "password": "1asinf" },
    { "username": "rustam.usmonov190920", "password": "1asinf" },
    { "username": "m.mubashirova", "password": "1asinf" },
    { "username": "samiramuxammadiyeva2", "password": "1asinf" },
    { "username": "muhammadsolih.o10201", "password": "1asinf" },
    { "username": "rustamjonosmanov", "password": "1asinf" },
    { "username": "ramazon.pardayev1220", "password": "1asinf" },
    { "username": "qodirov.abduqodir042", "password": "1asinf" },
    { "username": "zaynabxonrixsiboyeva", "password": "1asinf" },
    { "username": "rutmova", "password": "1asinf" },
    { "username": "ibrohimsaidahmadiy", "password": "1asinf" },
    { "username": "saidahmadzoda", "password": "1asinf" },
    { "username": "saidakbararova", "password": "1asinf" },
    { "username": "abduhakimsaidnabiyev", "password": "1asinf" },
    { "username": "robiya_ubaydullaeva", "password": "1asinf" },
    { "username": "n.umarjonov", "password": "1asinf" },
    { "username": "xaxrullayev", "password": "1asinf" },
    { "username": "farxod.xolmatov05199", "password": "320maktab" },
    { "username": "uabduraxmonov3001198", "password": "320maktab" },
    { "username": "aziza.xasanova020519", "password": "320maktab" },
    { "username": "rixsiyevarixsixon", "password": "320maktab" },
    { "username": "sardor.kamilov021219", "password": "320maktab" },
    { "username": "shahodat.nizomova", "password": "320maktab" },
    { "username": "gaybullayev.abror199", "password": "320maktab" },
    { "username": "muxtabar.abdiyeva", "password": "320maktab" },
    { "username": "turdikulovsardor", "password": "320maktab" },
    { "username": "karimovamuxlisa04199", "password": "320maktab" },
    { "username": "sidorajurayeva", "password": "320maktab" },
    { "username": "yunusova.zilola02197", "password": "320maktab" },
    { "username": "zulxumor.nabiyeva061", "password": "320maktab" },
    { "username": "qodirova.dilafruz118", "password": "320maktab" },
    { "username": "uktamjondadabayeva", "password": "320maktab" },
    { "username": "raximova.munisa07198", "password": "320maktab" },
    { "username": "mohira.roziyeva01199", "password": "320maktab" },
    { "username": "umida.maxamatova0119", "password": "320maktab" },
    { "username": "saodatraxmatjonova", "password": "320maktab" },
    { "username": "dilshod.axmedov25121", "password": "320maktab" },
    { "username": "aabduraxmona", "class": "320maktab"},
    { "username": "ismoilabduqodirov", "class": "320maktab"},
    { "username": "shahzodaabduraximova", "class": "320maktab"},
    { "username": "nodiraxonanvarova", "class": "320maktab"},
    { "username": "atxamovamubina", "class": "320maktab"},
    { "username": "azimovvv", "class": "320maktab1"},
    { "username": "botirovaezoza", "class": "320maktab"},
    { "username": "ikromovamubina", "class": "320maktab"},
    { "username": "firdavskarimjonov", "class": "320maktab"},
    { "username": "rmaxamadjanova", "class": "320maktab"},
    { "username": "mahmudovvv", "class": "abdulboriy170511"},
    { "username": "gmuxammadnaimova", "class": "320maktab"},
    { "username": "solixabonunabiyeva", "class": "320maktab"},
    { "username": "m_nuriddinova", "class": "320maktab"},
    { "username": "nurzodaolimova", "class": "320maktab"},
    { "username": "otabekqobilov", "class": "320maktab"},
    { "username": "jasminarustamova", "class": "320maktab"},
    { "username": "shahinarustamova", "class": "320maktab1"},
    { "username": "layloxonsalixova", "class": "320maktab"},
    { "username": "sardorsaidiganiev", "class": "320maktab"},
    { "username": "javohirbeksodiqjonov", "class": "320maktab"},
    { "username": "otadjixodjayeva", "class": "320maktab"},
    { "username": "ezozavoxidova", "class": "320maktab"},
    { "username": "xalilovamuslima", "class": "320maktab"},
    { "username": "xasanovaomina", "class": "320maktab"},
    { "username": "abdurashidyulchiyev", "class": "320maktab"},
    { "username": "zakirjanova", "class": "320maktab"},
    { "username": "sheripbayevich", "class": "320maktab"},
    { "username": "maxmudov.zafar310119", "class": "320maktab"},
    { "username": "nodira.usmanova23101", "class": "320maktab"},
    { "username": "abduqodir.abdumomino", "class": "320maktab"},
    { "username": "abduqodirova_rayyona", "class": "320maktab"},
    { "username": "zebiniso.alimova1020", "class": "320maktab"},
    { "username": "zeboxon.anvarova0820", "class": "320maktab"},
    { "username": "solihaergasheva08201", "class": "320maktab"},
    { "username": "zamiraeshtemirova", "class": "320maktab"},
    { "username": "rustambekismoilov201", "class": "320maktab"},
    { "username": "abdullohkushkinov", "class": "320maktab"},
    { "username": "mubinamagrupova", "class": "320maktab"},
    { "username": "mirsaid_mirzoxidov", "class": "320maktab"},
    { "username": "muhammadamin_nurmato", "class": "320maktab"},
    { "username": "oktamjonov.jaxongir", "class": "320maktab"},
    { "username": "jannatobidova", "class": "320maktab"},
    { "username": "nurmuhammad.olimov08", "class": "320maktab"},
    { "username": "oqilovasoliha", "class": "320maktab"},
    { "username": "muhammadzaydulloh", "class": "320maktab"},
    { "username": "shavkatovamashkura", "class": "320maktab"},
    { "username": "sobirjonov.muhammad1", "class": "320maktab"},
    { "username": "solihabonusobitjonov", "class": "320maktab"},
     { "username": "htadjixodjayeva", "password": "320maktab" },
    { "username": "tolaboyevaziyoda", "password": "320maktab" },
    { "username": "shodiyabegim.u", "password": "320maktab" },
    { "username": "uxolmirzayeva2410201", "password": "320maktab" },
    { "username": "yusufbekxusniddinov", "password": "320maktab" },
    { "username": "zaxroyusufjonova", "password": "320maktab" },
    { "username": "abduaxatova", "password": "roziya8b" },
    { "username": "abdullayeva.m2203201", "password": "madina8b" },
    { "username": "mabduvoxidov", "password": "muhammadamin8b" },
    { "username": "alimbayev", "password": "abdumalik8b" },
    { "username": "odinaxonasqarova", "password": "odina8b" },
    { "username": "abduboriybaxtiyorov", "password": "abduboriy8b" },
    { "username": "odilxonbaxtiyorov", "password": "odil8b" },
    { "username": "durbekova", "password": "durbekova8b" },
    { "username": "guliranoergasheva", "password": "gulirano8b" },
    { "username": "mustafoerkinov", "password": "mustafo8b" },
    { "username": "muxammadrizoerkinov1", "password": "muhammadrizo8b" },
    { "username": "fozilovamuslima", "password": "muslima8b" },
    { "username": "solixajoraboyeva", "password": "solixa8b" },
    { "username": "tursunoyjoraboyeva", "password": "tursunoy8b" },
    { "username": "maxkambayev", "password": "shoakbar8b" },
    { "username": "muhammadsolix", "password": "muhammadsolix8b" },
    { "username": "hadichamirhamidova", "password": "xadicha8b" },
    { "username": "ibrohimmirsaidov", "password": "ibroxim8b" },
    { "username": "rayyonamirxalilova", "password": "rayyona8b" },
    { "username": "mirxoltayeva", "password": "mirxoltayeva8b" },
    { "username": "mubinanorbotayeva", "password": "norbutayeva8b" },
    { "username": "mnuvrillayev", "password": "muhammadali8b" },
    { "username": "patxillayeva", "password": "maftuna8b" },
    { "username": "muxlisa.qudratova", "password": "muxlisa8b" },
    { "username": "xabibulloxrixsiboyev", "password": "xabibullox8b" },
    { "username": "robiyatoirova", "password": "toirova8b" },
    { "username": "robiyauygunova", "password": "uygunova8b" },
    { "username": "bilolxojiakbarov", "password": "bilol8b" },
    { "username": "ayupxon", "password": "ayupxon8b" },
    { "username": "khudoyberganovb", "password": "baxtbek8b" },
    { "username": "mohinurabduaxatova", "password": "mohinur8b" },
    { "username": "xudoyberganova150420", "password": "xudoyberganova8b" },
    { "username": "abdusaidabdullayev", "password": "maktab320" },
    { "username": "r.abdurasulov", "password": "320maktab" },
    { "username": "adilovmirobid", "password": "320maktab1" },
    { "username": "mirsobitakbarov", "password": "320maktab2" },
    { "username": "abduvoxit", "password": "320maktab3" },
    { "username": "alisher.alimov", "password": "320maktab4" },
    { "username": "alimov.ulugbek", "password": "320maktab5" },
    { "username": "dekanov", "password": "320maktab6" },
    { "username": "eshnazarovibrohim", "password": "320maktab7" },
    { "username": "anvarfozilov", "password": "320maktab7" },
    { "username": "zokirilxamov", "password": "320maktab8" },
    { "username": "akbar.k", "password": "320maktab9" },
    { "username": "nodira.karimova05198", "password": "320maktab1" },
    { "username": "farxodkuchkarov", "password": "320maktab2" },
    { "username": "naimakhonkhusainova", "password": "320maktab4" },
    { "username": "mirbahromova", "password": "320maktab2" },
    { "username": "mullaxanov", "password": "320maktab1" },
    { "username": "jaxongirnasirov", "password": "320maktab2" },
    { "username": "nilufar_n", "password": "320maktab2" },
    { "username": "baxram", "password": "320maktab1" },
    { "username": "javlon.umarov0401198", "password": "320maktab1" },
    { "username": "xanbabayevdilshod", "password": "320maktab2" },
    { "username": "baxromjonxolmatov", "password": "320maktab2" },
    { "username": "shodiyabegim", "password": "320maktab1" },
    { "username": "yuldasheva.nodira199", "password": "320maktab2" },
    { "username": "gulomjonyusupov", "password": "320maktab1" },
    { "username": "shoafzalshausmanov", "password": "320maktab2" },
    { "username": "xudayberdiyevakbar", "password": "320maktab" },
    { "username": "xasanova.zilola06081", "password": "320maktab1" },
    { "username": "adilova.feruza140619", "password": "320maktab2" },
    { "username": "egamberdiyevad110319", "password": "320maktab3" },
    { "username": "abdullayeva.marjona", "password": "maktab10v" },
    { "username": "obidjon.abduraximov", "password": "maktab10v" },
    { "username": "safoaktamova", "password": "maktab10v" },
    { "username": "marxaboanvarova", "password": "maktab10v" },
    { "username": "aziza.asadova1610200", "password": "maktab10v" },
    { "username": "laziza.asatova", "password": "maktab10v" },
    { "username": "ibroximbaxtiyorov", "password": "maktab10v" },
    { "username": "nurillo.baxtiyorov", "password": "maktab10v" },
    { "username": "osiyobotirova", "password": "maktab10v" },
    { "username": "muxammadyusufb", "password": "maktab10v" },
    { "username": "boymatov.davlatbek", "password": "maktab10v" },
    { "username": "mubashshirs", "password": "maktab10v" },
    { "username": "rohilaerkaboyeva", "password": "maktab10v" },
    { "username": "ibroximov.ismoil", "password": "maktab10v" },
    { "username": "magrupoff", "password": "10vmaktab" },
    { "username": "mushtariy.megliyeva", "password": "maktab10v" },
    { "username": "kirish", "password": "maktab10v" },
    { "username": "risolatnigmonjonova", "password": "maktab10v" },
    { "username": "n.nuriddinova2011200", "password": "maktab10v" },
    { "username": "patxullayev", "password": "maktab10v" },
    { "username": "ravshanov_sardor", "password": "maktab10v" },
    { "username": "muxiddinruziboyev", "password": "maktab10v" },
    { "username": "xojiakbaryoldashev", "password": "maktab10v" },
    { "username": "m.shonazarov", "password": "maktab10v" },
    { "username": "umidashuhratjonova", "password": "maktab10v" },
    { "username": "shuxratovabdurashid", "password": "maktab10v" },
    { "username": "sabdullayev", "password": "maktab10v" },
    { "username": "imamalievazilola", "password": "maktab10v" },
    { "username": "qurbonovamunira", "password": "maktab10v" },
    { "username": "margubadjorayeva", "password": "maktab10v" },
    { "username": "azimjon.rafiqov", "password": "maktab10v" },
    { "username": "nigora.amonova080119", "password": "maktab10v" },
    { "username": "boxodirtursunov", "password": "maktab10v" },
    { "username": "polatova.nozima10198", "password": "maktab10v" },
    { "username": "obidnigmatov", "password": "maktab10v" },
    { "username": "kamoladosmuhammedova", "password": "maktab10v" },
    { "username": "zulhumorhalidova", "password": "maktab10v" },
    { "username": "zulxumorusmonova", "password": "maktab10v" },
    { "username": "nraxmatillayeva", "password": "maktab10v" },
    { "username": "shermuxamedovag", "password": "maktab10v" },
    { "username": "axmadjonmuxammedov", "password": "maktab10v" },
    { "username": "sherzodavazov1502198", "password": "maktab10v" },
    { "username": "qayumbekova", "password": "maktab10v" },
    { "username": "omonjonshamsiyev", "password": "maktab10v" },
    { "username": "kamolaxon.irnazarova", "password": "maktab10v" },
    { "username": "jaxongirnosirov", "password": "maktab10v" },
    { "username": "saida.rasulova070319", "password": "maktab10v" },
    { "username": "nazokat.atamurodova", "password": "maktab10v" },
    { "username": "yoldashevamalika", "password": "maktab10v" },
    { "username": "shoasror", "password": "maktab10v" },
    { "username": "isroilovbotir", "password": "maktab10v" },
    { "username": "xusanova.nozima", "password": "maktab10v" }
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