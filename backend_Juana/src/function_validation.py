def validar_nPedido(numeroPedido: str) -> bool:
    """
        Funcion que valida la cantidad de caracteres del numero de pedido debe ser 4
        """
    return len(numeroPedido) > 4

#def validar_password(password: str):
#    """
#        Funcion que valida la cantidad de caracteres del password debe ser 8
#        """
#    if len(password) > 7:
#        count = 0
#        for i in password:
#            if i.isspace() is True:
#                count += 1
#        if count == 0:
#            return True
#        else:
#            return False
