from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


def create_app(storage):
    app = FastAPI()

    BASE_DIR = Path(__file__).resolve().parent

    app.mount(
        "/static",
        StaticFiles(directory=str(BASE_DIR / "web" / "static")),
        name="static"
    )

    templates = Jinja2Templates(
        directory=str(BASE_DIR / "web" / "templates")
    )

    @app.get("/")
    def index(request: Request):
        return templates.TemplateResponse(
            request,
            "index.html",
            {
                "pages": storage.get_pages()
            }
        )

    @app.get("/{page}")
    def page_view(request: Request, page: str):
        logs = storage.get_logs(page)

        return templates.TemplateResponse(
            request,
            "page.html",
            {
                "page": page,
                "logs": logs
            }
        )

    return app