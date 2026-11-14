from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlmodel import SQLModel

from app.core.database import engine

from app.modules.heroes.router import router as heroes_router
from app.modules.weapons.router import router as weapons_router

#importar modelos para registrarlos
from app.modules.teams.models import Team
from app.modules.heroes.models import Hero
from app.modules.weapons.models import Weapon

@asynccontextmanager
async def lifespan(app: FastAPI):    
    SQLModel.metadata.drop_all(engine) #Solo para pruebas! BORRAR AL FINALIZAR.
    SQLModel.metadata.create_all(engine)
    yield

app = FastAPI(lifespan=lifespan)    

app.include_router(heroes_router)
app.include_router(weapons_router)