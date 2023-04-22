from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import BoundFilter
from magic_filter import F



from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

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
    markup =types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('По названию',callback_data='name'))
    markup.add(types.InlineKeyboardButton('По каталогу',callback_data='cat'))
    await message.answer("Как будем производить поиск?", reply_markup=markup)

@dp.callback_query_handler()
async def callback1(call1):
    await call1.message.answer(call1.data)
    fg={'шельф':1,"бурение":2,"бизнес":3,"газ":4,"Добыча":5}
    if call1.data=='cat':
        markup = types.InlineKeyboardMarkup()
        for i in fg.keys():
            markup.add(types.InlineKeyboardButton(i,callback_data=fg[i]))
        await call1.message.answer("Выберете функциональную группу",reply_markup=markup)

@dp.callback_query_handler()
async def callback2(call2):
    await call2.message.answer(call2.data)
    domen={'AR':1,"VR":2,"ИИ":3,"3D":4,"БВС":5}
    markup = types.InlineKeyboardMarkup()
    for j in domen.keys():
        markup.add(types.InlineKeyboardButton(j,callback_data=domen[j]))
    await call2.message.answer("Отлично! Теперь опредилимся с доменом",reply_markup=markup)

if __name__ == '__main__':

    executor.start_polling(dp)
