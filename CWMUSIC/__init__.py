from CWMUSIC.core.bot import Anony
from CWMUSIC.core.dir import dirr
from CWMUSIC.core.git import git
from CWMUSIC.core.userbot import Userbot
from CWMUSIC.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
