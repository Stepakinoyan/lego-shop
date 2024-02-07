from fastapi import Depends, FastAPI
from fastapi.templating import Jinja2Templates
from app.database import User
from app.auth.schemas import UserCreate, UserRead
from app.lego.router import router as lego_router
from app.cart.router import router as cart_router
from fastapi.middleware.cors import CORSMiddleware
from app.auth.manager import auth_backend, current_active_user, fastapi_users


templates = Jinja2Templates("app/templates")
app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8000",
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

@app.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.id}!"}
