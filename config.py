from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "0ff15ae2153bd8e03b48cb293010bc6a")
      API_ID = int(getenv("API_ID", "22672907"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "6982341614:AAHCwiX90PtKsRyGKvVIJ9BLrQlkCq1Bzp8")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1001722984461:-1001623633000").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
