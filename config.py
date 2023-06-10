import os
from os import getenv
from dotenv import load_dotenv
from distutils.util import strtobool
TIME_LIMIT = int(getenv("TIME_LIMIT", "2592000"))
TIME_SLEEP = int(getenv("TIME_SLEEP", "86400"))

load_dotenv(".env")


API_ID = int(getenv("API_ID", "28785136")) #optional
API_HASH = getenv("API_HASH", "3435ed2cfee6ed694f365cabf2cfa559")
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://sarya:sarya@cluster0.fqlha2h.mongodb.net/?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2079755654").split()))
DEEP_AI = getenv("DEEP_AI", "d7394561-0528-4714-a1ee-edd7020b48e1")
OWNER_ID = int(getenv("OWNER_ID", "2079755654") or 0)
ADMIN1_ID = list(map(int, getenv("ADMIN1_ID", "1054295664").split()))
ADMIN2_ID = list(map(int, getenv("ADMIN2_ID", "1755047203").split()))


ADMIN1_ID.append(1054295664)
ADMIN2_ID.append(1755047203)


BOT_TOKEN = getenv("BOT_TOKEN", "5935406240:AAFJ0ZlPQiiuCBcp2Rj-1U5geHqhbaylndU")
PM_AUTO_BAN = strtobool(getenv("PM_AUTO_BAN", "True"))
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER", None)
OPENAI_API = getenv("OPENAI_API", "")
DB_URL = getenv("DATABASE_URL", "postgres://mcclbjwx:CqMrbec47cqL5KbaZOUDlVQWOscjNcKR@peanut.db.elephantsql.com/mcclbjwx")
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BOT_WORKERS = int(getenv("BOT_WORKERS", "2"))
USER_WORKERS = int(getenv("BOT_WORKERS", "8"))
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
BRANCH = getenv("BRANCH", "azazel") #don't change
REPO_URL = getenv("REPO_URL", "https://github.com/ayrizz/Azazel-Project")
CMD_HNDLR = getenv("CMD_HNDLR", ".")
SUPPORT = int(getenv("SUPPORT", "-1001812143750"))
CHANNEL = int(getenv("CHANNEL", "-1001896537650"))
SESSION1 = getenv("SESSION1", "BQAY8JIAgfUCwbSP91XJHYWO0DIgJjsU-0oWr-GIslzpNhbMq1KSTvhG84KKCPzbYJUvFoHVqNchGXEn-AvbpLItSeV0EHa72ui-Z69OOl_NaMiT7tPi-f2A_J3GIAQMgYrwsu0tCCdbNgbSqa98is4dkz9LLasC6VoRKkV54yna5nJeytzpyO3JQWtpNAaq3TZWv8dwNEWSW5bvbYrZEun8LMfAO6eqwDAUfPBRZ2VzwWQxsh8jR4ptedS8H5tAt0AZQ9eAieMoKNTpBYAzKHR05axKWi2Wvx8ZaAp_guBXxwh9S5aloxpDxbT2oqwOBz0LIRS3ONZm9GqoI7UyMpb1Wp1D4QAAAAB79o2GAA")
SESSION2 = getenv("SESSION2", "BQAY8JIAcOGWHdjhkQM2QQF1pTQspySQwkGAPAtorKr5tiA2N4n3f8E4D777EBl3gnWw1g3Fua1wjY-cmWy8pX4m87FmaMda_LcV66Giahx0KoQ_5kMEmRX7gKEtIYGD5Tk6VMGQbQmGqhxZJWF6G6ydt_USS5qnHRoKzraAkDncpta2kmOVKsgNDsSWbc02edJO-BRjcovFfE9SyevVZ_vcHmIelXoxl-f3WvsX_mjo3f4E3IA5wBFxfsXz_xT9cao3pwNJ3dbIe82bx9faeYeIjtVHWDQs6ctPC1rgFb64qLqAb6_w-kd4L73B7N94wiiem95WC0KQH4pVmBhBtsnYz6t2ewAAAAFPi-YRAA")
SESSION3 = getenv("SESSION3", "")
SESSION4 = getenv("SESSION4", "")
SESSION5 = getenv("SESSION5", "")
SESSION6 = getenv("SESSION6", "")
SESSION7 = getenv("SESSION7", "")
SESSION8 = getenv("SESSION8", "")
SESSION9 = getenv("SESSION9", "")
SESSION10 = getenv("SESSION10", "")
