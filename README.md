<!-- 

             /$$                                 /$$  
            | $$                               /$$$$  
  /$$$$$$$ /$$$$$$    /$$$$$$   /$$$$$$       |_  $$  
 /$$_____/|_  $$_/   /$$__  $$ /$$__  $$        | $$  
|  $$$$$$   | $$    | $$$$$$$$| $$  \ $$        | $$  
 \____  $$  | $$ /$$| $$_____/| $$  | $$        | $$  
 /$$$$$$$/  |  $$$$/|  $$$$$$$| $$$$$$$/       /$$$$$$
|_______/    \___/   \_______/| $$____/       |______/
                              | $$                    
                              | $$                    
                              |__/                      

                                                             -->

# What is achieved in this step

**FastAPI application** connected to a **MySQL database**
    fully containerized using **Docker Compose**.
    Configuration is handled via environment variables to keep secrets out of code and to support clean dev/prod workflows.

**Docker Compose**
    ↓
**FastAPI** 
    project initialized with a clean skeleton structure
    Base API application created and running inside Docker
    Skeleton endpoints defined (structure in place, logic can be added later)

**MySQL database** 
    container running via Docker Compose
    Persistent MySQL volume configured to retain data across restarts
    Automatic database initialization using an SQL init script
    Secure database access using environment variables
    Clear separation between application configuration and database configuration
    App-to-database communication via Docker network

## 🧱 Docker Compose Build Overview

The system consists of **two services**:

* **`app`** – FastAPI backend
* **`database`** – MySQL 8 database

They run on the same Docker network and communicate using the MySQL service name (`database`) as the hostname.

## ⚙️ Configuration

### Services

#### App (FastAPI)

* Built from `./app`
* Exposes port **8080**
* Connects to MySQL using environment variables
* Waits for the database to become healthy before starting

#### Database (MySQL)

* Uses the official `mysql:8` image
* Initializes the database on first startup
* Persists data using a Docker volume
* Runs an init SQL script to create tables

---

## 🔐 Environment Variables (`.env`)

All configuration is centralized in a `.env` file.

* `MYSQL_*` variables → **database setup**
* `DB_*` variables → **application runtime**

### Database initialization (used by MySQL container)

```env
MYSQL_ROOT_PASSWORD=rootpassword
MYSQL_DATABASE=contacts_db
MYSQL_USER=appuser
MYSQL_PASSWORD=apppassword
```

### Application connection (used by FastAPI)

```env
DB_HOST=database
DB_PORT=3306
DB_USER=appuser
DB_PASSWORD=apppassword
DB_NAME=contacts_db
```

## 🗂️ Database Initialization

On first startup, MySQL automatically runs:

```
/app/sql/init.sql
```

```sql
CREATE TABLE contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(20) NOT NULL
);
```

This happens **only once**, when the database volume is empty.

<!-- 
             /$$                                /$$$$$$ 
            | $$                               /$$__  $$
  /$$$$$$$ /$$$$$$    /$$$$$$   /$$$$$$       |__/  \ $$
 /$$_____/|_  $$_/   /$$__  $$ /$$__  $$        /$$$$$$/
|  $$$$$$   | $$    | $$$$$$$$| $$  \ $$       /$$____/ 
 \____  $$  | $$ /$$| $$_____/| $$  | $$      | $$      
 /$$$$$$$/  |  $$$$/|  $$$$$$$| $$$$$$$/      | $$$$$$$$
|_______/    \___/   \_______/| $$____/       |________/
                              | $$                      
                              | $$                      
                              |__/        
                                             -->
## 🔄 Build & Startup Flow (Detailed)

### 1. `docker-compose up --build`

* Docker Compose reads `docker-compose.yml`
* Loads variables from `.env`

### 2. MySQL container starts

* Reads `MYSQL_*` variables
* Initializes MySQL data directory
* Creates:

  * Database
  * User
  * Permissions
* Runs `init.sql`
    thanks to this line in the compose 
        - ./app/sql/init.sql:/docker-entrypoint-initdb.d/init.sql:ro
* Marks itself **healthy**

### 3. FastAPI container starts

* Waits for MySQL health check
* Reads `DB_*` variables
* Starts the FastAPI server
* Opens DB connections using `appuser`

### 4. Application is ready

* API available at `http://localhost:8080`
* Database persists data via Docker volume
* MySQL accessible via CLI or MySQL Workbench

## make shure port is availble
```bash
netstat -ano | findstr :8080
```

##  Commands
```bash
docker-compose up -d --build
```
### Stop everything
```bash
docker-compose down
```
### View database from container
```bash
docker exec -it mysql_db mysql -u appuser -papppassword contacts_db
```
### View database from host
```bash
mysql -h 127.0.0.1 -P 3306 -u appuser -papppassword contacts_db
```

