#!/usr/bin/python
#-*- coding: utf-8 -*-
# passive-agressive
class Lista_de_eventos:
    def __init__(self):
        self.id_evento = None
    def setDetalles(evento, detalles_):
        assert(type(detalles_) is str), "Los detalles deben estar contenidos en un string"
        evento.detalles = detalles_
    def setLink(evento, link_):
        assert("www" in link_), "El link debe contener 'www'"
        evento.link = link_
    def setId(evento, id_): 
        assert(type(id_) is int ), "El id debe ser un entero"
        evento.id = id_
    def setNombre(evento, nombre_):
        assert(type(nombre_) is str), "El nombre debe ser un string"
        evento.nombre = nombre_
    def setFecha(evento, fecha_):
        assert(type(fecha_) is str), "La fecha debe ser un string"
        evento.fecha = fecha_
    def setHoraInicio(evento, hora_inicio_):
        assert(type(hora_inicio_) is str), "La hora de inicio debe ser un string"
        evento.hora_inicio = hora_inicio_
    def setHoraFin(evento, hora_fin_):
        assert(type(hora_fin_) is str), "La hora de fin debe ser un string"
        evento.hora_fin = hora_fin_

