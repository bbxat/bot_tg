import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Настройки из Railway Variables
    API_ID = int(os.getenv('API_ID', 25922102))
    API_HASH = os.getenv('API_HASH', '801b220e3861a01c383d61e4491c54f4')
    BOT_TOKEN = os.getenv('BOT_TOKEN', '8108379584:AAG1D_YwPmx2_tBeIbJn8Cp9bCsW4k9Hx7k bot')  # Токен друга
    CHANNEL_USERNAME = os.getenv('CHANNEL_USERNAME', '@channel')
    ADMIN_ID = int(os.getenv('ADMIN_ID', 8465366061))  # ID друга
    DELAY_SECONDS = int(os.getenv('DELAY_SECONDS', 5))
    
    # Файлы
    LOG_FILE = 'forwarded_messages.log'
    GROUPS_FILE = 'groups.json'
    SCHEDULE_FILE = 'schedule.json'
