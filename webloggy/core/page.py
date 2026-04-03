from .models import Log


class Page:
    def __init__(self, name, storage, trace_provider, ensure_started):
        self.name = name
        self.storage = storage
        self.trace_provider = trace_provider
        self.ensure_started = ensure_started

    def _log(self, level, message, **context):
        self.ensure_started()

        log = Log(
            page=self.name,
            level=level,
            message=message,
            context=context or None,
            trace_id=self.trace_provider()
        )

        self.storage.add_log(log)

    def info(self, message, **context):
        self._log("info", message, **context)

    def warning(self, message, **context):
        self._log("warning", message, **context)

    def error(self, message, **context):
        self._log("error", message, **context)