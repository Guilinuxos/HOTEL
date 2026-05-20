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

    reser_query = """
            DELETE FROM
                reservas
            WHERE
                hospede_id = %s
                """

    hosp_query = """
            DELETE FROM
                hospedes
            WHERE
                id = %s
            """
    
    cursor.execute(reser_query, (id,))
    cursor.execute(hosp_query, (id,))
    cn.commit() 
    cursor.close()
    cn.close()

# ─────────
# quartos
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

def add_quarto(numero, tipo, valor_diaria, status):
    cn = connection()
    cursor = cn.cursor(dictionary=True)

    query = """
            INSERT INTO
                quartos (numero, tipo, valor_diaria, status)
            VALUES
                (%s, %s, %s, %s)
            """
    cursor.execute(query, (numero, tipo, valor_diaria, status))
    cn.commit()

    cn.close()
    cursor.close()

def udpate_quarto(id, numero, tipo, valor_diaria, status):
    cn = connection()
    cursor = cn.cursor(dictionary=True)

    query = """
            UDPATE quartos
                set numero = %s,
                tipo = %s,
                valor_diaria = %s,
                status = %s
            WHERE id = %s
            """
    
    cursor.execute(query, (numero, tipo, valor_diaria, status, id))
    cn.commit()

    cursor.close()
    cn.close()

def delete_quarto(id):
    cn = connection()
    cursor = cn.cursor(dictionary=True)

    cursor.execute("DELETE FROM quartos WHERE id = %s", (id,))
    cursor.close()
    cn.commit()

# ─────────
# RESERVAS
# ─────────

def consulta_reservas_ativas():
    cn = connection()
    cursor = cn.cursor(dictionary=True)

    query = """
        SELECT reservas.id, 
        hospedes.nome AS hospede, 
        quartos.numero AS quarto,
        reservas.data_entrada,
        reservas.data_saida
        
        FROM reservas
        JOIN hospedes ON 
            reservas.hospede_id = hospedes.id
        JOIN quartos ON 
            reservas.quarto_id = quartos.id
    """

    cursor.execute(query)
    request = cursor.fetchall()

    cursor.close()
    cn.close()

    return request

def consulta_reserva_id(id):
    cn = connection()
    cursor = cn.cursor(dictionary=True)

    query = """
        SELECT r.*,
               h.nome   AS nome_hospede,
               q.numero AS numero_quarto
        FROM reservas r
        JOIN hospedes h ON r.hospede_id = h.id
        JOIN quartos  q ON r.quarto_id  = q.id
        WHERE r.id = %s
    """

    cursor.execute(query, (id,))
    request = cursor.fetchone()

    cursor.close()
    cn.close()

    return request

def add_reserva(hospede_id, quarto_id, data_entrada, data_saida):
    cn = connection()
    cursor = cn.cursor(dictionary=True)

    query = """
            INSERT INTO reservas (hospede_id, quarto_id, data_entrada, data_saida)
            VALUES (%s, %s, %s, %s)
            """
    cursor.execute(query,(hospede_id, quarto_id, data_entrada, data_saida))
    cn.commit()
    cursor.close()
    cn.close()

def update_reserva(id, hospede_id, quarto_id, data_entrada, data_saida):
    cn = connection()
    cursor = cn.cursor(dictionary=True)

    query = """
        UPDATE reservas
        SET hospede_id   = %s,
            quarto_id    = %s,
            data_entrada = %s,
            data_saida   = %s
        WHERE id = %s
            """
    
    cursor.execute(query, (hospede_id, quarto_id, data_entrada, data_saida, id))
    cn.commit()
    cursor.close()
    cn.close()

def delete_reserva(id):
    cn = connection()
    cursor = cn.cursor(dictionary=True)

    cursor.execute("DELETE FROM reservas WHERE id = %s", (id,))
    cn.commit()
    cursor.close()
    cn.close()

def consulta_todas_reservas():
     conn = connection()
     cursor = conn.cursor(dictionary=True)

     query = """
         SELECT r.*,
                h.nome   AS nome_hospede,
                q.numero AS numero_quarto
         FROM reservas r
         JOIN hospedes h ON r.hospede_id = h.id
         JOIN quartos  q ON r.quarto_id  = q.id
         ORDER BY r.data_entrada
     """

     cursor.execute(query)
     request = cursor.fetchall()

     cursor.close()
     conn.close()

     # converter datas para string (JSON serializable)
     for r in request:
        if hasattr(r.get('data_entrada'), 'isoformat'):
            r['data_entrada'] = r['data_entrada'].isoformat()
        
        if hasattr(r.get('data_saida'), 'isoformat'):
             r['data_saida'] = r['data_saida'].isoformat()

     return request