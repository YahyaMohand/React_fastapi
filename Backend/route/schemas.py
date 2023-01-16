from datetime import datetime
from typing import List
from pydantic import BaseModel


class PostBase(BaseModel):
    image_url : str
    title : str
    content : str
    creator : str

class PostDisplay(BaseModel):
    id : int
    image_url : str
    title : str
    content : str
    creator : str
    timestamp : datetime
    class Config():
      orm_mode = True