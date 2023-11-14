from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "2802538"))
    API_HASH = getenv("API_HASH", "7bc625df204180e82ef3992f33ec8f0a")
    BOT_TOKEN = getenv("BOT_TOKEN", "5937806266:AAFhiH4ErjRHaqgZlFOHAmFB5KeHQ1gTK0U")
    FSUB = getenv("FSUB", "MovieMalonie")
    CHID = int(getenv("CHID", "-1001707587586"))
    SUDO = list(map(int, getenv("SUDO").split()))
    MONGO_URI = getenv("MONGO_URI", "")
    
cfg = Config()
