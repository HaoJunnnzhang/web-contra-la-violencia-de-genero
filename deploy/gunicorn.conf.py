# Configuración de gunicorn en producción (T05).
# Uso: gunicorn -c deploy/gunicorn.conf.py wsgi:app

# Solo accesible desde la propia máquina: NGINX es quien la publica.
bind = "127.0.0.1:8256"

# SQLite en modo WAL aguanta bien pocas escrituras simultáneas.
# 2 procesos x 4 hilos sobra para el público de un evento.
workers = 2
threads = 4
timeout = 30


def on_starting(server):
    """Crea la BD una sola vez, en el proceso principal, antes de lanzar los workers."""
    from bd import db

    db.init_db()


# Logs a la salida estándar: los recoge systemd (journalctl -u 25n-web).
accesslog = "-"
errorlog = "-"
loglevel = "info"
