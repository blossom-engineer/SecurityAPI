from fastapi import APIRouter
from starlette import status
from starlette.responses import Response

from src.schemas.BaseSchema import res_base
from src.schemas.IPASchemas import ipa_list_res

router = APIRouter(
	prefix='/IPA',
	tags=['IPA']
)

@router.get(
	'/IPA_List',
	response_model=ipa_list_res
)
def sec_list_get():
	return
