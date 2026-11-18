-- Esquema de la base de datos SQLite del proyecto 25N.
-- Se aplica con init_db() en db.py (o: sqlite3 datos/25n.db < schema.sql).
-- Es idempotente: se puede ejecutar varias veces sin perder datos.

-- Mensajes cortos del mural de burbujas (T01, T02, T03, T07).
-- Se publican directamente; la moderación solo los oculta (visible = 0).
CREATE TABLE IF NOT EXISTS mural (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    texto   TEXT    NOT NULL CHECK (length(trim(texto)) BETWEEN 1 AND 200),
    creado  TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%d %H:%M:%S', 'now')),
    visible INTEGER NOT NULL DEFAULT 1 CHECK (visible IN (0, 1))
);

-- Reflexiones del foro (T01, T02, T03, T09).
-- No se muestran hasta que una persona moderadora las aprueba (aprobado = 1).
CREATE TABLE IF NOT EXISTS foro (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo   TEXT    NOT NULL CHECK (length(trim(titulo)) BETWEEN 1 AND 80),
    texto    TEXT    NOT NULL CHECK (length(trim(texto))  BETWEEN 1 AND 1000),
    creado   TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%d %H:%M:%S', 'now')),
    aprobado INTEGER NOT NULL DEFAULT 0 CHECK (aprobado IN (0, 1))
);

-- Índices para las consultas de la pantalla (/api/mural y /api/foro).
CREATE INDEX IF NOT EXISTS idx_mural_visible_creado ON mural (visible, creado DESC);
CREATE INDEX IF NOT EXISTS idx_foro_aprobado_creado ON foro (aprobado, creado DESC);
