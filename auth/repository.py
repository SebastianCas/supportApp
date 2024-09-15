from .schema import Users
from config.database import connection
import hashlib

async def getUser(username: str):
    conn= connection()
    cur = conn.cursor()
    
    GetQuery = """
    SELECT * FROM users WHERE username = %s; 
    """
    cur.execute(GetQuery, (username,))
    user = cur.fetchone()
    
    cur.close()
    conn.close()
    return user


async def createUser(userData: Users):
    conn= connection()
    cur = conn.cursor()
    
    CreateQuery = """
    INSERT INTO users (username, password) VALUES (%s, %s);
    """
    passHashed = hashlib.sha256(userData.password.encode()).hexdigest()
    
    cur.execute(CreateQuery, (userData.username, passHashed))
    conn.commit()
    cur.close()
    conn.close()
    return {"success":True,"message": "User created successfully"}

async def searchUsers():
    conn= connection()
    cur = conn.cursor()
    
    GetQuery = """
    SELECT * FROM users; 
    """
    cur.execute(GetQuery)
    
    users = cur.fetchall()
    cur.close()
    conn.close()
    return users