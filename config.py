from os import environ

API_HASH = environ.get("API_HASH", "4e8f828046a30ec70899b523bd763fa9")
API_ID = int(environ.get("API_ID", "38751960"))
BOT_TOKEN = environ.get("BOT_TOKEN", "8658849738:AAFzvmhsJJLyEx82GtXNOwr06MqlKEbE08c")
BOT_OWNER = int(environ.get("BOT_OWNER", "7754709357"))
BOT_USERNAME = environ.get("BOT_USERNAME", "ProAutoReaction_bot")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1004365314045"))
AUTH_CHANNEL = int(environ.get("AUTH_CHANNEL", ""))
DATABASE_URL = environ.get("DATABASE_URL", "mongodb+srv://tgjiro441_db_user:Tgjirosamkun@cluster0.9reqco1.mongodb.net/?appName=Cluster0")

# Define default emojis list
EMOJIS = [
    "👍", "🤷‍♂", "❤", "🔥", "🥰", "👏", "😁", "🤔", "🤯", "😱", "🤬", "😢", 
    "🥶", "🤩", "🥳", "😎", "🙏", "👌", "🤣", "😇", "🥱", "🥴", "😍", "🤓", 
    "❤‍🔥", "🌚", "😐", "💯", "🦄", "⚡", "👾", "🏆", "💔", "🤨", "🌟", "😡", 
    "👅", "🆒", "😘", "😈", "😴", "😭", "👻", "🌈", "👨‍💻", "👀", "🎃", "🙄", 
    "🤧", "😨", "🤝", "🤐", "🤗", "🫡", "🤭", "🥸", "🤫", "😶‍🌫", "🤪", "😏"
]
