def menu ():
    menu= {
        1:("pikachu roll ", 4500),
        2:("otaku roll",5000),
        3:("pulpo venenoso", 5200),
        4:("anguila electrica roll", 4800)
    }

    while True:
        pedido = {}


        print("\n bienvenido a sushi ")


        while True:
            print("\nmenu de rolls")
            for opcion , (nombre, precio) in menu.items():
                print(f"{opcion}.{nombre} - ${precio}")
            print("5. finalizar pedido ")


            try:
                opcion =int(input("seleccione una opcion :"))
                if opcion == 5:
                    break
                elif opcion in menu:
                    pedido[opcion]= pedido.get(opcion, 0) + 1 
                    print(f"{menu   [opcion][0]} agregado al pedido")
                else:
                    print("opcion invalida, intenta denuevo")
            except ValueError:
                print("entrada no valida, ingresa un numero entre 1 y 5")
        if not pedido:
            print("no se ha seleccionado ningun producto, volviendo al menu principal ")
            continue
        subtotal= sum(menu[opcion][1]* cantidad for opcion , cantidad in pedido.items())


        descuento=0
        while True:
            tiene_codigo=input("tiene un codigo de descuento ?(si/no): ").strip().lower()
            if tiene_codigo == 'si':
                codigo=input("ingrese el codigo de descuento: ").strip()
            if codigo =="otaku":
                descuento= subtotal * 0.10
                print("codigo valido, se aplicara descuento")
                break
            else:
                print("codigo invalido, intente denuevo o escriba X para continuar sin codigo ")
                if input("desea intentar nuevamente (si/no):" ).strip().lower() !="s":
                    break
                elif tiene_codigo=="no":
                    break
                else:
                    print("respuesta invalida, ingresa 'si'  ' no' .")

        total=subtotal - descuento

        print("\n detalle de pedido ")
        print("**********************")
        total_productos= sum(pedido.values())
        print(f"total productos:{total_productos}")
        print("***********************************")
        for opcion, cantidad in pedido.items():
            print(f"{menu[opcion][0]} : {cantidad}")
        print("**********************************")
        print(f"subtotal por pagar: ${subtotal}") 
        print(f"descuento codigo:{descuento} ")
        print(f"total : ${total}")
        otra_vez=input("\n desea realizar otro pedido? (si/no):").strip().lower()
        if otra_vez != "si":
            print("gracias por su compra ")
            break


if __name__ == "__main__":
    menu()
