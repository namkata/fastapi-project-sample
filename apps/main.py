from fastapi import FastAPI, Request, Response

from apps.sql_app import models
from apps.database import engine, SessionLocal
from apps.sql_app.router import router as sql_app_router
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI example",
    description="This is fastapi template for development to learn knowledge basic about fastapi framework",
    version="0.1.0",
    docs_url="/",
    redoc_url="/re-doc/",
    openapi_url='/api/v1/openapi.json',
    swagger_ui_parameters={"defaultModelsExpandDepth": -1}  # Hide schemas in docs
    # openapi_tags='api',
    # openapi_prefix='/api/v1/',

)

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    # allow_methods=["*"],
    allow_methods=("GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"),
    allow_headers=["*"],
)


# @app.middleware("http")
# @app.middleware("https")
# async def db_session_middleware(request: Request, call_next):
#     response = Response("Internal server error", status_code=500)
#     try:
#         request.state.db = SessionLocal()
#         response = await call_next(request)
#     finally:
#         request.state.db.close()
#     return response


# Router
app.include_router(sql_app_router, prefix="", tags=["Auth"])
