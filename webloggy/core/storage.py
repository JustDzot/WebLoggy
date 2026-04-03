from collections import defaultdict
from .models import Log


class Storage:
    def __init__(self):
        self.logs = []
        self.pages = defaultdict(list)

    def add_log(self, log: Log):
        self.logs.append(log)
        self.pages[log.page].append(log)

    def get_pages(self):
        return list(self.pages.keys())

    def get_logs(self, page: str):
        return self.pages.get(page, [])