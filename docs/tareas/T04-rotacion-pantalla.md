# T04 · Screen rotation and polling / Rotación de la pantalla y actualización

## English
**Goal:** Make `/pantalla` cycle through the three views and keep the data up to date.

**To do**
- `templates/pantalla.html` with three sections (mural, video, forum); only one visible at a time.
- `static/js/pantalla.js`:
  - Configurable sequence and duration per view (default 5 minutes).
  - The video view advances on the video `ended` event, not on a timer.
  - Every 10 s, `fetch(document.body.dataset.apiMural)` and `fetch(document.body.dataset.apiForo)` (never `'/api/...'`: the app runs in a subdirectory), then call `pintarMural(datos)` and `pintarForo(datos)` (provided by T07 and T09).
  - If a request fails, keep showing the last data (no blank screen).
- Fullscreen button or instructions to use F11.

**Done when**
- The screen runs alone for 15 minutes completing at least one full cycle.
- A new message appears on the wall within ~10 s.
- Disconnecting the network does not break the screen.

---

## Español
**Objetivo:** Que `/pantalla` vaya alternando las tres vistas y mantenga los datos al día.

**Qué hay que hacer**
- `templates/pantalla.html` con tres secciones (mural, vídeo, foro); solo una visible a la vez.
- `static/js/pantalla.js`:
  - Secuencia y duración por vista configurables (5 minutos por defecto).
  - La vista de vídeo avanza con el evento `ended` del vídeo, no por tiempo.
  - Cada 10 s, `fetch(document.body.dataset.apiMural)` y `fetch(document.body.dataset.apiForo)` (nunca `'/api/...'`: la app vive en un subdirectorio), y llamar a `pintarMural(datos)` y `pintarForo(datos)` (de las tareas T07 y T09).
  - Si una petición falla, se siguen mostrando los últimos datos (nunca pantalla en blanco).
- Botón de pantalla completa o indicación de usar F11.

**Terminado cuando**
- La pantalla funciona sola durante 15 minutos y completa al menos un ciclo entero.
- Un mensaje nuevo aparece en el mural en unos 10 s.
- Si se corta la red, la pantalla no se rompe.
