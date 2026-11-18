# T01 · Backend base and submissions / Backend base y envíos

## English
**Goal:** Create the Flask app, the SQLite database and the public submission endpoints.

**To do**
- `app.py` with Flask. Call `db.init_db()` from `bd/db.py` at startup (already done: it creates these tables if they do not exist):
  - `mural(id, texto ≤200, creado, visible DEFAULT 1)`
  - `foro(id, titulo ≤80, texto ≤1000, creado, aprobado DEFAULT 0)`
- `POST /mural` and `POST /foro`: validate input (trim, not empty, max length) and insert with `db.insertar_mural()` / `db.insertar_foro()` (**parameterized queries**).
- Redirect with `redirect(url_for('gracias'))` to `GET /gracias` (simple confirmation page). `GET /` redirects to `participa`.
- Use the endpoint names from the README table (`participa`, `crear_mural`, `crear_foro`, `gracias`, `inicio`). The app runs in a subdirectory: never hard-code paths that start with `/`.
- Serve `GET /participa` (template provided by T06).

**Done when**
- Submitting the form stores the row in SQLite and shows `/gracias`.
- Empty or too-long texts are rejected.
- No SQL is built by concatenating strings.

---

## Español
**Objetivo:** Crear la aplicación Flask, la base de datos SQLite y las rutas públicas de envío.

**Qué hay que hacer**
- `app.py` con Flask. Llamar a `db.init_db()` de `bd/db.py` al arrancar (ya hecho: crea estas tablas si no existen):
  - `mural(id, texto ≤200, creado, visible DEFAULT 1)`
  - `foro(id, titulo ≤80, texto ≤1000, creado, aprobado DEFAULT 0)`
- `POST /mural` y `POST /foro`: validar la entrada (quitar espacios, no vacía, longitud máxima) e insertar con `db.insertar_mural()` / `db.insertar_foro()` (**consultas parametrizadas**).
- Redirigir con `redirect(url_for('gracias'))` a `GET /gracias` (página de confirmación sencilla). `GET /` redirige a `participa`.
- Usar los nombres de endpoint de la tabla del README (`participa`, `crear_mural`, `crear_foro`, `gracias`, `inicio`). La app vive en un subdirectorio: nunca escribir rutas que empiecen por `/`.
- Servir `GET /participa` (plantilla de la T06).

**Terminado cuando**
- Al enviar el formulario se guarda la fila en SQLite y aparece `/gracias`.
- Se rechazan textos vacíos o demasiado largos.
- Ninguna consulta SQL se construye concatenando texto.
