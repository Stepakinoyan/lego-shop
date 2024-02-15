from fastapi_users.authentication import AuthenticationBackend, BearerTransport, JWTStrategy
from app.config import settings


SECRET = settings.SECRET

cookie_transport = BearerTransport(tokenUrl="auth/jwt/login")

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)