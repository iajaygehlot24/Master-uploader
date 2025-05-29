import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7706309668:AAFdPwaXQt8_1PSHSJX_cmMpLP7AjIw88CQ")  # Ensure correct key name
    API_ID = int(os.environ.get("API_ID", "10634878"))  # Added key name and default value
    API_HASH = os.environ.get("API_HASH", "2eab99b8459017fff27395cc52f3c860")  # Added key name for consistency

    AUTH_USER = os.environ.get("AUTH_USERS", "1168219996").split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]  # Ensuring list of integers

    HOST = os.environ.get("HOST", "https://api.masterapi.tech")  # Keeping HOST configurable
    CREDIT = os.environ.get("CREDIT", "𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎")  # Making CREDIT an environment variable for flexibility
