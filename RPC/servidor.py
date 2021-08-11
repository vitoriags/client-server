#servidor


from xmlrpc.server import SimpleXMLRPCServer

def calculadora(menu, numero1, numero2):
    if menu == 1:
        return numero1 + numero2

    elif menu == 2:
        return numero1 - numero2

    elif menu == 3:
        return numero1 * numero2

    elif menu == 4:
        return numero1 / numero2

s = SimpleXMLRPCServer(("localhost", 8000))
s.register_function(calculadora, "calculadora")
s.serve_forever()
