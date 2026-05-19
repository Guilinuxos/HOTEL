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

# ────────────
# HOSPEDES
# ────────────
@app.get("/hospedes", response_class=HTMLResponse)
async def list_hospedes(request: Request):
    hospedes = consulta_hospedes()

    return templates.TemplateResponse(
        request = request,
        name = "hospedes.html",
        context={}
    )

@app.get("/add_hospede", response_class=HTMLResponse)
async def pagina_add_hospede(request: Request):
    return templates.TemplateResponse(
        request=request,
        name = "add_hospede.html",
        context={}
    )


@app.post("/add_hospede")
async def adicionar_hospede(
    nome: str = Form(...),
    email: str = Form(None),
    telefone: str = Form(None),
    cpf: str = Form(None)
):
    add_hospede(nome, email, telefone, cpf)
    return RedirectResponse(url="/hospedes", status_code=303)


@app.get("/edit_hospede/{id}", response_class=HTMLResponse)
async def pagina_edit_hospede(request: Request, id: int):
    hospede = consulta_hospede_id(id)

    return templates.TemplateResponse(
        request = request,
        name = "edit_hospede.html",
        context = {"hospede": hospede}
    )


@app.post("/edit_hospede/{id}")
async def editar_hospede(
    id: int,
    nome: str = Form(...),
    email: str = Form(None),
    telefone: str = Form(None),
    cpf: str = Form(None)
):
    update_hospede(id, nome, email, telefone, cpf)
    return RedirectResponse(url="/hospedes", status_code=303)


@app.get("/delete_hospede/{id}")
async def deletar_hospede(id: int):
    delete_hospede(id)
    return RedirectResponse(url="/hospedes", status_code=303)

# ────────────
# QUARTOS
# ────────────

@app.get("/add_quarto", response_class=HTMLResponse)
async def add_quarto(request: Request):
     return templates.TemplateResponse(
        request=request,
        name="form_quarto.html",
        context={}
    )

@app.post("/add_quarto")
async def salvar_quarto(
    numero: str = Form(...),
    tipo: str = Form(...),
    valor_diaria: float = Form(...),
    status: str = Form(...)
):
    add_quarto(numero, tipo, valor_diaria, status)
    return RedirectResponse(url="/quartos", status_code=303)

@app.get("/edit_quarto/{id}", response_class=HTMLResponse)
async def edit_quarto(request:Request, id: int):
    quarto = consulta_quarto_id(id)

    return templates.TemplateResponse(
        request=request,
        name="form_quarto.html",
        context={"quarto": quarto}
    )
@app.post("/edit_quarto/{id}")
async def editar_quarto(
    id: int,
    numero: str = Form(...),
    tipo: str = Form(...),
    valor_diaria: float = Form(...),
    status: str = Form(...)
):
    udpate_quarto(id, numero, tipo, valor_diaria, status)
    return RedirectResponse(url="/quartos", status_code=303)

@app.get("/delete_quarto/{id}")
async def deletar_quarto(id:int):
    deletar_quarto(id)
    return RedirectResponse(url="/quartos", status_code=303)

# ────────────
# RESERVAS
# ────────────
