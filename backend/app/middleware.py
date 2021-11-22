from http import HTTPStatus
import logging

from fastapi import Response
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

from app.errors import *


logger = logging.getLogger(__name__)


class MapAppErrorToHTTPResponse(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)
        except (
            ErrorUnknownVariant,

        ) as e:
            status_code = HTTPStatus.UNPROCESSABLE_ENTITY
            message = str(e)

        logger.error(message)
        return Response(content=message, status_code=status_code)


def add_middlewares(app):
    """
    Add all middlewares
    """

    app.add_middleware(MapAppErrorToHTTPResponse)
