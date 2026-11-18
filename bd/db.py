"""Acceso a la base de datos SQLite del proyecto 25N.

Uso desde app.py (T01):

    from bd import db
    db.init_db()                      # al arrancar: crea las tablas si no existen
    db.insertar_mural("texto")        # POST /mural
    db.listar_mural(solo_visibles=True, limite=30)   # GET /api/mural (T02)

Todas las consultas son parametrizadas: nunca se concatena texto en el SQL.
La ruta del fichero se toma de la variable de entorno DB_PATH
(por defecto, datos/25n.db). En el despliegue (T05) debe apuntar a un disco
persistente para que los datos sobrevivan a un reinicio.

Ejecutar `python -m bd.db` (desde la raíz del proyecto) crea la base de datos vacía.
"""

import os
import sqlite3
from pathlib import Path

BD_DIR = Path(__file__).resolve().parent
PROYECTO_DIR = BD_DIR.parent
DB_PATH = Path(os.environ.get("DB_PATH", PROYECTO_DIR / "datos" / "25n.db"))
SCHEMA_PATH = BD_DIR / "schema.sql"

# Longitudes máximas (las mismas que en schema.sql y en el formulario de T06).
MAX_MURAL_TEXTO = 200
MAX_FORO_TITULO = 80
MAX_FORO_TEXTO = 1000

# Lista permitida para el panel de administración (T03):
# tabla -> {acción: (sentencia SQL, ...)}. Nada que llegue en la URL se
# mete en el SQL: solo se usa para elegir una de estas sentencias fijas.
_ACCIONES = {
    "mural": {
        "ocultar": "UPDATE mural SET visible = 0 WHERE id = ?",
        "mostrar": "UPDATE mural SET visible = 1 WHERE id = ?",
        "borrar": "DELETE FROM mural WHERE id = ?",
    },
    "foro": {
        "aprobar": "UPDATE foro SET aprobado = 1 WHERE id = ?",
        "retirar": "UPDATE foro SET aprobado = 0 WHERE id = ?",
        "borrar": "DELETE FROM foro WHERE id = ?",
    },
}


def get_conexion():
    """Abre una conexión nueva. Las filas se pueden leer como diccionarios."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(DB_PATH, timeout=10)
    con.row_factory = sqlite3.Row
    # WAL permite leer (pantalla) mientras se escribe (móviles) sin bloqueos.
    con.execute("PRAGMA journal_mode = WAL")
    return con


def init_db():
    """Crea las tablas e índices si no existen. No borra nada."""
    with get_conexion() as con:
        con.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))
    con.close()


def _ejecutar(sql, params=()):
    con = get_conexion()
    try:
        with con:
            cur = con.execute(sql, params)
            return cur
    finally:
        con.close()


def _consultar(sql, params=()):
    con = get_conexion()
    try:
        return [dict(fila) for fila in con.execute(sql, params).fetchall()]
    finally:
        con.close()


# --- Escritura pública (T01) -------------------------------------------------

def insertar_mural(texto):
    """Guarda un mensaje del mural y devuelve su id."""
    return _ejecutar("INSERT INTO mural (texto) VALUES (?)", (texto.strip(),)).lastrowid


def insertar_foro(titulo, texto):
    """Guarda una reflexión del foro (pendiente de aprobar) y devuelve su id."""
    return _ejecutar(
        "INSERT INTO foro (titulo, texto) VALUES (?, ?)",
        (titulo.strip(), texto.strip()),
    ).lastrowid


# --- Lectura (T02 API y T03 admin) -------------------------------------------

def listar_mural(solo_visibles=True, limite=None):
    """Mensajes del mural, más recientes primero."""
    sql = "SELECT id, texto, creado, visible FROM mural"
    if solo_visibles:
        sql += " WHERE visible = 1"
    sql += " ORDER BY creado DESC, id DESC"
    params = ()
    if limite is not None:
        sql += " LIMIT ?"
        params = (int(limite),)
    return _consultar(sql, params)


def listar_foro(solo_aprobadas=True):
    """Reflexiones del foro, más recientes primero.

    Con solo_aprobadas=False (panel de admin) las pendientes van primero.
    """
    if solo_aprobadas:
        sql = ("SELECT id, titulo, texto, creado, aprobado FROM foro "
               "WHERE aprobado = 1 ORDER BY creado DESC, id DESC")
    else:
        sql = ("SELECT id, titulo, texto, creado, aprobado FROM foro "
               "ORDER BY aprobado ASC, creado DESC, id DESC")
    return _consultar(sql)


# --- Moderación (T03) --------------------------------------------------------

def aplicar_accion(tabla, id_, accion):
    """Aplica una acción de moderación. Devuelve True si cambió alguna fila.

    Lanza ValueError si la tabla o la acción no están en la lista permitida.
    """
    try:
        sql = _ACCIONES[tabla][accion]
    except KeyError:
        raise ValueError(f"Acción no permitida: {tabla}/{accion}") from None
    return _ejecutar(sql, (int(id_),)).rowcount > 0


if __name__ == "__main__":
    init_db()
    print(f"Base de datos lista en {DB_PATH}")
