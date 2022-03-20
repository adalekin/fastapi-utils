from fastapi import Header

from fastapi_utils import jwt


class AccessDenied(Exception):
    pass


def ensure_current_user(x_jwt_payload: str = Header(...)):
    payload = jwt.decode_payload(x_jwt_payload)

    if not payload:
        raise AccessDenied("Access denied")

    return payload


def ensure_current_superuser(x_jwt_payload: str = Header(...)):
    payload = ensure_current_user(x_jwt_payload)

    if not payload.get("is_superuser"):
        raise AccessDenied("Access denied")

    return payload
