# 1.-Implementacion de estilos de Programacion
## Array 
En la implementación de Modelo Candidato/backend/models/asistente.py
Toda la información recibida desde la base de datos se almacena en arreglos. 
```
# array
from backend.models.connection_pool import MySQLPool
class AsistenteModel:
    def __init__(self):
        self.mysql_pool = MySQLPool()

    def get_asistente(self, id):
        params = {'id': id}
        rv = self.mysql_pool.execute("SELECT * from usuario INNER JOIN asistente ON where asistente.id%(id)s=usuario.id%(id)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id': result[0], 'nombre': result[1], 'apellido': result[2], 'correo': result[3]}
            data.append(content)
            content = {}
        return data
    def get_all_asistentes(self):
        rv = self.mysql_pool.execute("select * from usuario")
        data = []
        content = {}


    def create_asistente(self, id, nombre, apellido, correo):

    def delete_asistente(self, id)
```

## Things
Constraints:

- The larger problem is decomposed into 'things' that make sense for the problem domain
- Each 'thing' is a capsule of data that exposes procedures to the rest of the world
- Data is never accessed directly, only through these procedures
- Capsules can reappropriate procedures defined in other capsules

En la implementación de Evento.py, la data nunca se accede de forma directa. Se utilizan setters y getters. 

```
#!/usr/bin/python
#-*- coding: utf-8 -*-
# Things
class Evento:
    def __init__(self, _id, _nombre, _apellidos, _correo):
        self.id          = _id
        self.nombre      = _nombre
        self.apellidos   = _apellidos
        self.correo      = _correo
    def get_nombre(self):
        return self.nombre
    def get_apellidos(self):
        return self.apellidos
    def get_correo(self):
        return self.correo
    def set_nombre(self, _nombre):
        self.nombre = _nombre
    def set_apellidos(self, _apellidos):
        self.apellidos = _apellidos
    def set_correo(self, _correo):
        self.correo = _correo
```

## Passive-Agressive

Constraints:

- Every single procedure and function checks the sanity of its arguments and refuses to continue when the arguments are unreasonable, jumping out of the function
- When calling out other functions, program functions only check for errors if they are in a position to react meaningully
- Error handling occurs at higher levels of function call chains, wherever it is meaningul to do so

En la clase Lista_de_eventos.py, el manejo de errores se realize mediante asserts. 
Cada función comprueba la validez de sus argumentos. 
```
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
```

# 2.-Implementacion de practicas de codificacion legible
## Function rules - Use descriptive names
Cada función describe su funcionamiento, implementación en Evento.py
```
class Evento:
    def __init__(self, _id, _nombre, _apellidos, _correo):
        self.id          = _id
        self.nombre      = _nombre
        self.apellidos   = _apellidos
        self.correo      = _correo
    def get_nombre(self):
        return self.nombre
    def get_apellidos(self):
        return self.apellidos
    def get_correo(self):
        return self.correo
    def set_nombre(self, _nombre):
        self.nombre = _nombre
    def set_apellidos(self, _apellidos):
        self.apellidos = _apellidos
    def set_correo(self, _correo):
        self.correo = _correo
```
## Source code structure - Don't break indentation
La indentación en Python va más allá de la legibilidad, puede incluso traer errores de sintaxis. 
## Source code structure - Place functions in a downward direction.
Todas las funciones están definidas en un mismo nivel (indentación). 
Implementación en Modelo Candidato/backend/models/escuela_model.py
```
class EscuelaModel:
    def __init__(self):
        self.mysql_pool = MySQLPool()

    def get_escuela(self,idEscuela):
        params = {'idEscuela' : idEscuela}
        rv = self.mysql_pool.execute("SELECT * from escuela where idEscuela=%(idEscuela)s",params)
        data = []
        content = {}
        for result in rv:
            content = {'idEscuela': result[0], 'escuela':result[1], 'anio': result[2], 'numero_estudiantes': result[3]}
            data.append(content)
            content = {}
        return data

    def get_all_escuela(self):#Obtener todos los datos 
        rv = self.mysql_pool.execute("SELECT * from escuela")  
        data = []
        content = {}
        for result in rv:
            content = {'idEscuela': result[0], 'escuela': result[1], 'anio': result[2], 'numero_estudiantes': result[3]}
            data.append(content)
            content = {}
        return data

    def create_escuela(self, idEscuela, escuela, anio, numero_estudiantes):#Se envian los parametros a traves del formato JSON 
        params = {
            'idEscuela' : idEscuela,
            'escuela' : escuela,
            'anio' : anio,
            'numero_estudiantes' : numero_estudiantes
        }
        query = """insert into escuela (idEscuela, escuela,anio,numero_estudiantes)
            values (%(idEscuela)s,%(escuela)s,%(anio)s,%(numero_estudiantes)s)"""
        cursor = self.mysql_pool.execute(query, params, commit=True)

        data = {'idEscuela': cursor.lastrowid, 'escuela': escuela, 'anio': anio, 'numero_estudiantes': numero_estudiantes}
        return data

    def delete_escuela(self, idEscuela):#Se envia el IdEscuela con la que se identifica para eliminar no se necesita mas
        params = {'idEscuela': idEscuela}
        query = """delete from escuela where idEscuela = %(idEscuela)s"""    
        self.mysql_pool.execute(query, params, commit=True)  
        data = {'result': 1}
        return data
```
## Source code structure - Similar functions should be close
Las funciones parecidas están implementadas cerca una de las otras. 
Implementación en Evento.py, todos los getters y setters se encuentran agrupados. 
```
class Evento:
    def __init__(self, _id, _nombre, _apellidos, _correo):
        self.id          = _id
        self.nombre      = _nombre
        self.apellidos   = _apellidos
        self.correo      = _correo
    def get_nombre(self):
        return self.nombre
    def get_apellidos(self):
        return self.apellidos
    def get_correo(self):
        return self.correo
    def set_nombre(self, _nombre):
        self.nombre = _nombre
    def set_apellidos(self, _apellidos):
        self.apellidos = _apellidos
    def set_correo(self, _correo):
        self.correo = _correo
```
## Objects and data structures - Prefer non-static methods to static methods.
Hasta el momento no se utilizaron métodos static. 
```
class AsistenteModel:
    def __init__(self):
        self.mysql_pool = MySQLPool()

    def get_asistente(self, id):
        params = {'id': id}
        rv = self.mysql_pool.execute("SELECT * from usuario INNER JOIN asistente ON where asistente.id%(id)s=usuario.id%(id)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id': result[0], 'nombre': result[1], 'apellido': result[2], 'correo': result[3]}
            data.append(content)
            content = {}
        return data
    def get_all_asistentes(self):
        rv = self.mysql_pool.execute("select * from usuario")
        data = []
        content = {}
        

    def create_asistente(self, id, nombre, apellido, correo):

    def delete_asistente(self, id)
```
# 3.-Aplicacion de principios SOLID
