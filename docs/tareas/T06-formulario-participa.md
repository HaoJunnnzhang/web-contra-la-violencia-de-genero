# T06 · Participation form / Formulario de participación

## English
**Goal:** Build `/participa`, the only page the public sees (opened from the QR).

**To do**
- Mobile-first HTML + CSS template (`templates/participa.html`).
- Two options (tabs or two blocks):
  - **Bubble message:** one `textarea` (max 200), `form method="POST" action="{{ url_for('crear_mural') }}"`.
  - **Reflection:** title (max 80) + text (max 1000), `form method="POST" action="{{ url_for('crear_foro') }}"`.
- Use `maxlength` and `required` in the inputs.
- Privacy notice: *"Do not use real names or details that identify anyone."*
- Note under the forum: *"Your reflection will be shown after review."*
- `templates/gracias.html`: thank-you message and a link to send another one.
- Optional: character counter.

**Done when**
- Looks good and is easy to use on a 360 px-wide phone.
- Both forms send the data correctly.
- Text and buttons are large enough to tap.

---

## Español
**Objetivo:** Crear `/participa`, la única página que ve el público (se abre desde el QR).

**Qué hay que hacer**
- Plantilla HTML + CSS mobile first (`templates/participa.html`).
- Dos opciones (pestañas o dos bloques):
  - **Mensaje burbuja:** un `textarea` (máx. 200), `form method="POST" action="{{ url_for('crear_mural') }}"`.
  - **Reflexión:** título (máx. 80) + texto (máx. 1000), `form method="POST" action="{{ url_for('crear_foro') }}"`.
- Usar `maxlength` y `required` en los campos.
- Aviso de privacidad: *«No uses nombres reales ni datos que identifiquen a nadie.»*
- Nota bajo el foro: *«Tu reflexión se mostrará tras ser revisada.»*
- `templates/gracias.html`: mensaje de agradecimiento y enlace para enviar otro.
- Opcional: contador de caracteres.

**Terminado cuando**
- Se ve bien y es fácil de usar en un móvil de 360 px de ancho.
- Los dos formularios envían los datos correctamente.
- Los textos y botones son lo bastante grandes para pulsarlos.
