from fastapi import APIRouter, HTTPException

from services.user import *
from logic.patronBuilder.microservice import * 
from models.models import PagoIn


# Initializing the FastAPI router
router = APIRouter(tags=['Pago'])


data_storage_pago = []

@router.post('/pago/')
def create_pago(pagoIn: PagoIn,
                user: User = Depends(get_current_active_user)):
    builder = PagoBuilder()
    builder._Pago = Pago(rules = pagoIn.rules, schedules= pagoIn.schedules, routes = pagoIn.routes)
    pago = builder.getMicroservice() 
    data_storage_pago.append(pago)
    return {'pago': data_storage_pago}

@router.get('/pagos/')
def show_pago():
    return data_storage_pago

@router.get('/pago/{pago_id}')
def read_pago(pago_id: int,
              user: User = Depends(get_current_active_user)):
    try:
        pago = data_storage_pago[pago_id]
    except IndexError:
        raise HTTPException(status_code= 404, 
                            detail = 'Pago no encontrado')
    return pago

@router.put('/pago/{pago_id}')
def update_pago(pago_id: int, 
                    pago_in: PagoIn,
                    user: User = Depends(get_current_active_user)):
    try: 
        builder = PagoBuilder()
        builder._Pago = Pago(rules = pago_in.rules, schedules= pago_in.schedules, routes = pago_in.routes)
        pago = builder.getMicroservice()
        data_storage_pago[pago_id] = pago
    except IndexError:
        raise HTTPException(status_code= 404, 
                            detail = 'Pago no encontrado')
    return pago


@router.delete('/pago/{pago_id}')
def delete_pago(pago_id: int,
                user: User = Depends(get_current_active_user)):
    try:
        del data_storage_pago[pago_id]
    except IndexError:
        raise HTTPException(status_code= 404, 
                            detail= 'Pago no encontrado')
    return data_storage_pago