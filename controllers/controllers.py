import xml.etree.ElementTree as ET
import json
import listaPeliculas.datoPelicula as datoPelicula
import listaPeliculas.listaPeliculas as listaPeliculas
global listaPelis
listaPelis = listaPeliculas.ListaPeliculas()
        
def agregarPelicula(doc):
    global listaPelis
    doc = str(doc, "utf-8")
    infor = json.loads(doc)
    peliculaID = infor["movieId"]
    nombre = infor["name"]
    genero = infor["genre"]
    if listaPelis.buscarElmentos(peliculaID):
        pelicula = datoPelicula.datoPelicula(peliculaID, nombre, genero)
        listaPelis.Insertar(pelicula)
        return(
     '''{
         "Codigo":201,
         "Mensaje": "Se agregó la pelicula: ''' + str(nombre) + ''', con el id: ''' + str(peliculaID) + ''', y el genero: '''+ str(genero) +'''"
        }'''
     )
    else:
        return(
     '''{
         "Codigo":200,
         "Mensaje": "El ID ya esta en uso"
        }'''
     )
    
def MostrarPorGenero(genero):
    global listaPelis
    if listaPelis.buscarElmentos(genero):
        Texto = str(listaPelis.buscarGenero(genero))
        print(Texto)
        return(
    '''{
         "Codigo":201,
         "Mensaje": "Películas con el género ''' + genero + '''",
         "Lista": '''+'''\n'''+Texto+'''
        }'''
        )
    else:
        return(
    '''{
         "Codigo":200,
         "Mensaje": "El genéro no existe"
        }''')

def editarPelicula(doc):
    global listaPelis
    doc = str(doc, "utf-8")
    infor = json.loads(doc)
    peliculaID = infor["movieId"]
    nombre = infor["name"]
    genero = infor["genre"]
    if listaPelis.buscarElmentos(peliculaID):
        return(
     '''{
         "Codigo":200,
         "Mensaje": "El ID no existe"
        }'''
     )
    else:
        listaPelis.cambiarDato(peliculaID, nombre, genero)
        return(
     '''{
         "Codigo":201,
         "Mensaje": "Se Editó la pelicula: ''' + str(nombre) + ''', con el id: ''' + str(peliculaID) + ''', y el genero: '''+ str(genero) +'''"
        }'''
     )
        