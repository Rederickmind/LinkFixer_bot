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
# register_routers(dp)


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
    modified_urls = []
    # Замена ссылок на новые значения
    for url in urls:
        if 'x.com' in url:
            modifiedurl = url.replace('x.com', 'fixupx.com')
        elif 'twitter.com' in url:
            modifiedurl = url.replace('twitter.com', 'vxtwitter.com')
        elif 'instagram.com' in url:
            modifiedurl = url.replace('instagram.com', 'ddinstagram.com')
        modified_urls.append(modifiedurl)
    if modified_urls:
        if message.from_user.username:
            modified_text = ("Saved @"
                             + message.from_user.username
                             + " a click:\n" + "\n".join(modified_urls))
        else:
            modified_text = ("Saved a click:\n" + "\n".join(modified_urls))
        await message.reply(modified_text)


async def main() -> None:
    await dp.start_polling(bot)


# Запуск бота
if __name__ == '__main__':
    asyncio.run(main())