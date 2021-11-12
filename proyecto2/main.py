from arbol import Arbol

def perder(aquinator, nodoActual):
    print("nO PuEde se, He perdio chavale!!!!!!!!!!")
    datoPadre = input("Digite la caracteristica de su personaje: ")
    nodoPadre = aquinator.insertarPregunta(nodoActual, datoPadre)
    datoHijo = input("Digite su personaje caracteristico: ")
    aquinator.insertarPersonaje(nodoPadre, datoHijo)

def jugar(aquinator, opcion=None, nodoActual=None):

    nodo = aquinator.obtener(opcion, nodoActual)
    if nodo is False:
        perder(aquinator, nodoActual)
    elif nodo is True:
        print("He ganao chavale")
    else:
        opcion = input("¿Su personaje es " + nodo.dato() + "?" + " Acerte? S/N: ")  # falta validar que solo sea S o N
        jugar(aquinator, opcion, nodo)

def main():
    seguir = True
    aquinator = Arbol()
    # cargar
    aquinator.insertar("deportista")
    print("----------------AQUINATOR-----------------")
    while seguir:
        jugar(aquinator)
        opcion = input("Desea seguir jugando? S/N: ")
        if opcion == "N":
            seguir = False


if __name__ == '__main__':
    main()