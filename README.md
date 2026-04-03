![Python](https://img.shields.io/badge/python-3.8+-blue)
![License](https://img.shields.io/badge/license-MIT-green)

# WebLoggy 🚀

Lightweight debugging web tool for Python

WebLoggy turns your logs into a live web interface — instantly.

No setup. Just debug.

---

## ✨ Features

* 📄 Pages-based logging
* 🌐 Built-in web UI
* 🧩 Structured logs (with context)
* 🔗 Trace support
* 🔍 Search
* 💬 Telegram / Discord (optional)

---

## 🚀 Quick Start

```bash
pip install webloggy
```

```python
from webloggy import Logger

logger = Logger()

auth = logger.page("auth")

auth.info("user logged in")
auth.error("user not found", user_id=123)
```

Open:
http://localhost:8000

---

## 🔗 Trace

```python
with logger.trace("req_1"):
    auth.info("start")
    auth.error("fail")
```

---

## 🧠 Philosophy

Simple. Local. Fast debugging.

---

## 📄 License

MIT
