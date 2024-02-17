from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "29906518"))
API_HASH = getenv("API_HASH", "76a9e84e87200fb7311a2d779a42d13a")

BOT_TOKEN = getenv("BOT_TOKEN", "6819381670:AAGHM2b7aJHP_GE0LnXI8elW9odocGopieA")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "1556830659"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", "BQHIVlYAlMxFnknM3rkOWJRM-rYoBmQBchyB6oRZxdXVvwqTjhRiniLXSHYA8yJO3MH5YfUKIdwAlUwCpAy_d0D00lYDvtxDLpmOkalvs4XTRA2xUypUhGbtdqD5pkw0TzynwnksZDS4z3b7kO4X17DrpElVK6YbaR_mCSvduLQUUt5geAmHyj_qqmNB0PvCldaalPB-6cYcth8UHeftk4r_Mz0jpQJzBQqnlNzrteFy0Sus5QhfDVjYhMEp4yLK74l8sXNRRZEQRyBj0m2kSbN5Zf-4jQ88tO1hq9ZNHs1tbloBxWO7n7yMmnlomtg2jhmm4rjfqCghPpBnx9Z8Jf376NEwZgAAAAFt-yL1AA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DevilsHeavenMF")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FallenAssociation")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1556830659").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
