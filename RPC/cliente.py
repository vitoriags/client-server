import xmlrpc.client
with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:

    parar = 0

    while parar != 5:
        menu = int(input("\n(1) Soma\n(2) Subtração\n(3)Multiplicação\n(4)Divisão\n(5)Sair\n"))

        if menu == 1:
            print("\nSOMA")
            num1 = int(input("primero número: "))
            num2 = int(input("segundo número: "))
            print("SOMA: %s" % str(proxy.calculadora(menu, num1, num2)))

        elif menu == 2:
            print("\nSUBTRAÇÃO")
            num1 = int(input("primero número: "))
            num2 = int(input("segundo número: "))
            print("SOMA: %s" % str(proxy.calculadora(menu, num1, num2)))

        elif menu == 3:
            print("\nMULTIPLICAÇÃO")
            num1 = int(input("primero número: "))
            num2 = int(input("segundo número: "))
            print("SOMA: %s" % str(proxy.calculadora(menu, num1, num2)))

        elif menu == 4:
            print("\nDIVISÃO")
            num1 = int(input("primero número: "))
            num2 = int(input("segundo número: "))
            print("SOMA: %s" % str(proxy.calculadora(menu, num1, num2)))

        parar = menu
