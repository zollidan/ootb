import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from art import tprint
from app.api.router import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print(15*'-' + ' LeFort ootb. ' + 15*'-')
    tprint('ootb.')
    yield
   
    
    

app = FastAPI(lifespan=lifespan)
app.include_router(router=router)
