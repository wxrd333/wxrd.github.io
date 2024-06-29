# bot.py

import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiohttp import web
from config import BOT_TOKEN, WEBAPP_URL
from start_handler import router as start_router
from cash_register_handler import router as cash_register_router
from webapp_server import app as webapp

logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(start_router)
    dp.include_router(cash_register_router)

    webapp["bot"] = bot
    webapp_runner = web.AppRunner(webapp)
    await webapp_runner.setup()
    site = web.TCPSite(webapp_runner, "0.0.0.0", 8080)
    await site.start()

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

