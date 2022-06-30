CREATE TABLE `BD_juana`.`Pedidos` (
  `idPedidos` INT NOT NULL,
  `id_estados_pedidos` INT NOT NULL,
  PRIMARY KEY (`idPedidos`),
  INDEX `fk_estado_pedidos_idx` (`id_estados_pedidos` ASC) VISIBLE,
  CONSTRAINT `fk_estado_pedidos`
    FOREIGN KEY (`id_estados_pedidos`)
    REFERENCES `BD_juana`.`estado_pedidos` (`id_estado_pedidos`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE);