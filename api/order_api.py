import logging
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from api.data import Order
from typing import List
from passlib.context import CryptContext

from starlette.status import HTTP_403_FORBIDDEN


router = APIRouter()
security = HTTPBasic()
credentials_exception = HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials")


log = logging.getLogger(__name__)
log.info("Test Order API")


order1 = Order(**{
            "owner_id": "001",
            "order_id": "1001",
            "order_name": "Order 1",
            "description": "Description order 1",
            "thumb_url": "http://thumb1.com/1"
        })
order2 = Order(**{
            "owner_id": "002",
            "order_id": "1002",
            "order_name": "Order 2",
            "description": "Description order 2",
            "thumb_url": "http://thumb2.com/2"
        })


@router.get('/orders', response_model=List[Order])
async def orders() -> List[Order]:
    log.info(f'API: List /orders')
    return [order1, order2]

