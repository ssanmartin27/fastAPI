from fastapi import APIRouter, HTTPException

from services.user import *
from logic.patronBuilder.microservice import * 
from models.models import DespachoIn

# Initializing the FastAPI router
router = APIRouter(tags=['Despacho'])


data_storage_despacho = []

@router.post('/despacho/')
def create_despacho(despachoIn: DespachoIn = Depends(get_current_active_user)):
    builder = DespachoBuilder()
    builder._despacho = Despacho(rules = despachoIn.rules, schedules= despachoIn.schedules, routes = despachoIn.routes)
    despacho = builder.getMicroservice() 
    data_storage_despacho.append(despacho)
    return {'despacho': data_storage_despacho}

@router.get('/despachos/')
def show_despacho():
    return data_storage_despacho

@router.get('/despacho/{despacho_id}')
def read_despacho(despacho_id: int = Depends(get_current_active_user)):
    try:
        despacho = data_storage_despacho[despacho_id]
    except IndexError:
        raise HTTPException(status_code= 404, 
                            detail = 'Despacho no encontrado')
    return despacho

@router.put('/despacho/{despacho_id}')
def update_despacho(despacho_id: int = Depends(get_current_active_user), 
                    despacho_in: DespachoIn = Depends(get_current_active_user)):
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
def delete_despacho(despacho_id: int = Depends(get_current_active_user)):
    try:
        del data_storage_despacho[despacho_id]
    except IndexError:
        raise HTTPException(status_code= 404, 
                            detail= 'Despacho no encontrado')
    return data_storage_despacho