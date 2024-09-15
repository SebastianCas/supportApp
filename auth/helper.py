from fastapi import HTTPException, Header
import hashlib
import jwt

SECRET_KEY = "QXBsaWNhdGlvbnB5dGhvblBydWViYTIwMjQ="
ALGORITHM = "HS256"

def verifyPassword(password: str, hashedPassword: str):
    passwordHashed = hashlib.sha256(password.encode()).hexdigest()
    if passwordHashed == hashedPassword:
        return True
    return False

def getCurrentUser(Authorization: str = Header(...)):
    try:
        if not Authorization.startswith("Bearer "):
            raise HTTPException(status_code=401, detail="Invalid token")
        payload = jwt.decode(Authorization[len("Bearer "):], SECRET_KEY, algorithms=[ALGORITHM])
        userId = payload.get("userid")
        if userId is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return {"userid": userId}
    except jwt.PyJWKError:
        raise HTTPException(status_code=401, detail="Invalid token")