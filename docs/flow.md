
<!-- __ _               
                          
███████ ██       ██████  ██     ██ 
██      ██      ██    ██ ██     ██ 
█████   ██      ██    ██ ██  █  ██ 
██      ██      ██    ██ ██ ███ ██ 
██      ███████  ██████   ███ ███  
                                   
                       -->
### **1️⃣ Status**
```bash
docker ps
docker ps -a
docker images
docker volume ls
docker system df -v
```
### **2️⃣ Build / Start**
```bash
docker-compose up
docker-compose up -d --build

uvicorn main:app --reload
uvicorn app.main:app --reload --host 127.0.0.1 --port 8090

http://127.0.0.1:8000/docs#/
```
### **3️⃣ Clear / Cleanup**
```bash

echo "Stopping all running containers..."
docker stop $(docker ps -q) 2>/dev/null || true

echo "Removing all containers..."
docker rm $(docker ps -a -q) 2>/dev/null || true

echo "Removing all images..."
docker rmi -f $(docker images -q) 2>/dev/null || true

echo "Removing all volumes..."
# Remove volumes only if they exist
volumes=$(docker volume ls -q)
if [ ! -z "$volumes" ]; then
  docker volume rm $volumes 2>/dev/null || true
fi

echo "Removing all custom networks..."
# Keep default networks (bridge, host, none)
networks=$(docker network ls -q | grep -v -E "bridge|host|none")
if [ ! -z "$networks" ]; then
  docker network rm $networks 2>/dev/null || true
fi

echo "Full Docker cleanup complete!"
docker system prune -af --volumes



docker images
docker rmi contact_manager-api
```
<!-- 
 /$$   /$$                                            
| $$$ | $$                                            
| $$$$| $$  /$$$$$$  /$$$$$$/$$$$   /$$$$$$   /$$$$$$$
| $$ $$ $$ |____  $$| $$_  $$_  $$ /$$__  $$ /$$_____/
| $$  $$$$  /$$$$$$$| $$ \ $$ \ $$| $$$$$$$$|  $$$$$$ 
| $$\  $$$ /$$__  $$| $$ | $$ | $$| $$_____/ \____  $$
| $$ \  $$|  $$$$$$$| $$ | $$ | $$|  $$$$$$$ /$$$$$$$/
|__/  \__/ \_______/|__/ |__/ |__/ \_______/|_______/ 
-->


# Service names
App service: app
Database service: database

# Container names
App container: backend_api
Database container: mysql_db

# Environment variables for App (FastAPI)
DB_HOST = database
DB_PORT = 3306
DB_USER = root
DB_PASSWORD = password
DB_NAME = contacts_db

# Environment variables for Database (MySQL)
MYSQL_ROOT_PASSWORD = password
MYSQL_DATABASE = contacts_db

# Network
Network name: app-network

# Volumes
Volume name: mysql_data

# Ports
App: 8080:80
Database: 3307:3306
