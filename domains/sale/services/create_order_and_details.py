from domains.inventory.models.product_model import ProductModel
from domains.sale.models.order_model import OrderModel
from domains.sale.schemas.order_schema import CreateOrderRequestSchema, OrderResponseSchema
from domains.sale.schemas.order_detail_schema import CreateOrderDetailRequestSchema
from domains.sale.models.order_detail_model import OrderDetailModel
from sqlalchemy.orm import Session
import uuid
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

def create_order_and_details(order_request: CreateOrderRequestSchema, db: Session) -> dict:
    # create a new order
    order_dict = order_request.dict()
    order_dict['order_id'] = str(uuid.uuid4())
    order_dict['total_amount'] = 0  # initialize total_amount with 0
    order = OrderModel(**order_dict)
    db.add(order)

    # create order details and update total_amount in order
    for detail in order_request.order_details:
        product = db.query(ProductModel).filter(ProductModel.product_name == detail.product_name).first()
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")

        order_detail_dict = detail.dict()
        order_detail_dict['order_detail_id'] = str(uuid.uuid4())
        order_detail_dict['order_id'] = order.order_id
        order_detail_dict['product_id'] = product.product_id
        order_detail_dict['price_per_unit'] = product.unit_price
        order_detail_dict['total_amount_per_product'] = product.unit_price * detail.quantity

        order_detail = OrderDetailModel(**order_detail_dict)
        db.add(order_detail)

        order.total_amount += order_detail.total_amount_per_product  # increase total_amount in Order

    try:
        db.commit()
        db.refresh(order)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error occurred during creation of Order and OrderDetails.")

    return OrderResponseSchema.from_orm(order)
