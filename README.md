# PROJETO HOTELARIA

## Descrição

O projeto consiste em um sistema de hotelaria com front-end e back-end seguindo a arquitetura MVC, desenvolvido utilizando:

- FastAPI
- Jinja2
- MySQL Connector

O sistema possui funcionalidades completas de CRUD para:

- Hóspedes
- Quartos
- Reservas

As operações incluem:

- Criar
- Editar
- Excluir
- Visualizar

Os dados são manipulados por meio de uma API integrada ao banco de dados MySQL.

---

# Tecnologias Utilizadas

- Python
- FastAPI
- Jinja2
- MySQL
- MySQL Connector
- Uvicorn
- HTML/CSS

---

# Requisitos

- Windows
- Python instalado
- XAMPP
- MySQL Workbench
- VS Code (recomendado)

---

# Instruções de Instalação

## 1. Iniciar o MySQL no XAMPP

Abra o **XAMPP Control Panel** e ative o módulo:

- MySQL

---

## 2. Executar o Script SQL

1. Abra o **MySQL Workbench**
2. Abra o arquivo `.sql` do projeto
3. Execute o script para:
   - Criar o banco de dados
   - Criar as tabelas
   - Popular os dados iniciais

---

## 3. Abrir o Projeto no VS Code

Abra a pasta do projeto no VS Code.

---

## 4. Criar o Ambiente Virtual

No terminal do VS Code, execute:

```powershell
python -m venv .venv
