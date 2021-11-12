from arbol import Arbol
from nodo import Nodo

def perder(nodoActual):
    datoActual = nodoActual.dato()
    print("nO PuEde se, He perdio chavale!!!!!!!!!!")
    datoHijo = input("Que personaje era?: ")
    datoPadre = input("Cual caracteristica diferencia a su personaje?: ")
    nodoActual._dato = datoPadre
    nodoActual._izquierda = Nodo(datoHijo)
    nodoActual._derecha = Nodo(datoActual)

def jugar(aquinator, opcion=None, nodoActual=None):

    nodo = aquinator.obtener(opcion, nodoActual)
    if nodo is False:
        perder(nodoActual)
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
    aquinator.insertar("Keylor Navas")
    aquinator.insertar("Keylor Navassssss")
    print("----------------AQUINATOR-----------------")
    while seguir:
        jugar(aquinator)
        opcion = input("Desea seguir jugando? S/N: ")
        if opcion == "N":
            seguir = False


if __name__ == '__main__':
    main()