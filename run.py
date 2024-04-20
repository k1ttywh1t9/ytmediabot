import asyncio
import logging

from aiogram import Bot, Dispatcher
from config import tkn
from handlers import router
from playlist import router_playlist

bot = Bot(token=tkn)
dp = Dispatcher()

async def main():
    dp.include_router(router)
    dp.include_router(router_playlist)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        # logging.basicConfig(level=logging.INFO) # turn it on for debug
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
