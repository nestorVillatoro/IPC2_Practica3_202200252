class NodoPeliculas:

    def __init__(self, Dato):
        self.Dato = Dato
        self.Siguiente = None

    
    def ObtenerNombre(self):
        return self.Dato.ObtenerNombre()
    
    def ObtenerID(self):
        return self.Dato.ObtenerPeliID()
    
    def setNombre(self, nuevoNombre):
        return self.Dato.setNombre(nuevoNombre)
    
    def setGenero(self, nuevoGenero):
        return self.Dato.setGenero(nuevoGenero)
    
    def ObtenerGenero(self):
        return self.Dato.ObtenerGenero()
    
    def ObtenerSiguiente(self):
        return self.Siguiente
    
    def SetSiguiente(self, NodoS):
        self.Siguiente = NodoS

    def Buscar(self, Nombre):
        return self.Dato.EncontroNombre(Nombre)
    
    def AsignarSiguiente(self, valorsiguiente):
        self.Siguiente = valorsiguiente

    def ObtenerDato(self):
        return self.Dato
    
    def CambiarDato(self, NuevoDato):
        self.Dato = NuevoDato