import os
import asyncio
import re

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from aiogram import types
from aiogram.filters import Command

from constants import HELP_TEXT, LINK_FILTER, START_TEXT

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')


# Создаем экземпляр бота
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command('start'))
async def cmd_start(message: types.Message) -> None:
    """Processes the `start` command"""
    username = message.from_user.full_name
    await message.reply(START_TEXT.format(username))


@dp.message(Command('help'))
async def help_command(message: types.Message) -> None:
    await message.reply(HELP_TEXT)


@dp.message(LINK_FILTER)
async def process_message(message: types.Message):
    text = message.text
    # Поиск ссылок в тексте сообщения
    urls = re.findall(
        r'(https?://(?:www\.)?(?:x|twitter|instagram)\.com/[^\s]+)',
        text
    )
    # Замена ссылок на новые значения
    for url in urls:
        modifiedurl = replace(
            r'(x|twitter)\.com',
            'fixupx.com',
            url
        )
        modifiedurl = replace(
            r'instagram\.com',
            'ddinstagram.com',
            modifiedurl
        )
        if modifiedurl != url:
            if message.from_user.username:
                modified_text = (
                    "Saved @"
                    + message.from_user.username
                    + " a click:\n" + modifiedurl
                )
            else:
                modified_text = ("Saved a click:\n" + modifiedurl)
            await message.reply(modified_text)


def replace(match, replacer, input):
    return re.sub(match, replacer, input)


async def main() -> None:
    await dp.start_polling(bot)


# Запуск бота
if __name__ == '__main__':
    asyncio.run(main())
