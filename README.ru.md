![Python](https://img.shields.io/badge/python-3.8+-blue)
![License](https://img.shields.io/badge/license-MIT-green)

# WebLoggy 🚀

Лёгкий debugging web tool для Python

WebLoggy превращает логи в удобный веб-интерфейс — сразу после запуска.

Без настройки. Просто дебаг.

---

## ✨ Возможности

* 📄 Логи по страницам
* 🌐 Встроенный веб-интерфейс
* 🧩 Context
* 🔗 Trace
* 🔍 Поиск
* 💬 Telegram / Discord (опционально)

---

## 🚀 Быстрый старт

```bash
pip install webloggy
```

```python
from webloggy import Logger

logger = Logger()

auth = logger.page("auth")

auth.info("пользователь вошёл")
auth.error("пользователь не найден", user_id=123)
```

Открой:
http://localhost:8000

---

## 🔗 Trace

```python
with logger.trace("req_1"):
    auth.info("старт")
    auth.error("ошибка")
```

---

## 🧠 Идея

Просто. Локально. Быстро.

---

## 📄 Лицензия

MIT
