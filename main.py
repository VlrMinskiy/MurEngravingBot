from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(f'{message.from_user.first_name}, добро пожаловать в мою творческую студию!')

@dp.message_handler()
async def answer(message: types.Message):
    await message.reply('Пока что у меня нет такой команды :(')

if __name__ == '__main__':
    executor.start_polling(dp)



