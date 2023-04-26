
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN
from Database import Data

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

parametr={'fg':0,'domen':0,'tech':0,'method':0}
ans=0

#Функция старт
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Здравстуйте, я GasBot!"
                        " \nЯ помогу Вам подобрать интересующий Вас продукт."
                        " \nДля получения инструкции напишите /help")


#Функция окна помощи
@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Для того чтобы начать сначала напишите /start "
                        "\nЧтобы снова увидеть это окно /help "
                        "\nДля поиска продукта напишите /search")

#Функция начала поиска
@dp.message_handler(commands=["search"])
async def cmd_start(message: types.Message):
    global parametr
    parametr = {'fg': 0, 'domen': 0, 'tech': 0, 'method': 0}
    kb = [
        [types.KeyboardButton(text="По названию")],
        [types.KeyboardButton(text="По каталогу")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Как будем производить поиск?", reply_markup=keyboard)


#Начало поиска по названию
@dp.message_handler(lambda message: message.text == "По названию")
async def without_puree(message: types.Message):
    await message.answer("Введите название искомого сценария в такой форме: \"Поиск: название сценария\".")



@dp.message_handler(lambda message: message.text.split()[0]=="Поиск:" )
async def without_puree1(message: types.Message):
        message.text.split().pop(0)
        res=Data.get_correlation(message.text)
        await message.answer('Вот, что удалось найти:')
        for i in res:
            await message.answer(
                f"\nНаименование сценария: {i['Наименование сценария']}"
                f"\nОписание: {i['Описание']}"
                f"\nПотенциал решения: {i['Потенциал решения']}"
                f"\nРыночная зрелость: {i['Рыночная зрелость']}"
                f"\nОрганизационная готовность: {i['Организационная готовность']}"
                f"\nРеализуется в Газпром нефти?: {i['Реализуется в Газпром нефти?']}")



@dp.message_handler(lambda message: message.text == "По каталогу" or message.text=="Вернуться к выбору функциональной группы")
async def without_puree2(message: types.Message):
    fg=Data.get_func_group()
    if len(fg)==0:
        await message.answer("К сожалению по вашему запросу ничего не найдено...")
    kb = []
    kb.append([types.KeyboardButton(text="Начать поиск заново")])
    kb.append([types.KeyboardButton(text="Остановить поиск сейчас")])
    for i in fg:
        kb.append([types.KeyboardButton(text=i)])
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Тогда выберем функциональную группу!", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text in Data.get_func_group()or message.text=="Вернуться к выбору домена")
async def without_puree3(message: types.Message):
    parametr['fg']=message.text
    domen=Data.get_domen(message.text)
    if len(domen) == 0:
        await message.answer("К сожалению по вашему запросу ничего не найдено...")
    kb = []
    kb.append([types.KeyboardButton(text="Начать поиск заново")])
    kb.append([types.KeyboardButton(text="Остановить поиск сейчас")])
    kb.append([types.KeyboardButton(text="Вернуться к выбору функциональной группы")])
    for j in domen:
        kb.append([types.KeyboardButton(text=j)])
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Теперь определимся с доменом!", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text in Data.get_domen(parametr['fg']) or message.text=="Вернуться к выбору технологии")
async def without_puree4(message: types.Message):
    parametr['domen']=message.text
    tech=Data.get_technology(parametr['domen'],parametr['fg'])
    if len(tech) == 0:
        await message.answer("К сожалению по вашему запросу ничего не найдено...")
    kb = []
    kb.append([types.KeyboardButton(text="Начать поиск заново")])
    kb.append([types.KeyboardButton(text="Остановить поиск сейчас")])
    kb.append([types.KeyboardButton(text="Вернуться к выбору домена")])
    for k in tech:
        kb.append([types.KeyboardButton(text=k)])
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Какую технологию вы бы хотели применить!", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text in Data.get_technology(parametr['domen'],parametr['fg']))
async def without_puree5(message: types.Message):
    parametr['tech']=message.text
    method=Data.get_method(parametr['domen'],parametr['fg'],parametr['tech'])
    if len(method) == 0:
        await message.answer("К сожалению по вашему запросу ничего не найдено...")
    kb = []
    kb.append([types.KeyboardButton(text="Начать поиск заново")])
    kb.append([types.KeyboardButton(text="Остановить поиск сейчас")])
    kb.append([types.KeyboardButton(text="Вернуться к выбору технологии")])

    for f in method:
        kb.append([types.KeyboardButton(text=f)])
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Осталось выбрать метод!", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text in Data.get_method(parametr['domen'],parametr['fg'],parametr['tech']))
async def without_puree6(message: types.Message):
    parametr['method']=message.text
    res = Data.get_documents(parametr['fg'],parametr['domen'],parametr['tech'],parametr['method'])
    if len(res) == 0:
        await message.answer("К сожалению по вашему запросу ничего не найдено...")
    await message.answer('Результаты поиска:')
    for i in res:
        await message.answer(
                             f"\nНаименование сценария: {i['Наименование сценария']}"
                             f"\nОписание: {i['Описание']}"
                             f"\nПотенциал решения: {i['Потенциал решения']}"
                             f"\nРыночная зрелость: {i['Рыночная зрелость']}"
                             f"\nОрганизационная готовность: {i['Организационная готовность']}"
                             f"\nРеализуется в Газпром нефти?: {i['Реализуется в Газпром нефти?']}"
    )

@dp.message_handler(lambda message: message.text=="Начать поиск заново")
async def cmd_start(message: types.Message):
    global parametr
    parametr = {'fg': 0, 'domen': 0, 'tech': 0, 'method': 0}
    kb = [
        [types.KeyboardButton(text="По названию")],
        [types.KeyboardButton(text="По каталогу")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Как будем производить поиск?", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Остановить поиск сейчас")
async def cmd_start1(message: types.Message):
    if parametr['fg']!=0 and parametr['domen']==0 and parametr['tech']==0 and parametr['method']==0:
        res=Data.get_documents_by_fg(func=parametr['fg'])
    elif parametr['fg']!=0 and parametr['domen']!=0 and parametr['tech']==0 and parametr['method']==0:
        res=Data.get_documents_by_fg_and_domen(func=parametr['fg'],domen=parametr['domen'])
    elif parametr['fg']!=0 and parametr['domen']!=0 and parametr['tech']!=0 and parametr['method']==0:
        res=Data.get_documents_by_fg_and_domen(func=parametr['fg'],domen=parametr['domen'],tech=parametr['tech'])
    if len(res) == 0:
        await message.answer("К сожалению по вашему запросу ничего не найдено...")
    await message.answer('Результаты поиска:')
    for i in res:
        await message.answer(
                             f"\nНаименование сценария: {i['Наименование сценария']}"
                             f"\nОписание: {i['Описание']}"
                             f"\nПотенциал решения: {i['Потенциал решения']}"
                             f"\nРыночная зрелость: {i['Рыночная зрелость']}"
                             f"\nОрганизационная готовность: {i['Организационная готовность']}"
                             f"\nРеализуется в Газпром нефти?: {i['Реализуется в Газпром нефти?']}"
    )

if __name__ == '__main__':

    executor.start_polling(dp)
