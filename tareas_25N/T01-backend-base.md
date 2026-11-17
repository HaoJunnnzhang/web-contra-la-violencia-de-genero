# T01 · Backend base and submissions / Backend base y envíos

## English
**Goal:** Create the Flask app, the SQLite database and the public submission endpoints.

**To do**
- `app.py` with Flask and a function that creates the tables if they do not exist:
  - `mural(id, texto ≤200, creado, visible DEFAULT 1)`
  - `foro(id, titulo ≤80, texto ≤1000, creado, aprobado DEFAULT 0)`
- `POST /mural` and `POST /foro`: validate input (trim, not empty, max length) and insert with **parameterized queries**.
- Redirect to `GET /gracias` (simple confirmation page).
- Serve `GET /participa` (template provided by T06).

**Done when**
- Submitting the form stores the row in SQLite and shows `/gracias`.
- Empty or too-long texts are rejected.
- No SQL is built by concatenating strings.

---

## Español
**Objetivo:** Crear la aplicación Flask, la base de datos SQLite y las rutas públicas de envío.

**Qué hay que hacer**
- `app.py` con Flask y una función que crea las tablas si no existen:
  - `mural(id, texto ≤200, creado, visible DEFAULT 1)`
  - `foro(id, titulo ≤80, texto ≤1000, creado, aprobado DEFAULT 0)`
- `POST /mural` y `POST /foro`: validar la entrada (quitar espacios, no vacía, longitud máxima) e insertar con **consultas parametrizadas**.
- Redirigir a `GET /gracias` (página de confirmación sencilla).
- Servir `GET /participa` (plantilla de la T06).

**Terminado cuando**
- Al enviar el formulario se guarda la fila en SQLite y aparece `/gracias`.
- Se rechazan textos vacíos o demasiado largos.
- Ninguna consulta SQL se construye concatenando texto.
