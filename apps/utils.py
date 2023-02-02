from apps.database import SQLALCHEMY_DATABASE_URL, SessionLocal, engine


async def check_db_connected():
    try:
        print(SQLALCHEMY_DATABASE_URL)
        if not str(SQLALCHEMY_DATABASE_URL).__contains__('sqlite'):
            db = SessionLocal()
            print(engine.connect())
            print(db.connection())
            if not db.is_active:
                await db.connection()
        print("Database is connected (^_^)")
    except Exception as e:
        print("Looks like there is some problem in connection,see below traceback")
        raise e
