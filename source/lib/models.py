from pydantic import BaseModel
from typing import Optional

class Equipment(BaseModel):
    serial_number: Optional[str]
    equipment_name: Optional[str]
    equipment_type: Optional[str]
    prev_date: Optional[str]
    next_date: Optional[str]
    ser_link: Optional[str]
    equipment_owner: Optional[str]
    equipment_location: Optional[str]
    equipment_departure: Optional[str]
    equipment_sign: Optional[str]