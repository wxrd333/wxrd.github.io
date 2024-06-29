# webapp_server.py

from aiohttp import web
import sqlite3
import random

async def handle(request):
    data = await request.json()
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    code = f"{random.randint(10, 99)}-{random.randint(1000, 9999)}"
    cursor.execute("""
        INSERT INTO cash_register (place, issues, accepts, amount, code, has_recount)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (data["place"], data["issues"], data["accepts"], data["amount"], code, data["has_recount"]))
    conn.commit()
    conn.close()

    # Отправка сообщения в Telegram
    bot = request.app["bot"]
    chat_id = data["chat_id"]
    summary = (
        f"Итоговая заявка:\n"
        f"Место: {data['place']}\n"
        f"Выдает: {data['issues']}\n"
        f"Принимает: {data['accepts']}\n"
        f"Сумма: {data['amount']}\n"
        f"Код: {code}\n"
        f"Есть пересчет: {'Да' if data['has_recount'] else 'Нет'}"
    )
    await bot.send_message(chat_id, summary)

    return web.json_response({"ok": True})

app = web.Application()
app.add_routes([web.post('/submit', handle)])

if __name__ == "__main__":
    web.run_app(app, host="0.0.0.0", port=8080)
