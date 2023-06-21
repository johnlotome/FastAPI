from .config import settings

def db_url(uri=settings.DATABASE_URL):

    if uri and uri.startswith("postgres://"):
            uri = uri.replace("postgres://", "postgresql://", 1)

    return uri