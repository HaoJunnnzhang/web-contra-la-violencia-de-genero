# T03 · Admin panel / Panel de administración

## English
**Goal:** Let the moderator manage content from a phone or a computer.

**To do**
- `GET /admin` (admin credentials only), rendered on the server with Jinja.
- Two lists: bubble messages and forum reflections, newest first, with status.
- Buttons (small HTML forms): **Hide/Show** (mural), **Approve** (forum), **Delete** (both).
- `POST /admin/<tabla>/<id>/<accion>`: validate table and action against an allowed list, run the change and redirect to `/admin`.
- Forum reflections pending approval are highlighted at the top.

**Done when**
- Hiding a message removes it from the screen within the next refresh.
- Approving a reflection makes it appear on the screen.
- The page is usable on a phone.

---

## Español
**Objetivo:** Que la persona moderadora gestione el contenido desde el móvil o el ordenador.

**Qué hay que hacer**
- `GET /admin` (solo credenciales de admin), generada en el servidor con Jinja.
- Dos listas: mensajes del mural y reflexiones del foro, más recientes primero, con su estado.
- Botones (pequeños formularios HTML): **Ocultar/Mostrar** (mural), **Aprobar** (foro), **Borrar** (ambos).
- `POST /admin/<tabla>/<id>/<accion>`: validar tabla y acción contra una lista permitida, aplicar el cambio y redirigir a `/admin`.
- Las reflexiones pendientes de aprobar aparecen destacadas arriba.

**Terminado cuando**
- Al ocultar un mensaje, desaparece de la pantalla en la siguiente actualización.
- Al aprobar una reflexión, aparece en la pantalla.
- La página se puede usar en el móvil.
