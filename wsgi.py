"""Punto de entrada en producción (T05). Lo usa gunicorn: `gunicorn wsgi:app`.

La app se publica en un subdirectorio detrás de NGINX
(…/colaboraciones/2026-2027/web-contra-la-violencia-de-genero/). NGINX quita ese
prefijo y lo envía en la cabecera X-Forwarded-Prefix. ProxyFix lo lee para que
url_for() y redirect() generen las URLs con el prefijo correcto.

En local se sigue usando `flask --app app run`; este archivo no hace falta.
"""

from werkzeug.middleware.proxy_fix import ProxyFix

from app import app

app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)
