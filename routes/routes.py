from controllers.controllers import *
from flask import Blueprint, jsonify, Response, request

RutasSaludos = Blueprint("RutasSaludos", __name__)

@RutasSaludos.route("/api/new-movie", methods=["POST"])
def new_movie():
    print(request.data)
    variable = agregarPelicula(request.data)
    print(variable)
    return Response(variable, status=201, mimetype="json") 

@RutasSaludos.route("/api/all-movies-by-genre/<genero>", methods=["GET"])
def SaludoParams(genero):
    print(genero)
    variable = MostrarPorGenero(genero)
    return Response(variable, status=201, mimetype="json") 

@RutasSaludos.route("/api/update-movie", methods=["PUT"])
def update_movie():
    print(request.data)
    variable = editarPelicula(request.data)
    print(variable)
    return Response(variable, status=201, mimetype="json") 