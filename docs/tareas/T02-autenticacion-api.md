# T02 · Authentication and JSON API / Autenticación y API JSON

## English
**Goal:** Protect the screen and admin areas and expose the data the screen needs.

**To do**
- HTTP Basic Auth decorator. Users and passwords read from environment variables (`ADMIN_USER`, `ADMIN_PASS`, `PANTALLA_USER`, `PANTALLA_PASS`).
- Endpoint names: `pantalla`, `api_mural`, `api_foro` (see README). Use `db.listar_mural(limite=30)` and `db.listar_foro()`.
- Admin credentials give access to `/admin`, `/pantalla` and the API. Screen credentials give access to `/pantalla` and the API only.
- `GET /api/mural`: JSON list `[{id, texto}]` with `visible = 1`, newest first, max 30.
- `GET /api/foro`: JSON list `[{id, titulo, texto}]` with `aprobado = 1`, newest first.

**Done when**
- Without credentials, `/pantalla`, `/admin` and `/api/*` return 401.
- Hidden messages and unapproved reflections never appear in the API.
- No password is written in the code.

---

## Español
**Objetivo:** Proteger la pantalla y la administración y ofrecer los datos que necesita la pantalla.

**Qué hay que hacer**
- Decorador de HTTP Basic Auth. Usuarios y contraseñas leídos de variables de entorno (`ADMIN_USER`, `ADMIN_PASS`, `PANTALLA_USER`, `PANTALLA_PASS`).
- Nombres de endpoint: `pantalla`, `api_mural`, `api_foro` (ver README). Usar `db.listar_mural(limite=30)` y `db.listar_foro()`.
- Las credenciales de admin dan acceso a `/admin`, `/pantalla` y la API. Las de pantalla, solo a `/pantalla` y la API.
- `GET /api/mural`: lista JSON `[{id, texto}]` con `visible = 1`, más recientes primero, máximo 30.
- `GET /api/foro`: lista JSON `[{id, titulo, texto}]` con `aprobado = 1`, más recientes primero.

**Terminado cuando**
- Sin credenciales, `/pantalla`, `/admin` y `/api/*` devuelven 401.
- Los mensajes ocultos y las reflexiones sin aprobar nunca aparecen en la API.
- Ninguna contraseña está escrita en el código.
