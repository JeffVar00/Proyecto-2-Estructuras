from arbol import Arbol
from nodo import Nodo


def perder(nodoActual):
    datoActual = nodoActual.dato()
    print("Buena esa, CracK")
    datoHijo = input("Que personaje era?: ")
    datoPadre = input("Digite una frase que diferencia a su personaje: ")
    nodoActual._dato = 'P' + datoPadre
    nodoActual._izquierda = Nodo('R' + datoHijo)
    nodoActual._derecha = Nodo('R' + datoActual)


def jugar(aquinator, opcion=None, nodoActual=None):
    nodo = aquinator.obtener(opcion, nodoActual)
    if nodo is False:
        perder(nodoActual)
    elif nodo is True:
        print("Te adivine que era, mas respeto CRACK")
    else:
        opcion = input("¿Su personaje es " + nodo.dato() + "?" + " Acerte? S/N: ")  # falta validar que solo sea S o N
        jugar(aquinator, opcion, nodo)


def main():
    seguir = True

    preguntasyrespuestas = ["PDeportista", "RKeylor Navas", "PConductor", "RBrayan Ruiz", "PMusico", "RZeta"]
    preguntasyrespuestas.reverse()

    aquinator = Arbol(preguntasyrespuestas)

    print("----------------AQUINATOR-----------------")
    while seguir:
        jugar(aquinator)
        opcion = input("Desea seguir jugando? S/N: ")
        if opcion == "N":
            seguir = False


if __name__ == '__main__':
    main()
