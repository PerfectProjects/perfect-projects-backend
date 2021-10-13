from functools import wraps
from flask import g, request, redirect, url_for


def require_authentication(f):
    @wraps(f)
    def is_signed_in(*args, **kwargs):
        print(request.headers.get("refreshToken"))

        return f(*args, **kwargs)
    return is_signed_in
