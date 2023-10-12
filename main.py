import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import Command
from Notion import *

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6380923818:AAGKjLup6yvNM3D3ehgsM3MeZNkgzhFMYwg")
storage = MemoryStorage()
# Диспетчер
dp = Dispatcher(storage=storage)
class States(StatesGroup):
    subject = State()
    group = State()
    Familiya = State()
    GoNext = State()

spisok = []

@dp.message(Command("start"))
async def cmd_start(message:types.Message, state: FSMContext):
    print(message.from_user.id)
    identified = False
    for i in spisok:
        if i == message.from_user.id:
            identified = True
    if (identified == False):
        await message.answer("Введите дисциплину")
        await state.set_state(States.subject)

        @dp.message(States.subject)
        async def process_first_question(message: types.Message, state: FSMContext):
            answer = message.text
            await state.update_data(subject=answer)
            await message.reply("Введи группу")
            await state.set_state(States.group)

        @dp.message(States.group)
        async def process_second_question(message: types.Message, state: FSMContext):
            # Обработка ответа на второй вопрос
            answer = message.text
            # Сохранение ответа в состоянии
            await state.update_data(group=answer)
            # Переход к следующему состоянию
            await state.set_state(States.Familiya)
            await message.reply("Введите ФИО")

        @dp.message(States.Familiya)
        async def process_third_question(message: types.Message, state: FSMContext):
            answer = message.text
            await state.update_data(Familiya=answer)
            data = await state.get_data()
            SUBject = data['subject']
            Group = data['group']
            FIO = data['Familiya']
            if (find_Student(fix_lesson(SUBject),fix_group(Group),fix_full_name(FIO)) == True):
                spisok.append(message.from_user.id)
                for i in spisok:
                    print(i)
                await message.answer('Вы идентифицированы, введи "Начать", чтобы продолжить ')
            else:
                await message.answer('Вы не идентифицированы, введите "/start", чтобы повторить попытку')
    else:
        await message.answer('Введи "Начать", чтобы продолжить')
        await state.set_state(States.GoNext)

@dp.message(lambda message: message.text == "начать" or message.text == "Начать")
async def GoNext(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Проверить документы"),
            types.KeyboardButton(text="Проверить сданные работы"),
            types.KeyboardButton(text="Материалы"),
            types.KeyboardButton(text="Профиль")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи"
    )
    await message.answer("Выберите функцию", reply_markup=keyboard)

@dp.message(lambda message: message.text == "Проверить документы")
async def docs(message: types.Message):
    await message.reply("Здесь будет функция провреки документов")

@dp.message(lambda message: message.text == "Проверить сданные работы")
async def works(message: types.Message):
    await message.reply("Здесь будет функция провреки сданных работ")

@dp.message(lambda message: message.text == "Материалы")
async def materials(message: types.Message):
    await message.reply("здесь ссылка на материалы")

@dp.message(lambda message: message.text == "Профиль")
async def profile(message: types.Message):
    await message.reply("Инфо о типуле:")
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())