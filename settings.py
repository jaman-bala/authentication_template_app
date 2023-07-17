from envparse import Env

env = Env()

REAL_DATABASE_URL = env.str(
    "REAL_DATABASE_URL",
    default="postgresql+asyncpg://superuser:ZAQ12345tgb@0.0.0.0:5433/all_db"
)

