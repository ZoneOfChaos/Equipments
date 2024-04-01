from pydantic import BaseModel

class Equipment(BaseModel):
    serial_number: str
    equipment_name: str
    equipment_type: str
    prev_date: str
    next_date: str
    ser_link: str
    equipment_owner: str
    equipment_location: str
    equipment_departure: str
    equipment_sign: str