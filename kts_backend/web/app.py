from typing import Sequence, Callable

from aiohttp.web import (
    Application as AiohttpApplication,
    View as AiohttpView,
    Request as AiohttpRequest,
)
from pyparsing import Optional


from kts_backend import __appname__, __version__
from .urls import register_urls
from kts_backend.store import setup_store, Store


class Application(AiohttpApplication):
    config = None
    store = None
    database = None

app = Application()


def setup_app(config_path: str) -> Application:
    setup_config(app, config_path)
    setup_store(app)
    return app
