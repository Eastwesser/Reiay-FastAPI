from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from api.i18n.i18n_helper import set_language


class LocaleMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        language = request.headers.get("Accept-Language", "en").split(",")[0]
        set_language(language)
        response = await call_next(request)
        return response
