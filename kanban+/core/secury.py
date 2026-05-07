from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
from http import HTTPStatus
from ..db.session import Settings
from jwt import encode, decode, DecodeError
from pwdlib import PasswordHash
from datetime import datetime, timedelta, timezone
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from ..models.model import User
from ..db.session import get_session
from sqlalchemy import select

ouath_bearer = OAuth2PasswordBearer(
    tokenUrl='api/auth/token'
)

passW_hash = PasswordHash.recommended()

toked = Annotated[str, Depends(ouath_bearer)]
Session = Annotated[AsyncSession, Depends(get_session)]

def hash_passWord(plainText: str):
    return passW_hash.hash(plainText)

def verify_passWord(plainText: str, hash_pass: str):
    return passW_hash.verify(plainText, hash_pass)

def create_token(date: dict):
    to_encode = date.copy()
    expire = datetime.now(tx=timezone.utc) + timedelta(minutes=Settings().EXPIRE_TOKEN)
    to_encode.update({'exp': expire})
    return encode(to_encode, Settings().SECRET_KEY, algorithm=Settings().ALGORITHHM)



def check_token(token: toked, session: Session):
    response_http = HTTPException(
        status_code=HTTPStatus.UNAUTHORIZED,
        detail='Usuario não-autenticado',
        headers={'WWW-Athenticate': False}
        )
    
    try:
        playload = decode(token, Settings().SECRET_KEY, algorithms=[Settings().ALGORITHHM])
        get_id = playload.get('sub')
        if not get_id:
            raise response_http
    except DecodeError:
        raise response_http
    
    id_user_parse = int(get_id)
    user = session.scalar(select(User).where(User.id == id_user_parse))

    if not user:
        raise response_http
    
    return user

