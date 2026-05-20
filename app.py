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
    hospedes_consult = consulta_hospedes()

    return templates.TemplateResponse(
        request = request,
        name = "hospedes.html",
        context={
            "hospedes": hospedes_consult
        }
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

@app.get("/quartos", response_class=HTMLResponse)
async def list_quartos(request: Request):
    quartos_consult = consulta_quartos()

    return templates.TemplateResponse(
        request = request,
        name = "quartos.html",
        context={
            "quartos": quartos_consult
        }
    )

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
    update_quarto(id, numero, tipo, valor_diaria, status)
    return RedirectResponse(url="/quartos", status_code=303)

@app.get("/delete_quarto/{id}")
async def deletar_quarto(id:int):
    deletar_quarto(id)
    return RedirectResponse(url="/quartos", status_code=303)

# ────────────
# RESERVAS
# ────────────


@app.get("/reservas", response_class=HTMLResponse)
async def listar_reservas(request: Request):
    reservas = consulta_reservas_ativas()

    return templates.TemplateResponse(
        request=request,
        name="reservas.html",
        context={"reservas": reservas}
    )

@app.get("/reserva/{id}", response_class=HTMLResponse)
async def visualizar_reserva(request: Request, id: int):
    reserva = consulta_reserva_id(id)

    return templates.TemplateResponse(
        request=request,
        name="reserva_detalhe.html",
        context={"reserva": reserva}
    )

@app.get("/add_reserva", response_class=HTMLResponse)
async def pagina_add_reserva(request: Request):
    hospedes = consulta_hospedes()
    quartos = consulta_quartos()

    return templates.TemplateResponse(
        request=request,
        name="add_reserva.html",
        context={
            "hospedes": hospedes,
            "quartos": quartos
        }
    )

@app.get("/edit_reserva/{id}", response_class=HTMLResponse)
async def pagina_edit_reserva(request: Request, id: int):
    reserva = consulta_reserva_id(id)
    hospedes = consulta_hospedes()
    quartos = consulta_quartos()

    return templates.TemplateResponse(
        request=request,
        name="edit_reserva.html",
        context={
            "reserva": reserva,
            "hospedes": hospedes,
            "quartos": quartos
        }
    )

@app.post("/edit_reserva/{id}")
async def editar_reserva(
    id: int,
    hospede_id: int = Form(...),
    quarto_id: int = Form(...),
    data_entrada: str = Form(...),
    data_saida: str = Form(...)
):
    update_reserva(id, hospede_id, quarto_id, data_entrada, data_saida)
    return RedirectResponse(url="/reservas", status_code=303)


@app.get("/delete_reserva/{id}")
async def deletar_reserva(id: int):
    delete_reserva(id)
    return RedirectResponse(url="/reservas", status_code=303)

@app.post("/add_reserva")
async def adicionar_reserva(
    hospede_id: int = Form(...),
    quarto_id: int = Form(...),
    data_entrada: str = Form(...),
    data_saida: str = Form(...)
):
    add_reserva(hospede_id, quarto_id, data_entrada, data_saida)
    return RedirectResponse(url="/reservas", status_code=303)