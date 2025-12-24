================= PROJECT TREE =================

.gitignore
README.md
app/ [subfolders: 3, files: 4, total files: 17]
    Dockerfile
    __init__.py
    data/ [subfolders: 0, files: 2, total files: 2]
        __init__.py
        db_use.py
    main.py
    requirements.txt
    routers/ [subfolders: 1, files: 4, total files: 10]
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
        utils.py
    sql/ [subfolders: 0, files: 1, total files: 1]
        init.sql
docker-compose.yml
docs/ [subfolders: 0, files: 7, total files: 7]
    arcs.md
    docker_commands.md
    docker_compose.md
    flow.md
    project_overview.py
    test.py
    text.txt
instruction.md

⫘⫶⫘⫶⫘⫶⫘⫶⫘⫶⫘⫶⫘⫶⫘⫶⫘⫶⫘⫶⫘⫶⫘⫶⫘⫶

env_file 
DB_NAME=contacts_db
ROOT_PASS=pass

⫘⫶⫘⫶⫘⫶⫘⫶⫘⫶⫘⫶⫘⫶⫘⫶⫘⫶⫘⫶⫘⫶⫘⫶⫘⫶

dockercompose
start at this point only db and backend is local 

version: "3.8"

services:
  # -------------------- FastAPI Backend --------------------
  # app:
  #   build: ./app
  #   container_name: backend_api
  #   restart: unless-stopped
  #   ports:
  #     - "8080:80"
  #   env_file:
  #     - .env
  #   depends_on:
  #     database:
  #       condition: service_healthy
  #   networks:
  #     - app-network

  # -------------------- MySQL Database --------------------
  # db only docker compose up -d database
  database:
    image: mysql:8
    container_name: mysql_db
    restart: unless-stopped
    environment:
      MYSQL_ROOT_PASSWORD: ${ROOT_PASS}
      MYSQL_DATABASE: ${DB_NAME}
    ports:
      - "3307:3306"
    volumes:
      - mysql_data:/var/lib/mysql
      - ./app/sql/init.sql:/docker-entrypoint-initdb.d/init.sql:ro
    networks:
      - app-network

# -------------------- Networks --------------------
networks:
  app-network:
    driver: bridge

# -------------------- Volumes --------------------
volumes:
  mysql_data:
