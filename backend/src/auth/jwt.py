from jose import jwt, JWTError, ExpiredSignatureError

from datetime import datetime, timedelta, UTC

from settings.config import get_settings


def encode_token(user_id: str) -> str:
    settings = get_settings()
    crated_at = datetime.now(UTC)
    payload = {
        "sub": user_id,
        "exp": crated_at + timedelta(minutes=int(settings.ACCESS_TOKEN_EXPIRE_MINUTES)),
        "iat": crated_at,
    }

    return jwt.encode(
        claims=payload, key=settings.SECRET_KEY, algorithm=settings.JWT_ALGORYTHM
    )


def decode_token(token: str) -> str:
    settings = get_settings()
    payload = jwt.decode(
        token, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORYTHM]
    )

    return payload["sub"]
