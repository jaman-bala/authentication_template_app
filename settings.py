from envparse import Env

env = Env()

REAL_DATABASE_URL = env.str(
    "REAL_DATABASE_URL",
    default="postgresql+asyncpg://superuser_db:ZAQ12345tgb@0.0.0.0:5432/db"
)

