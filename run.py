import asyncio
import logging

from aiogram import Bot, Dispatcher
from config import tkn
from handlers import router

bot = Bot(token=tkn)
dp = Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        logging.basicConfig(level=logging.INFO)
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
