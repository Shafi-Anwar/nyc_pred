from pydantic import BaseModel


class TaxiInput(BaseModel):
    vendor_id: int
    passenger_count: int

    pickup_longitude: float
    pickup_latitude: float

    dropoff_longitude: float
    dropoff_latitude: float

    pickup_hour: int
    pickup_day: int
    pickup_weekday: int
    pickup_month: int

    store_and_fwd_flag: str