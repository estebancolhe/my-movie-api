from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException
from utils.jwt_manager import create_token, validate_token


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request): # funcion requerida para acceder la peticion del usuario
        # con 'request' ya tengo acceso a la peticion del usuario
        auth = await super().__call__(request) # con 'super().__call__(request)' llamamos a la funcion
        # __call__() de 'HTTPBearer' que es la que nos retorna el token
        # como esa consulta toma un tiempo se utiliza el 'await' y se convierte en una funcion
        # asincrona con el 'async'
        data = validate_token(auth.credentials)
        if data['email'] != "admin@gmail.com":
            raise HTTPException(status_code=403, detail="Credenciales invalidas")