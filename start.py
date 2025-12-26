import asyncio
from telethon import TelegramClient

async def create_session():
    print("=== СОЗДАНИЕ СЕССИИ ДЛЯ БОТА ===")
    
    # Запрашиваем данные
    api_id = input("Введите API ID (число с my.telegram.org): ")
    api_hash = input("Введите API Hash (строка с my.telegram.org): ")
    phone = input("Введите телефон (+79991234567): ")
    
    # Создаём клиента
    client = TelegramClient('user_session', int(api_id), api_hash)
    
    # Запускаем авторизацию
    await client.start(phone)
    
    print("✅ Сессия создана успешно!")
    print("Файл 'user_session.session' готов.")
    print("Пришли этот файл мне.")
    
    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(create_session())
