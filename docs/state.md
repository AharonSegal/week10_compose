================= PROJECT TREE =================

.gitignore
README.md
app/ [subfolders: 3, files: 4, total files: 16]
    Dockerfile
    __init__.py
    data/ [subfolders: 0, files: 2, total files: 2]
        __init__.py
        db_use.py
    main.py
    requirements.txt
    routers/ [subfolders: 1, files: 3, total files: 9]
        __init__.py
        __pycache__/ [subfolders: 0, files: 6, total files: 6]
            input.cpython-311.pyc
            input.cpython-314.pyc
            utils.cpython-311.pyc
            utils.cpython-314.pyc
            view.cpython-311.pyc
            view.cpython-314.pyc
        contacts.py
        db_test.py
    sql/ [subfolders: 0, files: 1, total files: 1]
        init.sql
docker-compose.yml
docs/ [subfolders: 0, files: 8, total files: 8]
    Commands.md
    arcs.md
    docker_commands.md
    docker_compose.md
    flow.md
    project_overview.py
    sql_curtos.md
    text.txt
instruction.md
state.md
test.py

================= PROJECT STATS =================


⫘⫶⫘⫶⫘⫶⫘⫶⫘⫶⫘⫶⫘⫶⫘⫶⫘⫶⫘⫶⫘⫶⫘⫶⫘⫶

DB_USER=root
ROOT_PASS=pass
DB_NAME=contacts_db

⫘⫶⫘⫶⫘⫶⫘⫶⫘⫶⫘⫶⫘⫶⫘⫶⫘⫶⫘⫶⫘⫶⫘⫶⫘⫶
version: "3.8"

services:
  # -------------------- MySQL Database --------------------
  db:
    image: mysql:8
    container_name: mysql_db
    restart: unless-stopped
    environment:
      MYSQL_ROOT_PASSWORD: ${ROOT_PASS}   
      MYSQL_DATABASE: ${DB_NAME}          
    ports:
      - "3307:3306"                
    volumes:
      - db_data:/var/lib/mysql
      - ./sql/init.sql:/docker-entrypoint-initdb.d/init.sql:ro
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost", "-p${ROOT_PASS}"]
      interval: 5s
      timeout: 5s
      retries: 10
      start_period: 20s
    networks:
      - app-network

  # -------------------- FastAPI Backend --------------------
  api:
    build: ./app
    container_name: contacts_api
    restart: unless-stopped
    environment:
      ROOT_PASS: ${ROOT_PASS}       
      DB_NAME: ${DB_NAME}
      API_PORT: ${API_PORT}         
    depends_on:
      db:
        condition: service_healthy
    ports:
      - "8080:80"                   
    networks:
      - app-network

# -------------------- Networks --------------------
networks:
  app-network:
    driver: bridge

# -------------------- Volumes --------------------
volumes:
  db_data: