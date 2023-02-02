import logging
import os

from fastapi import FastAPI
from apps.sql_app import models
from apps.database import engine
from apps.sql_app.router import router as sql_app_router
from fastapi.middleware.cors import CORSMiddleware
from apps.config import settings, logging_conf
from logging.config import dictConfig

models.Base.metadata.create_all(bind=engine)
dictConfig(logging_conf)

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
#     """Startup application."""
#     db_url = os.getenv("PG_DNS")
#
#     if not db_url.__contains__("sqlite"):
#         Base.metadata.drop_all(bind=engine)
#         Base.metadata.create_all(bind=engine)
#
#     database = app.state.database
#     if not database.i