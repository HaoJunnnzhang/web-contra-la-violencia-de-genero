# T07 · Bubble wall / Mural de burbujas

## English
**Goal:** Draw the messages as floating bubbles on the projected screen.

**To do**
- In `static/mural.js`, write `pintarMural(mensajes)`, which receives an array like `[{id: 1, texto: "..."}]`.
- Each message is a bubble (`div`) with a random position and a soft floating animation (`@keyframes`).
- Show at most ~30 bubbles; new ones enter with a simple effect (fade or grow).
- **Always insert the text with `textContent`, never with `innerHTML`.**
- Develop with test data (a fake array) until the API is ready.
- Large, readable text from a distance; 25N purple palette.

**Done when**
- Calling `pintarMural()` with 5 or 30 messages shows them without overlapping too much.
- Calling it again with the same messages does not duplicate bubbles.
- A message like `<b>hi</b>` is shown as plain text.

---

## Español
**Objetivo:** Dibujar los mensajes como burbujas flotantes en la pantalla proyectada.

**Qué hay que hacer**
- En `static/mural.js`, escribir `pintarMural(mensajes)`, que recibe un array como `[{id: 1, texto: "..."}]`.
- Cada mensaje es una burbuja (`div`) con posición aleatoria y una animación suave de flotación (`@keyframes`).
- Mostrar como máximo unas 30 burbujas; las nuevas entran con un efecto sencillo (aparecer o crecer).
- **Insertar siempre el texto con `textContent`, nunca con `innerHTML`.**
- Desarrollar con datos de prueba (un array falso) hasta que esté la API.
- Texto grande y legible a distancia; paleta morada del 25N.

**Terminado cuando**
- Llamar a `pintarMural()` con 5 o con 30 mensajes los muestra sin solaparse demasiado.
- Volver a llamarla con los mismos mensajes no duplica burbujas.
- Un mensaje como `<b>hola</b>` se ve como texto normal.
