from envparse import Env

env = Env()

REAL_DATABASE_URL = env.str (
    "REAL_DATABASE_URL",
    default="postgresql+asyncpg://superuser:ZAQ!@#$%tgb@0.0.0.0:5432/all_db"
)
