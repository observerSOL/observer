import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.engine.analyzer import fetch_transaction_data, calculate_risk

load_dotenv()
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("🤖Observer запущен.\nПришли Signature транзакции для анализа.")

@dp.message()
async def analyze_tx(message: types.Message):
    signature = message.text.strip()
    if len(signature) < 64:
        await message.answer("❌ Это не похоже на Solana Signature.")
        return

    msg = await message.answer("⏳ Анализирую блокчейн...")
    data = fetch_transaction_data(signature)
    
    if not data:
        await msg.edit_text("❌ Транзакция не найдена (проверь Signature).")
        return

    level, score = calculate_risk(data)
    await msg.edit_text(f"🛡 **Отчет безопасности**\n\nРиск: {level}\nБаллы: {score}", parse_mode="Markdown")

async def main():
    print("Бот работает...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())