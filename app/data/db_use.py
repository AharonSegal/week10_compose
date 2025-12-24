import mysql.connector
import os

"""
docker exec -it mysql_db mysql -uroot -ppass -e "USE contacts_db; SHOW TABLES;"
docker exec -it mysql_db mysql -uroot -ppass -e "USE contacts_db; SELECT * FROM contacts;"
"""

import os
import mysql.connector

# Read env vars, but make sure we always have a non-None default
ROOT_PASS = os.getenv("ROOT_PASS") or "pass"        # default: "pass"
DB_NAME   = os.getenv("DB_NAME")   or "contacts_db" # default: "contacts_db"

def get_connection():
    # DEBUG: this will show in your FastAPI log
    print(
        f"[DB DEBUG] ROOT_PASS={repr(ROOT_PASS)}, "
        f"DB_NAME={repr(DB_NAME)}, "
        f"has_password={bool(ROOT_PASS)}"
    )

    return mysql.connector.connect(
        host="127.0.0.1",   # MySQL is on your host at 127.0.0.1
        port=3307,          # mapped from container 3306 -> host 3307
        user="root",        # same as MYSQL_ROOT_PASSWORD user
        password=ROOT_PASS, # MUST be non-None to avoid 'using password: NO'
        database=DB_NAME
    )


"""
for prod 

def get_connection():
    return mysql.connector.connect(
        host="database",    # MySQL service name from docker-compose.
                            # Docker DNS resolves "database" to the MySQL container.

        port=3306,          # MySQL's internal port inside the Docker network.
                            # You do NOT use 3307 here; 3307 is only for the host.

        user="root",        # Same user, root, unless you configure MYSQL_USER.

        password=ROOT_PASS, # Same env var, passed into the app container
                            # via env_file or environment in docker-compose.

        database=DB_NAME    # Same DB name, again from env var (contacts_db).
    )
    """