from nodo import Nodo

class Arbol:

    def __init__(self, listaPreguntas, raiz=None, actual=None):
        self._raiz = raiz
        self._actual = actual
        self._raiz = self.insertarNodos(listaPreguntas)

    def insertarNodos(self, listaPreguntas):

        if len(listaPreguntas) != 0:

            aux = listaPreguntas.pop()

            nodoA = Nodo(aux)

            if aux[0] == 'P':
                nodoA._izquierda = self.insertarNodos(listaPreguntas)
                nodoA._derecha = self.insertarNodos(listaPreguntas)

            return nodoA

        else:

            return None

    def obtener(self, respuesta=None, nodoActual=None):

        if nodoActual is None:
            nodoActual = self._raiz
            return nodoActual

        if respuesta == "S" or respuesta == "s":
            if nodoActual.izquierda() is None:
                return True
            else:
                return nodoActual.izquierda()
        elif respuesta == "N" or respuesta == "n":
            if nodoActual.derecha() is None:
                return False
            else:
                return nodoActual.derecha()

        return "none"



