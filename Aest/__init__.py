from Aest.core.bot import Anony
from Aest.core.dir import dirr
from Aest.core.git import git
from Aest.core.userbot import Userbot
from Aest.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
