from typing import List, Optional
from fastapi import APIRouter, Header, Response, Cookie, Form
from fastapi.responses import HTMLResponse, PlainTextResponse


router = APIRouter(
    prefix='/product',
    tags=['product']
)

products = [
    "watch",
    "camera",
    "phone"
]

@router.get('/all')
def get_all_products():
    # return product
    data = " ".join(products)
    return Response(content=data, media_type="text/plain")


@router.post('/new')
def create_product(name: str = Form(...)):
    products.append(name)
    return products


# Cookie endpoint
@router.get('/with-cookie')
def get_cookie():
    data = " ".join(products)
    response = Response(content=data, media_type="text/plain")
    response.set_cookie(key="test_cookie", value="test_cookie_value")
    return response


@router.get('/with-header')
def get_products(response: Response,
                 custom_header: Optional[str] = Header(None),
                 Authorization: Optional[str] = Header(None),
                 test_cookie: Optional[str] = Cookie(None)):
    print(custom_header)
    print(Authorization)
    response.headers['Custom-Response-Header'] = "NewToken asdhgasdhgasfdhgasd"
    products.append("Token xfga65asd65asd65asd")
    return {
        'data': products,
        'custom_header': custom_header,
        'cookie': test_cookie
    }


@router.get('/{id}')
def get_product(id: int):
    if id > len(products) - 1:
        return PlainTextResponse(status_code=404,
            content="Product not found", media_type="text/plain"
        )
    else:
        product = products[id]
        out = f"""
        <head>
            <style>
            .product {{
                width: 500px;
                height: 30px;
                border: 2px inset green;
                background-color: lightblue;
                text-align: center;
            }}
            </style>

        </head>
        <div class='product'> {product}
        </div>
        """
        return HTMLResponse(content=out, media_type='text/html')


