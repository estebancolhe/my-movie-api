from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse

class ErrorHandler(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI) -> None:
        super().__init__(app)

    # metodo asincrono para detectar errores
    async def dispatch(self, request: Request, call_next) -> Response or JSONResponse:
        # next_call, si no hay errores entonces pasa a entrgar la respuesta en un Json gracias a
        # JSONResponse
        try:
            # si no hay error entra por aca
            return await call_next(request)
        except Exception as e:
            # si hay error, entra por aca y retorna el error
            return JSONResponse(status_code=500, content = {'error': str(e)})