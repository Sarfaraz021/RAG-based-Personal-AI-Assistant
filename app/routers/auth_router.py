from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from app.models.user_model import User
from app.utils.security import verify_password, get_password_hash
from app.database import get_user_collection
from typing import Optional

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"


async def authenticate_user(username: str, password: str):
    users_collection = get_user_collection()
    user = await users_collection.find_one({"username": username})
    if not user or not verify_password(password, user['password']):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token_data = {"sub": username}
    token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)
    return token


@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    token = await authenticate_user(form_data.username, form_data.password)
    return {"access_token": token, "token_type": "bearer"}


async def create_user(email: str, password: str):
    users_collection = get_user_collection()
    existing_user = await users_collection.find_one({"email": email})
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    hashed_password = get_password_hash(password)
    user = {"email": email, "hashed_password": hashed_password}
    result = await users_collection.insert_one(user)
    return result.inserted_id


@router.post("/signup")
async def signup(user: User):
    user_id = await create_user(user.email, user.password)
    return {"user_id": str(user_id), "message": "User created successfully"}


async def get_current_user(token: str = Depends(oauth2_scheme)) -> Optional[dict]:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # Here you tell it can be `str` or `None`
        username: Optional[str] = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    users_collection = get_user_collection()
    user = await users_collection.find_one({"username": username})
    if user is None:
        raise credentials_exception
    return user
