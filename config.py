import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters
load_dotenv()



#Basic-Setup
OWNER_ID = int(getenv("OWNER_ID"))
LOGGER_ID = int(getenv("LOGGER_ID", None))

#Bot-Setup
BOT_TOKEN = getenv("BOT_TOKEN")

#MongoDB-Setup
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

#Assistant-Setup
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))



SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Life_Codes")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Life_Codes")

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv("UPSTREAM_REPO","https://github.com/JustAyu/Aest")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)  # Fill this variable if your upstream repository is private

#Limits
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 250))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 100))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://i.pinimg.com/236x/57/ec/22/57ec223ee51d8753168de1af3ede1aeb.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://i.pinimg.com/564x/d9/b5/46/d9b5464b3de60b9b1df325e41cf22fd3.jpg"
)
STATS_IMG_URL = "https://i.pinimg.com/originals/2f/b8/d3/2fb8d33c12f3816e5bfed7fe614d447a.jpg"
PLAYLIST_IMG_URL = "https://i.pinimg.com/736x/ea/e1/e3/eae1e38f90928b64acf67a85462667ea.jpg"
TELEGRAM_AUDIO_URL = "https://i.pinimg.com/736x/71/e8/4b/71e84b0169197bece76520e3979cf899.jpg"
TELEGRAM_VIDEO_URL = "https://i.pinimg.com/736x/71/e8/4b/71e84b0169197bece76520e3979cf899.jpg"
STREAM_IMG_URL = "https://i.pinimg.com/originals/03/e8/db/03e8db879f8e9a0a83514b135260e182.jpg"
YOUTUBE_IMG_URL = "https://i.pinimg.com/originals/d0/30/eb/d030ebe0b24de823dda499ac37301eb2.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://w0.peakpx.com/wallpaper/407/1022/HD-wallpaper-wets-female-wet-brown-eyes-sexy-cute-short-hair-girl-anime-hot-anime-girl-black-hair-night.jpg"
SPOTIFY_ALBUM_IMG_URL = SPOTIFY_ARTIST_IMG_URL
SPOTIFY_PLAYLIST_IMG_URL = SPOTIFY_ARTIST_IMG_URL


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
