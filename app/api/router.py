from fastapi import APIRouter

router = APIRouter(prefix='/api')


@router.get('/')
def api_home():
    return {"message":"This is api of ootb."}

@router.get('/products')
def products_list():
    return {'products': [
        "1", "2", "3"
    ]}