from fastapi import Request
from pydantic import ValidationError
from starlette.responses import JSONResponse, Response
from starlette.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
)

DEFAULT_ERROR_MESSAGE = "An error occurred"


class BaseException(Exception):
    pass


class AccessDenied(BaseException):
    pass


class AuthFailure(BaseException):
    pass


class NotFound(BaseException):
    pass


_EXCEPTION_STATUS_CODE_MAP = {
    AuthFailure: HTTP_401_UNAUTHORIZED,
    AccessDenied: HTTP_403_FORBIDDEN,
    NotFound: HTTP_404_NOT_FOUND,
}


def _get_exception_status_code(exc):
    for cls, status_code in _EXCEPTION_STATUS_CODE_MAP.items():
        if isinstance(exc, cls):
            return status_code

    return HTTP_400_BAD_REQUEST


async def default_exception_handler(request: Request, exc: Exception) -> Response:
    content = {"code": exc.__class__.__name__, "description": getattr(exc, "msg", str(exc)) or DEFAULT_ERROR_MESSAGE}

    if isinstance(exc, ValidationError):
        content["detail"] = exc.json()

    return JSONResponse(status_code=_get_exception_status_code(exc), content=content)
