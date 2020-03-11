from pydantic import BaseModel, Schema


class Order(BaseModel):
    owner_id: str = Schema(..., max_length=40)
    order_id: str = Schema(..., max_length=40)
    order_name: str = Schema(..., max_length=100)
    description: str = Schema(..., max_length=200)
    thumb_url: str = Schema(..., max_length=200)

