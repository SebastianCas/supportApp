import psycopg2
from psycopg2.extras import RealDictCursor

def connection():
    conn = psycopg2.connect(
        host="database-1.c30cxtzlflsq.us-east-1.rds.amazonaws.com",
        database="supportApp",
        user="postgres",
        password="postgres1234",
        cursor_factory=RealDictCursor
    )
    return conn