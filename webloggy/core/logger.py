import threading
from contextlib import contextmanager

import uvicorn

from .storage import Storage
from .page import Page
from ..server import create_app


class Logger:
    def __init__(self, host="127.0.0.1", port=8000):
        self.host = host
        self.port = port

        self.storage = Storage()
        self._current_trace = None
        self._started = False

    def page(self, name):
        return Page(name, self.storage, self._get_trace, self._ensure_started)

    def _get_trace(self):
        return self._current_trace

    def _ensure_started(self):
        if not self._started:
            self._start_server()

    def _start_server(self):
        app = create_app(self.storage)

        thread = threading.Thread(
            target=uvicorn.run,
            args=(app,),
            kwargs={"host": self.host, "port": self.port},
            daemon=True
        )
        thread.start()

        self._started = True
        print(f"🚀 WebLoggy running at http://{self.host}:{self.port}")

    @contextmanager
    def trace(self, trace_id):
        self._current_trace = trace_id
        try:
            yield
        finally:
            self._current_trace = None

    def error(self, message, page="default", **context):
        self.page(page).error(message, **context)