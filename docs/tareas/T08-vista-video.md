# T08 · Video view / Vista de vídeo

## English
**Goal:** Show the awareness video on the projected screen.

**To do**
- In the video section of `templates/pantalla.html`, add `<video id="video25n" src="/static/video/video.mp4" muted playsinline>`.
- Full-screen size, keeping the proportions (`object-fit: contain`), dark background.
- Expose two functions in `static/js/video.js`: `iniciarVideo()` (rewinds to 0 and plays) and `pararVideo()`.
- The `ended` event is used by T04 to move to the next view.

**Done when**
- The video starts by itself when its view is shown (muted).
- It starts from the beginning every time.
- It fills the screen without being distorted.

---

## Español
**Objetivo:** Mostrar el vídeo de concienciación en la pantalla proyectada.

**Qué hay que hacer**
- En la sección de vídeo de `templates/pantalla.html`, añadir `<video id="video25n" src="/static/video/video.mp4" muted playsinline>`.
- Tamaño de pantalla completa manteniendo la proporción (`object-fit: contain`) y fondo oscuro.
- Exponer dos funciones en `static/js/video.js`: `iniciarVideo()` (vuelve al segundo 0 y reproduce) y `pararVideo()`.
- El evento `ended` lo usa la T04 para pasar a la siguiente vista.

**Terminado cuando**
- El vídeo arranca solo al mostrarse su vista (sin sonido).
- Empieza siempre desde el principio.
- Ocupa la pantalla sin deformarse.
