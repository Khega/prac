import mysql.connector
from fastapi import APIRouter, Depends, HTTPException
from fastapi.params import Body
from api.src.utils.db import db_create_user, db_reset_password
from api.src.utils.auth import create_access_token, get_current_user, OAuth2PasswordBearer

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/register")
async def register_user(user: dict = Body(...)):
    username_exists = db_check_username_exists(user['username'])
    if username_exists:
        raise HTTPException(status_code=400, detail="Username already registered")


    query = f"INSERT INTO users (username, password, email) VALUES ('{user['username']}', '{user['password']}', '{user['email']}')"
    db_create_user(query)
    return {"message": "User registered successfully"}

def db_check_username_exists(username):

    db_config = {
        "host": "your_host",
        "user": "your_username",
        "password": "your_password",
        "database": "your_database",
    }

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    try:
        cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
        user = cursor.fetchone()
        return bool(user)
    finally:
        cursor.close()
        conn.close()


@router.post("/reset-password")
async def reset_password(email: str = Body(...)):
    query = f"UPDATE users SET password_reset_token = 'generated_token' WHERE email = '{email}'"
    db_reset_password(query)
    return {"message": "Password reset instructions sent to your email"}

@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordBearer = Depends(oauth2_scheme)):
    token_data = {"sub": form_data.username}
    access_token = create_access_token(data=token_data)
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/users/me", response_model=dict)
async def read_users_me(current_user: dict = Depends(get_current_user)):
    return current_user
