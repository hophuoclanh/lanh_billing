from fastapi import APIRouter, Depends, HTTPException
from domains.sale.controllers.order_controller import router as order_controller
from domains.sale.controllers.order_detail_controller import router as order_detail_controller
from domains.sale.schemas.order_schema import OrderResponseSchema, CreateOrderRequestSchema
from sqlalchemy.orm import Session
from repository import get_db
from domains.authentication.models.user_model import UserModel
from dependencies.get_current_user import get_current_user
from domains.sale.services.create_order_and_details import create_order_and_details


router = APIRouter(tags=['Sale'])
router.include_router(order_controller, prefix='/order')
router.include_router(order_detail_controller, prefix='/order_detail')

@router.post("/", response_model=OrderResponseSchema)
def create_super_order(
    order: CreateOrderRequestSchema,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    if not current_user.has_permission(db, 'create', 'order'):
        raise HTTPException(status_code=403, detail="User does not have permission to create an order")
    return create_order_and_details (order_request=order, db=db)
