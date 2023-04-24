
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN
from Database import Data

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

parametr={'fg':0,'domen':0,'tech':0,'method':0}

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Здравстуйте, я GasBot!"
                        " \nЯ помогу Вам подобрать интересующий Вас продукт."
                        " \nДля получения инструкции напишите /help")



@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Для того чтобы начать сначала напишите /start "
                        "\nЧтобы снова увидеть это окно /help "
                        "\nДля поиска продукта напишите /search")


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


@dp.message_handler(lambda message: message.text == "По названию")
async def without_puree(message: types.Message):
    await message.answer("Введите название искомого сценария.")


@dp.message_handler(lambda message: message.text == "По каталогу")
async def without_puree(message: types.Message):
    fg=Data.get_func_group()
    kb = []
    for i in fg:
        kb.append([types.KeyboardButton(text=i)])
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Тогда выберем функциональную группу!", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text in Data.get_func_group())
async def without_puree(message: types.Message):
    parametr['fg']=message.text
    domen=Data.get_domen(message.text)
    kb = []
    for j in domen:
        kb.append([types.KeyboardButton(text=j)])
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Теперь определимся с доменом!", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text in Data.get_domen(parametr['fg']))
async def without_puree(message: types.Message):
    parametr['domen']=message.text
    tech=Data.get_technology(parametr['domen'],parametr['fg'])
    kb = []
    for k in tech:
        kb.append([types.KeyboardButton(text=k)])
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Какую технологию вы бы хотели применить!", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text in Data.get_technology(parametr['domen'],parametr['fg']))
async def without_puree(message: types.Message):
    parametr['tech']=message.text
    method=Data.get_method(parametr['domen'],parametr['fg'],parametr['tech'])
    kb = []
    for f in method:
        kb.append([types.KeyboardButton(text=f)])
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Осталось выбрать метод!", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text in Data.get_method(parametr['domen'],parametr['fg'],parametr['tech']))
async def without_puree(message: types.Message):
    parametr['method']=message.text
    res = Data.get_documents(parametr['fg'],parametr['domen'],parametr['tech'],parametr['method'])
    print(len(res))
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
    print(parametr)
if __name__ == '__main__':

    executor.start_polling(dp)
