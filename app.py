from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from model import *

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# ────────────
# DASHBOARD
# ────────────

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    hospedes = consulta_hospedes()
    quartos = consulta_quartos()
    reservas = consulta_reservas_ativas()  # já filtradas como ativas no SQL

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "total_hospedes": len(hospedes),
            "total_quartos": len(quartos),
            "total_reservas": len(reservas)
        }
    )