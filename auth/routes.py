from fastapi import APIRouter, HTTPException
from .schema import Users
from .repository import getUser, createUser, searchUsers
from .helper import verifyPassword
import jwt

SECRET_KEY = "QXBsaWNhdGlvbnB5dGhvblBydWViYTIwMjQ="
ALGORITHM = "HS256"

app = APIRouter(
    prefix="/auth",
)

@app.post("/register")
async def registerUser(userData: Users):
    user = await getUser(userData.username);
    if user:
        return HTTPException(status_code=404, detail="User already exists")
    
    return await createUser(userData)

@app.post("/login")
async def userLogin(userData: Users):
    user = await getUser(userData.username)
    if not user or not verifyPassword(userData.password, user['password']):
        return HTTPException(status_code=401, detail="Invalid username or password")

    token = jwt.encode({"sub": userData.username, "userid": user['id']}, SECRET_KEY, algorithm=ALGORITHM)
    return {"token": token}

@app.get("/users")
async def getUsers():
    users = await searchUsers()
    if not users:
        return HTTPException(status_code=404, detail="No users found")
    
    return await searchUsers()