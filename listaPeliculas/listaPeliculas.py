from .nodoPeliculas import NodoPeliculas

class ListaPeliculas:

    def __init__(self):
        self.Inicio = None
        self.Final = None

    def Insertar(self, Dato):
        NuevoNodo = NodoPeliculas(Dato)

        if self.Inicio == None:
            self.Inicio = NuevoNodo
            self.Final = NuevoNodo
        else:
            self.Final.SetSiguiente(NuevoNodo)
            self.Final = NuevoNodo

    def Pop(self):
        if self.Inicio != None:
            if self.Inicio.ObtenerSiguiente() == None:
                Auxiliar = self.Inicio
                self.Inicio = None
                self.Final = None
                return Auxiliar
            else:
                Auxiliar = self.Inicio
                self.Inicio = self.Inicio.ObtenerSiguiente()
                Auxiliar.SetSiguiente(None)
                return Auxiliar
            
            
    def EliminarElemento(self, Nombre):
        #indice será un valor numérico, que indica la posición de la lista a eliminar, la primera posición será 0
        if self.Inicio == None:
            print("La lista está vacía, no se puede eliminar nada.")
            return None
        if self.Inicio.Buscar(Nombre):
            Auxiliar = self.Pop()
            return Auxiliar
        Auxiliar = self.Inicio
        Auxliar2 = None
        while Auxiliar != None:
            if Auxiliar.Buscar(Nombre):
                if Auxiliar == self.Final:
                    self.Final = Auxliar2
                Auxliar2.SetSiguiente(Auxiliar.ObtenerSiguiente())
                Auxiliar.SetSiguiente(None)
                print("Se eliminó el elemento solicitado")
                return Auxiliar
            Auxliar2 = Auxiliar
            Auxiliar = Auxiliar.ObtenerSiguiente()
        print("No existe el elemento con ese filtro.")
        return None
    
    def ImprimirElmentos(self):
        if self.Inicio != None:
            Auxiliar = self.Inicio
            while Auxiliar != None:
                print("Nombre:",Auxiliar.ObtenerNombre(),"Indice:",Auxiliar.ObtenerIndice())
                Auxiliar = Auxiliar.ObtenerSiguiente()
        else:
            print("Lista Vacía")

    def obtenerElementos(self):
        if self.Inicio != None:
            Auxiliar = self.Inicio
            elemento = ""
            contador = 0
            while Auxiliar != None:
                contador += 1
                elemento += str(contador) + " - Nombre: " + str(Auxiliar.ObtenerNombre()) + "\n"
                Auxiliar = Auxiliar.ObtenerSiguiente()
            return elemento

    
    def buscarElmentos(self, peliID):
        if self.Inicio != None:
            Auxiliar = self.Inicio
            while Auxiliar != None:
                if Auxiliar.ObtenerID() == peliID:
                    return False
                Auxiliar = Auxiliar.ObtenerSiguiente()
            return True
        else:
            print("Lista Vacía")
            return True
            
    def buscarGenero(self, genero):
        if self.Inicio != None:
            Auxiliar = self.Inicio
            while Auxiliar != None:
                if Auxiliar.ObtenerGenero() == genero:
                    return False
                Auxiliar = Auxiliar.ObtenerSiguiente()
            return True
        else:
            print("Lista Vacía")
            return True
        
    def buscarGenero(self, genero):
        Texto = ""
        if self.Inicio != None:
            Auxiliar = self.Inicio
            while Auxiliar != None:
                if Auxiliar.ObtenerGenero() == genero:
                    Texto += "ID: " + str(Auxiliar.ObtenerID()) + ", Nombre: " + str(Auxiliar.ObtenerNombre()) + "\n"
                Auxiliar = Auxiliar.ObtenerSiguiente()
            return Texto
        else:
            print("Lista Vacía")
    
    def cambiarDato(self, PeliID, nombre, genero):
        if self.Inicio != None:
            Auxiliar = self.Inicio
            while Auxiliar != None:
                if Auxiliar.ObtenerID() == PeliID:
                    Auxiliar.setNombre(nombre)
                    Auxiliar.setGenero(genero)
                Auxiliar = Auxiliar.ObtenerSiguiente()
        else:
            print("Lista Vacía")

    def InicializarSistema(self):
        self.Inicio = None
        self.Final = None
        self.Contador = 0
