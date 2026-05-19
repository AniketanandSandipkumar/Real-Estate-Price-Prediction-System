from pydantic import BaseModel


class PropertyInput(BaseModel):

    area: float
    bedrooms: int
    bathrooms: int
    age: int
    location: str
    property_type: str
