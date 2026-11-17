# T10 · QR and screen styles / QR y estilos de pantalla

## English
**Goal:** Give the projected screen a common look and show the QR at all times.

**To do**
- Generate the QR image (`static/qr.png`) with the final public URL of `/participa` (provided by T05). Any QR generator or the Python `qrcode` library works.
- Place the QR fixed in a corner of `pantalla.html`, visible in all three views, with a short text: *"Leave your message / Deja tu mensaje"*.
- `static/estilos.css` shared by the screen: 25N purple palette, high contrast, large font, clean layout.
- Test `/participa` on several phones (Android and iPhone, different sizes) and report problems.

**Done when**
- The QR can be scanned from 3–4 metres away on the real screen.
- The QR opens `/participa` correctly.
- All screen views share the same visual style.

---

## Español
**Objetivo:** Dar a la pantalla proyectada un aspecto común y mostrar el QR en todo momento.

**Qué hay que hacer**
- Generar la imagen del QR (`static/qr.png`) con la URL pública definitiva de `/participa` (la da la T05). Vale cualquier generador de QR o la librería `qrcode` de Python.
- Colocar el QR fijo en una esquina de `pantalla.html`, visible en las tres vistas, con un texto corto: *«Leave your message / Deja tu mensaje»*.
- `static/estilos.css` común para la pantalla: paleta morada del 25N, alto contraste, letra grande y diseño limpio.
- Probar `/participa` en varios móviles (Android e iPhone, distintos tamaños) e informar de los problemas.

**Terminado cuando**
- El QR se puede escanear a 3–4 metros en la pantalla real.
- El QR abre `/participa` correctamente.
- Todas las vistas de la pantalla comparten el mismo estilo visual.
