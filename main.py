import os
import asyncio
import re

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from aiogram import types
from aiogram.filters import Command

from constants import LINK_FILTER

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')


# Создаем экземпляр бота
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
# register_routers(dp)


@dp.message(Command('start'))
async def cmd_start(message: types.Message) -> None:
    """Processes the `start` command"""
    await message.reply('Bot has been started!')


@dp.message(Command('help'))
async def help_command(message: types.Message) -> None:
    await message.reply('helptext')


@dp.message(LINK_FILTER)
async def process_message(message: types.Message):
    text = message.text
    # Поиск ссылок в тексте сообщения
    urls = re.findall(
        r'(https?://(?:www\.)?(?:x|twitter|instagram)\.com/[^\s]+)',
        text
    )
    modified_text = text
    # Замена ссылок на новые значения
    for url in urls:
        if 'x.com' in url:
            modified_text = modified_text.replace(
                url,
                url.replace('x.com', 'fixupx.com')
            )
        elif 'twitter.com' in url:
            modified_text = modified_text.replace(
                url,
                url.replace('twitter.com', 'vxtwitter.com')
            )
        elif 'instagram.com' in url:
            modified_text = modified_text.replace(
                url,
                url.replace('instagram.com', 'ddinstagram.com')
            )
    await message.reply(f"Modified text:\n{modified_text}")


async def main() -> None:
    await dp.start_polling(bot)


# Запуск бота
if __name__ == '__main__':
    asyncio.run(main())
