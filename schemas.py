from pydantic import BaseModel, Field, validator
from datetime import date
from typing import Optional

class ProductSchema(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0, lt=500)          # >0 and <500
    weight: float = Field(..., gt=0)                 # >0
    sale_percentage: int = Field(0, ge=0, le=100)   # 0–100
    creation_date: date
    expiration_date: date
    is_on_sale: bool = False

    # -------------------- Validators --------------------

    #---used inline instead---

    # @validator('price')
    # def price_positive_and_reasonable(cls, v):
    #     if v <= 0:
    #         raise ValueError('Price must be positive')
    #     if v > 500:
    #         raise ValueError('Price unusually high, check input')  # catches likely decimal errors
    #     return v

    # @validator('weight')
    # def weight_positive(cls, v):
    #     if v <= 0:
    #         raise ValueError('Weight must be positive')
    #     return v

    # @validator('sale_percentage')
    # def sale_percentage_valid(cls, v):
    #     if v < 0 or v > 100:
    #         raise ValueError('Sale percentage must be between 0 and 100')
    #     return v

    @validator('expiration_date')
    def expiration_after_creation(cls, v, values):
        if 'creation_date' in values and v <= values['creation_date']:
            raise ValueError('Expiration date must be after creation date')
        return v

    class Config:
        from_attributes = True



# -------------------- Subclasses --------------------

class DrinkSchema(ProductSchema):
    volume_ml: int = Field(..., gt=0)  
    is_carbonated: bool = False

    # @validator('volume_ml')
    # def volume_positive(cls, v):
    #     if v <= 0:
    #         raise ValueError('Volume must be positive')
    #     return v


class DairySchema(ProductSchema):
    fat_content: float  = Field(..., gt=0, lt=100) 

    # @validator('fat_content')
    # def fat_valid(cls, v):
    #     if not (0 <= v <= 100):
    #         raise ValueError('Fat content must be between 0 and 100')
    #     return v


class CannedSchema(ProductSchema):
    easy_open: bool = False


# -------------------- Response Schema --------------------
class ProductResponse(ProductSchema):
    id: int
    barcode: str