import os

from config import Config
from GDNBharath.core.logger import LOGS


# make required directories
if not os.path.isdir(Config.DWL_DIR):
    os.makedirs(Config.DWL_DIR)
if not os.path.isdir(Config.CACHE_DIR):
    os.makedirs(Config.CACHE_DIR)


# If any of the important variables are missing stop the bot from starting
if Config.API_ID == 0:
    LOGS.error("\x41\x50\x49\x20\x49\x44\x20\x69\x73\x20\x6d\x69\x73\x73\x69\x6e\x67\x21\x20\x4b\x69\x6e\x64\x6c\x79\x20\x63\x68\x65\x63\x6b\x20\x61\x67\x61\x69\x6e\x21")
    quit(1)
if not Config.API_HASH:
    LOGS.error("\x41\x50\x49\x20\x48\x41\x53\x48\x20\x69\x73\x20\x6d\x69\x73\x73\x69\x6e\x67\x21\x20\x4b\x69\x6e\x64\x6c\x79\x20\x63\x68\x65\x63\x6b\x20\x61\x67\x61\x69\x6e\x21")
    quit(1)
if not Config.BOT_TOKEN:
    LOGS.error("\x42\x4f\x54\x20\x54\x4f\x4b\x45\x4e\x20\x69\x73\x20\x6d\x69\x73\x73\x69\x6e\x67\x21\x20\x4b\x69\x6e\x64\x6c\x79\x20\x63\x68\x65\x63\x6b\x20\x61\x67\x61\x69\x6e\x21")
    quit(1)
if not Config.DATABASE_URL:
    LOGS.error("\x44\x41\x54\x41\x42\x41\x53\x45\x20\x55\x52\x4c\x20\x69\x73\x20\x6d\x69\x73\x73\x69\x6e\x67\x21\x20\x4b\x69\x6e\x64\x6c\x79\x20\x63\x68\x65\x63\x6b\x20\x61\x67\x61\x69\x6e\x21")
    quit(1)
if Config.LOGGER_ID == 0:
    LOGS.error("\x4c\x4f\x47\x47\x45\x52\x20\x49\x44\x20\x69\x73\x20\x6d\x69\x73\x73\x69\x6e\x67\x21\x20\x4b\x69\x6e\x64\x6c\x79\x20\x63\x68\x65\x63\x6b\x20\x61\x67\x61\x69\x6e\x21")
    quit(1)
if not Config.OWNER_ID:
    LOGS.error("\x4f\x57\x4e\x45\x52\x20\x49\x44\x20\x69\x73\x20\x6d\x69\x73\x73\x69\x6e\x67\x21\x20\x4b\x69\x6e\x64\x6c\x79\x20\x63\x68\x65\x63\x6b\x20\x61\x67\x61\x69\x6e\x21")
    quit(1)
if not Config.HELLBOT_SESSION:
    LOGS.error("\x48\x45\x4c\x4c\x42\x4f\x54\x20\x53\x45\x53\x53\x49\x4f\x4e\x20\x69\x73\x20\x6d\x69\x73\x73\x69\x6e\x67\x21\x20\x4b\x69\x6e\x64\x6c\x79\x20\x63\x68\x65\x63\x6b\x20\x61\x67\x61\x69\x6e\x21")
    quit(1)
