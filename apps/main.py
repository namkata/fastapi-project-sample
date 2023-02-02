import logging
from fastapi import FastAPI
from apps.sql_app import models
from apps.database import engine
from apps.sql_app.router import router as sql_app_router
from fastapi.middleware.cors import CORSMiddleware
from apps.config import settings, logging_conf
from logging.config import dictConfig
from apps.utils import check_db_connected

dictConfig(logging_conf)
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.project_title,
    description=settings.project_description,
    version=settings.project_version,
    docs_url="/",
    redoc_url="/re-doc/",
    openapi_url='/api/v1/openapi.json',
    swagger_ui_parameters={"defaultModelsExpandDepth": -1}  # Hide schemas in docs
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=settings.cors_methods,
    allow_headers=settings.cors_headers,
)
# Router
app.include_router(sql_app_router, prefix="", tags=["Auth"])


# @app.on_event("startup")
# async def startup_event():
#     await check_db_connected()

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
