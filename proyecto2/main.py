from arbol import Arbol
from nodo import Nodo

def perder(nodoActual):
    datoActual = nodoActual.dato()
    print("Buena esa, CracK")
    if datoActual[0] == 'P':
        datoHijo = input("Que personaje era?: ")
        datoPadre = input("Digite una frase que diferencia a su personaje: ")
        nodoActual._derecha = Nodo('P' + datoPadre)
        nodoActual.derecha()._izquierda = Nodo('R' + datoHijo)
        nodoActual.derecha()._derecha = Nodo('R' + "None")
    else:
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
    elif nodo.dato() == "RNone":
        perder(nodoActual)
    else:
        opcion = input("¿Su personaje es " + nodo.dato() + "?" + " Acerte? S/N: ")  # falta validar que solo sea S o N
        jugar(aquinator, opcion, nodo)


def main():
    seguir = True
    preguntasyrespuestas = []
    with open('preguntasyrespuestas.txt', 'r') as fichero:
        for linea in fichero:
            preguntasyrespuestas.append(linea.rstrip())

    preguntasyrespuestas.reverse()

    aquinator = Arbol(preguntasyrespuestas)
    # MUESTRA EL ARBOL
    # aquinator.verArbol()

    print("----------------AQUINATOR-----------------")
    while seguir:
        jugar(aquinator)
        opcion = input("Desea seguir jugando? S/N: ")
        if opcion == "N":
            seguir = False

    aquinator.guardar()

    # COSAS QUE HACEN FALTA:
    # VALIDAR QUE SOLO SE INGRESE S Y N Y REITERAR QUE SOLO ESOS DIGITOS SON VALIDOS
    # AL MOSTRAR LA RESPUESTA SE MUESTRA EL P O R, VER COMO IGNORARLO O AL INGRESAR IGNORAR EL PRIMER DIGITO,
    # ESTETICA NO ES OBLIGATORIO


if __name__ == '__main__':
    main()
