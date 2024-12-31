from typing import Optional
from pydantic import BaseModel, Field

from src.schemas.BaseSchema import res_base

class ipa_item(BaseModel):
	title: str = Field(
		default='',
		description='セキュリティ記事のタイトル'
	)
	content: str = Field(
		default='',
		description='セキュリティ記事の本文'
	)

class ipa_list(BaseModel):
	ipa_list: list[ipa_item]

class ipa_list_res(res_base):
	result: ipa_list
