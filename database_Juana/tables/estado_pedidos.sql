CREATE DATABASE IF NOT EXISTS BD_juana;
USE BD_juana;
CREATE TABLE IF NOT EXISTS estado_pedidos(
    numeroGuia VARCHAR(25) NULL,
    numeroPedido VARCHAR(25) NULL,
    estado VARCHAR(2) NULL,
    lugar VARCHAR(100) NULL,
    quienRecibe VARCHAR(20) NULL,
    motivoDescripcion VARCHAR(100) NULL,
    fecha VARCHAR(10) NULL,
    hora VARCHAR(10) NULL,
    link VARCHAR(400) NULL,
    observacion VARCHAR(100) NULL,
    tiempo DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    eliminado TINYINT(1) NOT NULL,
    id_estado_pedidos INT Primary key NOT NULL
);

