import time
from urllib import response

from typing import Optional
import base64
from passlib.context import CryptContext
from datetime import datetime, timedelta

import jwt
from jwt import PyJWTError

from pydantic import BaseModel

from fastapi import Depends, FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm, OAuth2
from fastapi.security.base import SecurityBase
from fastapi.security.utils import get_authorization_scheme_param
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi.openapi.utils import get_openapi

from starlette.status import HTTP_403_FORBIDDEN
from starlette.responses import RedirectResponse, Response, JSONResponse
from starlette.requests import Request

from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware

from routers import auth, user

app = FastAPI()

@app.get("/items/")

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process time"] = str(process_time)
    return response

