import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
def PyBot():
    logging.basicConfig(level=logging.INFO)
    # Объект бота
    bot = Bot(token="6380923818:AAGKjLup6yvNM3D3ehgsM3MeZNkgzhFMYwg")
    # Диспетчер
    dp = Dispatcher()

    @dp.message(Command("start"))
    async def cmd_start(message: types.Message):
        await message.answer("Hello!")

    async def main():
        await dp.start_polling(bot)

    if __name__ == "__main__":
        asyncio.run(main())