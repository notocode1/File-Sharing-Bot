import os
import logging
from logging.handlers import RotatingFileHandler

# API Configuration
API_HASH = os.environ.get('API_HASH', None)
APP_ID = int(os.environ.get('APP_ID', 0))
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
OWNER_ID = int(os.environ.get("OWNER_ID", "12345678"))

# Channel ID
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "0"))

# Adding three forced subscription channels
FORCE_SUB_CHANNEL_1 = 'YourFirstChannelID'
FORCE_SUB_CHANNEL_2 = 'YourSecondChannelID'
FORCE_SUB_CHANNEL_3 = 'YourThirdChannelID'

# Bot workers
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\\n\\nI can store private files in Specified Channel and other users can access it from special link.")

# Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\\n\\n<b>You need to join in my Channel/Group to use me\\n\\nKindly Please join Channel</b>")

# Set your custom caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Set True if you want to prevent users from forwarding files from the bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

# Set true if you want to disable your channel posts share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

# Bot Stats Message
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\\n{uptime}"

# User Reply Text when they send direct messages
USER_REPLY_TEXT = "❌ Don't send me messages directly! I'm only a file-sharing bot."

# Logging configuration
LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)

logging.getLogger("pyrogram").setLevel(logging.WARNING)

try:
    ADMINS = []
    for admin_id in os.environ.get("ADMINS", "").split():
        ADMINS.append(int(admin_id))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

ADMINS.append(OWNER_ID)

# Function to retrieve logger instances
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)