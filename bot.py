
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN


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
    fg=['шельф',"Бурение","Бизнес","Добыча","Разработка"]
    kb = []
    for i in fg:
        kb.append([types.KeyboardButton(text=i)])
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Тогда выберем функциональную группу!", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text in ['шельф',"Бурение","Бизнес","Добыча","Разработка"])
async def without_puree(message: types.Message):
    parametr['fg']=message.text
    domen=['VR',"AR","ИИ","3D","BDA"]
    kb = []
    for j in domen:
        kb.append([types.KeyboardButton(text=j)])
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Теперь определимся с доменом!", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text in ['VR',"AR","ИИ","3D","BDA"])
async def without_puree(message: types.Message):
    parametr['domen']=message.text
    tech=['VR',"Мобильные решения","Предективный анализ","Продвинутый анализ","Видеоаналитика"]
    kb = []
    for k in tech:
        kb.append([types.KeyboardButton(text=k)])
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Какую технологию вы бы хотели применить!", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text in ['VR',"Мобильные решения","Предективный анализ","Продвинутый анализ","Видеоаналитика"])
async def without_puree(message: types.Message):
    parametr['tech']=message.text
    method=['Обучение персонала',"Цифровой двойник","Мониторинг информации","3D печать","Отбор производственных данных"]
    kb = []
    for f in method:
        kb.append([types.KeyboardButton(text=f)])
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Осталось выбрать метод!", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text in ['Обучение персонала',"Цифровой двойник","Мониторинг информации","3D печать","Отбор производственных данных"])
async def without_puree(message: types.Message):
    parametr['method']=message.text
    await message.answer("Вот что нам удалось найти!"
                         "\n1)Иди нахуй"
                         "\n2)И че ты мне сделаешь"
                         "\n3)Иди нахуй")
    print(parametr)
if __name__ == '__main__':

    executor.start_polling(dp)
