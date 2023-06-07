from fastapi import APIRouter, Depends, HTTPException
from domains.sale.controllers.order_controller import router as order_controller
from domains.sale.controllers.order_detail_controller import router as order_detail_controller

router = APIRouter(tags=['Sale'])
router.include_router(order_controller, prefix='/order')
router.include_router(order_detail_controller, prefix='/order_detail')
