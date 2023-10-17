from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from logic.patronBuilder.microservice import * 

from router import despacho,pago, SSO
# Initializing the FastAPI app

app = FastAPI()
app.title = "Public Transport Agency"
app.include_router(despacho.router)
app.include_router(pago.router)
app.include_router(SSO.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=['home'])
async def router():
    return {'hello': 'world'}

