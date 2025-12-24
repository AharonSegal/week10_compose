import mysql.connector
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

"""
docker exec -it mysql_db mysql -uroot -ppass -e "USE contacts_db; SHOW TABLES;"
docker exec -it mysql_db mysql -uroot -ppass -e "USE contacts_db; SELECT * FROM contacts;"
"""

# Read env vars, but make sure we always have a non-None default
ROOT_PASS = os.getenv("ROOT_PASS")
DB_NAME   = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")

def get_connection():
    # DEBUG: this will show in your FastAPI log
    print(
        f"[DB DEBUG] ROOT_PASS={repr(ROOT_PASS)}, "
        f"DB_NAME={repr(DB_NAME)}, "
        f"has_password={bool(ROOT_PASS)}"
    )

    return mysql.connector.connect(
        host="127.0.0.1",  
        port=3307,          
        user=DB_USER,        
        password=ROOT_PASS, 
        database=DB_NAME
    )

