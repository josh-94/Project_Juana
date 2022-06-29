def validar_nPedido(numeroPedido: str) -> bool:
    """
        Funcion que valida la cantidad de caracteres del numero de pedido debe ser 4
        """
    return len(numeroPedido) > 4
