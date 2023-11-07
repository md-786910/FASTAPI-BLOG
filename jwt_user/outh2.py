from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from . import jwtSign

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/login")


async def get_current_user(data: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    print(f"data {data}")
    print(f"Crendtial {credentials_exception}")

    return jwtSign.verify_token(data, credentials_exception)
