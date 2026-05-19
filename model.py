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