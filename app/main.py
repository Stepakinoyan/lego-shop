from fastapi import Depends, FastAPI
from app.database import User
from app.auth.schemas import UserCreate, UserRead
from app.lego.router import router as lego_router
from app.cart.router import router as cart_router
from fastapi.middleware.cors import CORSMiddleware
from app.auth.manager import auth_backend, fastapi_users


app = FastAPI()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(lego_router)
app.include_router(cart_router)