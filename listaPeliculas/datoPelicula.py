class datoPelicula:

    def __init__(self, peliID, nombre, genero):
        self.PeliID = peliID
        self.Nombre = nombre
        self.Genero = genero

    def ObtenerPeliID(self):
        return self.PeliID
    
    def ObtenerNombre(self):
        return self.Nombre
    
    def ObtenerGenero(self):
        return self.Genero
    
    def setNombre(self, nuevoNombre):
        self.Nombre = nuevoNombre

    def setGenero(self, nuevoGenero):
        self.Genero = nuevoGenero
