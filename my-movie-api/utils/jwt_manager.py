from jwt import encode, decode

def create_token(data: dict): # data -> diccionario que voy a convertir al token
    token: str = encode(payload=data, key="my_secret_key", algorithm="HS256") # payload -> contenido
    # que voy a convertir al token, en este caso es la data, 
    # key -> string con la clave para generar el token
    # para descifrar el token debo enviar la clave que hay en 'key'
    # algorithm -> algoritmo utilizado para generar el token.
    return token

def validate_token(token: str) -> dict: # recibe el token en un string y retorna un diccionario
    data: dict = decode(token, key="my_secret_key", algorithms=['HS256']) # recibe el token, la contraseña
    # y una lista de algoritmos para descifrar el token
    return data