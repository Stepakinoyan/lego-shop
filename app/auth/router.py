from fastapi import APIRouter, Security, Response
from fastapi_jwt import JwtAuthorizationCredentials, JwtAccessBearer

router = APIRouter(prefix='/jwt', tags=["auth"])

access_security = JwtAccessBearer(secret_key="secret_key", auto_error=True)


@router.post("/auth")
def auth():
    subject = {"username": "username", "role": "user"}
    return {"access_token": access_security.create_access_token(subject=subject)}

@router.post("/auth_cookie")
def auth(response: Response):
    subject = {"username": "username", "role": "user"}
    access_token = access_security.create_access_token(subject=subject)
    access_security.set_access_cookie(response, access_token)
    return {"access_token": access_token}


@router.get("/users/me")
def read_current_user(
    credentials: JwtAuthorizationCredentials = Security(access_security),
):
    return {"username": credentials["username"], "role": credentials["role"]}