from fastapi import FastAPI
from app.routes.landpage_api import router
#venkat reddy

app= FastAPI()
#app.include_router(router)
app.include_router(
    router
)
#venakt
#k