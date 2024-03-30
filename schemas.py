from pydantic import BaseModel, validator
from typing import Union


class ErrorTypeModel(BaseModel):
    type: str

    # @validator('type')
    # def validate(self, v):
    #     return v in ['not_found']


class Resp404Body(BaseModel):
    errors: list[ErrorTypeModel]
    request_id: str

v = Resp404Body(
    errors=[ErrorTypeModel(type='not_found')],
    request_id='123',
)

print(v.dict())

s = Resp404Body.parse_obj({'errors': [{'type': 'not_found'}, {'type': 'found'}], 'request_id': '123'})

print(s)
