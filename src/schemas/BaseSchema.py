import os
from pydantic import BaseModel, Field

class res_base(BaseModel):
	api_version: str = Field(default=os.getenv('API_VERSION'))
	result: BaseModel
