
# 🏨 PROJETO HOTELARIA

## 📖 Descrição do Projeto

O Projeto Hotelaria é um sistema web desenvolvido com arquitetura MVC, utilizando:

- FastAPI
- Jinja2
- MySQL Connector

O sistema possui integração entre front-end e back-end, permitindo o gerenciamento completo das informações do hotel através de operações CRUD (Create, Read, Update e Delete).

### Funcionalidades do sistema:

- Cadastro de hóspedes
- Cadastro de quartos
- Cadastro de reservas
- Edição de informações
- Exclusão de registros
- Visualização de dados

---

# 💻 Tecnologias Utilizadas

- Python
- FastAPI
- Uvicorn
- Jinja2
- MySQL
- MySQL Connector
- HTML5
- CSS3

---

# ⚙️ Instruções de Instalação

## 📌 Pré-requisitos

Antes de iniciar o projeto, é necessário possuir instalado:

- Python
- XAMPP
- MySQL Workbench
- VS Code

---

## 🐍 Criação do Ambiente Virtual

Abra o terminal do VS Code na pasta do projeto e execute:

```powershell
python -m venv .venv
```

---

## ▶️ Ativação do Ambiente Virtual

### Windows (PowerShell)

```powershell
.venv\Scripts\activate
```

Caso apareça erro de permissão no PowerShell:

```powershell
Set-ExecutionPolicy Unrestricted -Scope Process
```

Depois execute novamente:

```powershell
.venv\Scripts\activate
```

---

## 📦 Instalação das Dependências

Execute o comando abaixo no terminal:

```powershell
pip install fastapi uvicorn jinja2 mysql-connector-python
```

---

# 🗄️ Configuração do Banco de Dados

## 📌 Iniciar o MySQL

1. Abra o XAMPP Control Panel
2. Ative o módulo:
   - MySQL

---

## 📌 Executar o Script SQL

1. Abra o MySQL Workbench
2. Abra o arquivo `.sql` do projeto
3. Execute o script para:
   - Criar o banco de dados
   - Criar as tabelas
   - Popular os dados iniciais

---

# 🔌 Configuração da Conexão com o MySQL

Verifique no arquivo de conexão com o banco de dados se as credenciais estão corretas.

Exemplo:

```python
mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hotelaria"
)
```

Caso necessário, altere:

- host
- user
- password
- database

de acordo com sua configuração local do MySQL.

---

# ▶️ Como Executar o Projeto

Com o ambiente virtual ativado, execute o servidor FastAPI:

```powershell
uvicorn app:app --reload
```

---

## ✅ Resultado Esperado

Após executar o comando, o terminal exibirá algo semelhante a:

```text
Uvicorn running on http://127.0.0.1:8000
```

---

# 🌐 Acessando o Sistema

Abra o navegador e acesse:

```text
http://127.0.0.1:8000
```

Também é possível acessar diretamente pelo link exibido no terminal.

---

# 📂 Estrutura do Projeto

```text
projeto/
│
├── app.py
├── database/
├── models/
├── routes/
├── templates/
├── static/
└── script.sql
```

---

# ❗ Observações

- O projeto foi desenvolvido para ambiente Windows.
- Recomenda-se utilizar o navegador em modo anônimo para evitar problemas de cache.
- Certifique-se de que o MySQL esteja ativo antes de iniciar a aplicação.

---

# 🛑 Encerrar o Servidor

Para parar a execução do servidor:

```text
CTRL + C
```
