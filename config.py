import re
from os import environ
from translation import Afsalibrary
id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "on"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "off"]:
        return False
    else:
        return default

# ==================================
API_ID = int(environ["API_ID"])
API_HASH = environ["API_HASH"]
B_KEYS = environ["BOT_TOKEN"]
START_MSG = environ.get("START_MSG", Afsalibrary.DEFAULT_MSG)
BOT_PICS = (environ.get('PICS', 'https://www.bing.com/images/search?view=detailV2&ccid=JVnrxNT8&id=FD3CE0B2F559AED5FDAF3BC6F229CE79BD0DC32A&thid=OIP.JVnrxNT8OArdjx_dMFeBkgHaHa&mediaurl=https%3a%2f%2fimage.freepik.com%2ffree-vector%2febook_24908-54028.jpg&exph=626&expw=626&q=ebooks+downloader&simid=608033954806789569&FORM=IRPRST&ck=97BAD295E9512C1410E9B0A8C41D925B&selectedIndex=35&ajaxhist=0&ajaxserp=0')).split()
SUPPORT = environ.get("SUPPORT", "t.me/alifdrive")
SPELL_MODE = is_enabled((environ.get('SPELL_MODE', "on")), True)
SET_SPEL_M = environ.get("SPELL_MODE_TEXT", Afsalibrary.SPELL_CHECK)
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", None))
DATABASE_URI = environ.get("DATABASE_URI", None)
FORCE = environ.get('FORCES_SUB')
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", Afsalibrary.FILE_CAPTIONS)
DEV_NAME = environ.get("DEV_NAME", "Muhammed Adnan K")
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['CHANNELS'].split()]
AUTH_GROUPS = [int(admin) for admin in environ.get("AUTH_GROUPS", "").split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]


# ==================================
# Empty 😂
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
BUTTONS = {}
CURRENT = int(environ.get("SKIP", 2))
CANCEL = False
FORCES_SUB = int(FORCE) if FORCE and id_pattern.search(FORCE) else FORCE
DATABASE_NAME = environ.get("DATABASE_NAME", 'Afsalibrary')
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
# ==================================
# About Bot 🤖
class bot_info(object):
    BOT_NAME = None
    BOT_USERNAME = None
    BOT_ID = None


