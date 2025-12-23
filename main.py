from fastapi import FastAPI
from routers import input, view, utils

app = FastAPI(title="Supermarket API")

# -------------------- Routers --------------------
app.include_router(utils.router)
app.include_router(input.router)
app.include_router(view.router)


if __name__ == "__main__":
    print("Run the program here!")
