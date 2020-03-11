""" basic """
import asyncio
import logging
import sys
import os

""" hypercorn """
from hypercorn.config import Config
from hypercorn.asyncio import serve

""" fastapi """
from fastapi import FastAPI
from starlette.websockets import WebSocket
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import Response

""" custom routes """
from api import order_api, ws_api
from config.settings import GLOBAL_ORDER_API_PREFIX, PORT, PORT_HTTP2
from config.settings import keyfile, certfile


app = FastAPI(title="TrustArea Test Server",
              openapi_url=None,
              docs_url=None,
              redoc_url=None,
              swagger_ui_oauth2_redirect_url=None)

app.include_router(order_api.router, tags=['Orders'], prefix=GLOBAL_ORDER_API_PREFIX)
app.include_router(ws_api.router, tags=['WebSockets'])


app.add_middleware(
    CORSMiddleware,
    allow_origins=[f'https://localhost:{PORT}'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware('http')
async def db_session_middleware(request: Request, call_next):
    response = Response('Internal server error', status_code=500)
    try:
        # request.state.db = SessionLocal()
        response = await call_next(request)
    except Exception as e:
        raise e
    else:
        ...
    finally:
        ...
    return response


if __name__ == '__main__':

    log_formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(module)s %(message)s')
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(log_formatter)

    logging.basicConfig(level=logging.NOTSET, handlers=[console_handler])

    config = Config()
    config.bind = [f"0.0.0.0:{PORT}"]
    config.keyfile = keyfile
    config.certfile = certfile
    config.alpn_protocols = ["h2", "http/1.1"]

    asyncio.run(serve(app, config))
    # uvicorn.run(app, host='0.0.0.0', port=PORT)
