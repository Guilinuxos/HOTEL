from dao import connection
from datetime import date

# ─────────
# HÓSPEDES
# ─────────

def consulta_hospedes():
    cn = connection()
    cursor = cn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM hospedes")
    request = cursor.fetchall()

    cursor.close()
    cn.close()

    return request

def consulta_hospede_id(id):
    cn = connection()
    cursor = cn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM hospedes WHERE id =%s",(id,))
    request = cursor.fetchone()

    cursor.close()
    cn.close()

    return request

def add_hospede(nome, email, telefone, cpf):
    cn = connection()
    cursor = cn.cursor(dictionary=True)

    query = """
            INSERT INTO hospedes (nome, email, telefone, cpf)
             VALUES (%s, %s, %s, %s)
            """
    
    cursor.execute(query, (nome, email, telefone, cpf))
    cn.commit()
    cursor.close()
    cn.close()

def update_hospede(id, nome, email, telefone, cpf):
    cn = connection()
    cursor = cn.cursor(dictionary=True)

    query = """
        UPDATE hospedes
        SET nome     = %s,
            email    = %s,
            telefone = %s,
            cpf      = %s
        WHERE id = %s
            """
    
    cursor.execute(query, (nome, email, telefone, cpf, id))
    cn.commit()
    cursor.close()
    cn.close()

def delete_hospede(id):
    cn = connection()
    cursor = cn.cursor(dictionary=True)

    query = """
            DELETE FROM
                hospedes
            WHERE
                id = %s
            """

    cursor.execute(query, (id,))
    cn.commit() 
    cursor.close()
    cn.close()

# ─────────
# HÓSPEDES
# ─────────

def consulta_quartos():
    cn = connection()
    cursor = cn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM quartos")
    request = cursor.fetchall()

    cursor.close()
    cn.close()

    return request

def consulta_quarto_id(id):
    cn = connection()
    cursor = cn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM quartos WHERE id =%s",(id,))
    request = cursor.fetchone()

    cursor.close()
    cn.close()

    return request

