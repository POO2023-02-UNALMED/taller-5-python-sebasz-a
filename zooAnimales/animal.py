class Animal:
    _totalAnimales = 0
    def __init__(self, nombre, edad, habitat, genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = []
        Animal._totalAnimales += 1

    def movimiento():
        pass
    @classmethod
    def totalPorTipo(cls):
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.ave import Ave
        from zooAnimales.reptil import Reptil
        from zooAnimales.pez import Pez
        from zooAnimales.anfibio import Anfibio
        return f"Mamiferos: {Mamifero.cantidadMamiferos()}\nAves: {Ave.cantidadAves()}\nReptiles: {Reptil.cantidadReptiles()}\nPeces: {Pez.cantidadPeces()}\nAnfibios: {Anfibio.cantidadAnfibios()}"
    def toString(self):
        if len(self._zona) == 0:
            return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"
        else:
            return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}, la zona en la que me ubico es {self._zona[0]}, en el {self._zona[0].getZoo()}"
        
    def getNombre(self):
        return self._nombre
    def setNombre(self, nombre):
        self._nombre = nombre
    def getEdad(self):
        return self._edad
    def setEdad(self, edad):
        self._edad = edad
    def getHabitat(self):
        return self._habitat
    def setHabitat(self, habitat):
        self._habitat = habitat
    def getGenero(self):
        return self._genero
    def setGenero(self, genero):
        self._genero = genero
    def getZona(self):
        return self._zona
    def setZona(self, zona):
        self._zona = zona
    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales
    @classmethod
    def setTotalAnimales(cls, totalAnimales):
        cls._totalAnimales = totalAnimales