# T09 · Forum view / Vista del foro

## English
**Goal:** Show the approved reflections on the projected screen.

**To do**
- In `static/js/foro.js`, write `pintarForo(reflexiones)`, which receives an array like `[{id: 1, titulo: "...", texto: "..."}]`.
- Each reflection is a card with a title and text.
- Show 2–3 cards at a time and rotate them every ~15 s (or a slow automatic scroll).
- **Always insert the text with `textContent`, never with `innerHTML`.**
- If there are no reflections, show a message such as *"Scan the QR and share your reflection"*.
- Develop with test data until the API is ready.

**Done when**
- Long texts are readable from a distance (cut with "…" if needed).
- It works with 0, 1 and 20 reflections.
- Calling it again with new data updates the cards without breaking the rotation.

---

## Español
**Objetivo:** Mostrar las reflexiones aprobadas en la pantalla proyectada.

**Qué hay que hacer**
- En `static/js/foro.js`, escribir `pintarForo(reflexiones)`, que recibe un array como `[{id: 1, titulo: "...", texto: "..."}]`.
- Cada reflexión es una tarjeta con título y texto.
- Mostrar 2–3 tarjetas a la vez y rotarlas cada ~15 s (o un scroll lento automático).
- **Insertar siempre el texto con `textContent`, nunca con `innerHTML`.**
- Si no hay reflexiones, mostrar un mensaje como *«Escanea el QR y comparte tu reflexión»*.
- Desarrollar con datos de prueba hasta que esté la API.

**Terminado cuando**
- Los textos largos se leen a distancia (se recortan con «…» si hace falta).
- Funciona con 0, 1 y 20 reflexiones.
- Volver a llamarla con datos nuevos actualiza las tarjetas sin romper la rotación.
