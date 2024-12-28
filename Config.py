from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

class Config(object):
    # required config variables
    API_HASH = getenv("API_HASH", "28362850")                # get from my.telegram.org
    API_ID = int(getenv("API_ID", "34f9cb93364db16fc45d003e4c81d97a"))                  # get from my.telegram.org
    BOT_TOKEN = getenv("BOT_TOKEN", "7820751181:AAFDMs4SVMkyjv23Wem_jHm1w254OwCCNO8")              # get from @BotFather
    DATABASE_URL = getenv("DATABASE_URL", "mongodb+srv://VamsixD:VamsixD@vamsi.x7gyybv.mongodb.net/?retryWrites=true&w=majority")     # from https://cloud.mongodb.com/
    HELLBOT_SESSION = getenv("HELLBOT_SESSION", "BQGwyGIAYTDXU1NQkRj9arPB22kBothsLUsSo3Q0YXafvcjDJdG5Hy-r8QmUXE_VZbLZNKy3O8j4MHE4HnxYJIzsJIS5bEL-QevcbHZcEu78JG1o-dxTo_0NZcAhs-7A9qrkGVmZg0gY3Q3AJ94ENrWpVQsc_a1J_abDcKsPj0YaJEVXoc6qlX6jy6KiylgIIypNyhjSByWuzG1yKnhmEyg2gs0zSm8GOqOdjoX2oy3_vCF6-SDX-47tbec4MtlLFLd4bBtKWld8Xll3s2cALCvdUYQ5YpWtKAvgYeWXKhZ0gUDvbTateQYV53IVUis2a2ByB_vqtwCjc5_uRpkjp-KtA1XQmgAAAAHETnMdAA")  # enter your session string here
    LOGGER_ID = int(getenv("LOGGER_ID", "-1002141779241"))            # make a channel and get its ID
    OWNER_ID = getenv("OWNER_ID", "7635867946")                  # enter your id here

    # optional config variables
    BLACK_IMG = getenv("BLACK_IMG", "https://telegra.ph/file/2c546060b20dfd7c1ff2d.jpg")        # black image for progress
    BOT_NAME = getenv("BOT_NAME", "\x40\x4d\x75\x73\x69\x63\x5f\x48\x65\x6c\x6c\x42\x6f\x74")   # dont put fancy texts here.
    BOT_PIC = getenv("BOT_PIC", "https://te.legra.ph/file/5d5642103804ae180e40b.jpg")           # put direct link to image here
    LEADERBOARD_TIME = getenv("LEADERBOARD_TIME", "3:00")   # time in 24hr format for leaderboard broadcast
    LYRICS_API = getenv("LYRICS_API", None)             # from https://docs.genius.com/
    MAX_FAVORITES = int(getenv("MAX_FAVORITES", 30))    # max number of favorite tracks
    PLAY_LIMIT = int(getenv("PLAY_LIMIT", 0))           # time in minutes. 0 for no limit
    PRIVATE_MODE = getenv("PRIVATE_MODE", "off")        # "on" or "off" to enable/disable private mode
    SONG_LIMIT = int(getenv("SONG_LIMIT", 0))           # time in minutes. 0 for no limit
    TELEGRAM_IMG = getenv("TELEGRAM_IMG", None)         # put direct link to image here
    TG_AUDIO_SIZE_LIMIT = int(getenv("TG_AUDIO_SIZE_LIMIT", 104857600))     # size in bytes. 0 for no limit
    TG_VIDEO_SIZE_LIMIT = int(getenv("TG_VIDEO_SIZE_LIMIT", 1073741824))    # size in bytes. 0 for no limit
    TZ = getenv("TZ", "Asia/Kolkata")   # https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

    # do not edit these variables
    BANNED_USERS = filters.user()
    CACHE = {}
    CACHE_DIR = "./cache/"
    DELETE_DICT = {}
    DWL_DIR = "./downloads/"
    GOD_USERS = filters.user()
    PLAYER_CACHE = {}
    QUEUE_CACHE =  {}
    SONG_CACHE = {}
    SUDO_USERS = filters.user()


# get all config variables in a list
all_vars = [i for i in Config.__dict__.keys() if not i.startswith("__")]
