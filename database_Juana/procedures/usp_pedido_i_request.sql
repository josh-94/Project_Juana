DELIMITER $$

DROP PROCEDURE IF EXISTS usp_pedido_i_request$$

CREATE PROCEDURE usp_pedido_i_request(
    p_header VARCHAR(800),
    p_content TEXT,
    OUT o_result INT
)
BEGIN
    SET o_result = 0;

    INSERT INTO pedido_request
        (
            header,
            content,
            insert_datetime
        )
    VALUES
        (
            p_header,
            p_content,
            NOW()
        );
        
    SET o_result = 1;
END$$

DELIMITER ;