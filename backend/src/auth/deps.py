from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import ExpiredSignatureError
from starlette import status

from api.dependencies import UserRepo
from auth.jwt import decode_token
from db.models import User

bearer = HTTPBearer()


def get_access_token(creds: HTTPAuthorizationCredentials = Depends(bearer)):
    return creds.credentials


async def get_auth_user(repo: UserRepo, token: str = Depends(get_access_token)) -> User:
    try:
        user_id = decode_token(token=token)
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    user = await repo.get(int(user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found."
        )
    return user


async def get_superuser(user: User = Depends(get_auth_user)):
    if not user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Access not allowed"
        )
    return user


UserDep = Annotated[User, Depends(get_auth_user)]
