CREATE DATABASE IF NOT EXISTS listproduct;
USE listproduct;
CREATE TABLE IF NOT EXISTS productos(
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
    eliminado TINYINT(1) NOT NULL
)
