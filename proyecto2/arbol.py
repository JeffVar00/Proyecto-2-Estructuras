from nodo import Nodo

class Arbol:

    def __init__(self, raiz=None, actual=None):
        self._raiz = raiz
        self._actual = actual
        self._contador = 0
        self._altura = 0
        self._tamanno = 0

    def recorrer(self):
        pass

    def Vacio(self, nodo):
        if nodo is None:
            return True
        return False

    def EsHoja(self, nodo):
        if nodo.izquierda() is None and nodo.derecha() is None:
            return True
        return False

    def insertar(self, dato):

        padre = None
        self._actual = self._raiz

        while self.Vacio(self._actual) is not True and dato != self._actual.dato():
            padre = self._actual
            if dato > self._actual.dato():
                self._actual = self._actual.derecha()
            elif dato < self._actual.dato():
                self._actual = self._actual.izquierda()

        if self.Vacio(self._actual) is not True:
            return
        if self.Vacio(padre) is True:
            self._raiz = Nodo(dato)
            self._tamanno += 1
        elif dato < padre.dato():
            padre._izquierda = Nodo(dato)
            self._tamanno += 1
        elif dato > padre.dato():
            padre._derecha = Nodo(dato)
            self._tamanno += 1

    def obtener(self, respuesta=None, nodoActual=None):

        if nodoActual is None:
            nodoActual = self._raiz
            return nodoActual

        if respuesta == "S":
            if nodoActual.izquierda() is None:
                return True
            else:
                return nodoActual.izquierda()
        elif respuesta == "N":
            if nodoActual.derecha() is None:
                return False
            else:
                return nodoActual.derecha()



