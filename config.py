import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Настройки из Railway Variables
    API_ID = int(os.getenv('API_ID', 0))
    API_HASH = os.getenv('API_HASH', '')
    BOT_TOKEN = os.getenv('BOT_TOKEN', '')  # Токен друга
    CHANNEL_USERNAME = os.getenv('CHANNEL_USERNAME', '@channel')
    ADMIN_ID = int(os.getenv('ADMIN_ID', 0))  # ID друга
    DELAY_SECONDS = int(os.getenv('DELAY_SECONDS', 5))
    
    # Файлы
    LOG_FILE = 'forwarded_messages.log'
    GROUPS_FILE = 'groups.json'
    SCHEDULE_FILE = 'schedule.json'
