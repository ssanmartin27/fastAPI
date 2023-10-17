from fastapi import APIRouter, HTTPException, Depends

from services.user import *
from logic.patronBuilder.microservice import * 
from models.models import DespachoIn
from pydantic import BaseModel
from typing import Annotated


# Initializing the FastAPI router
router = APIRouter(tags=['Despacho'])


data_storage_despacho = []

@router.post('/despacho/')
async def create_despacho(despachoIn: DespachoIn, user: User = Depends(get_current_active_user)):
    builder = DespachoBuilder()
    builder._despacho = Despacho(rules=despachoIn.rules, schedules=despachoIn.schedules, routes=despachoIn.routes)
    despacho = builder.getMicroservice()
    data_storage_despacho.append(despacho)
    return {'despacho': data_storage_despacho}

@router.get('/despachos/')
async def show_despacho():
    return data_storage_despacho

@router.get('/despacho/{despacho_id}')
async def read_despacho(despacho_id: int, user: User = Depends(get_current_active_user)):
    try:
        despacho = data_storage_despacho[despacho_id]
    except IndexError:
        raise HTTPException(status_code= 404, 
                            detail = 'Despacho no encontrado')
    return despacho

@router.put('/despacho/{despacho_id}')
async def update_despacho(despacho_id: int, 
                    despacho_in: DespachoIn,
                    user: User = Depends(get_current_active_user)):
    try: 
        builder = DespachoBuilder()
        builder._despacho = Despacho(rules = despacho_in.rules, schedules= despacho_in.schedules, routes = despacho_in.routes)
        despacho = builder.getMicroservice()
        data_storage_despacho[despacho_id] = despacho
    except IndexError:
        raise HTTPException(status_code= 404, 
                            detail = 'Despacho no encontrado')
    return despacho


@router.delete('/despacho/{despacho_id}')
async def delete_despacho(despacho_id: int,
                          user: User = Depends(get_current_active_user)):
    try:
        del data_storage_despacho[despacho_id]
    except IndexError:
        raise HTTPException(status_code= 404, 
                            detail= 'Despacho no encontrado')
    return data_storage_despacho