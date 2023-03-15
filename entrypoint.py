from fastapi import FastAPI
from pydantic import BaseModel

class PerBiblioteca(BaseModel):
    id:str
    nombre:str
    edad:int
    libros:dict
    
app = FastAPI()

biblioteca = {
    
    '1' : {
        'NOMBRE' : 'Salvatore',
        'EDAD' : 14,
        'LIBROS': {
            '1':{
            'NOMBRE': 'Hábitos Atómicos',
            'FECHA': '5/02/2023',
            'ESTADO': 'Prestado'
            },
            '2':{
            'NOMBRE': 'Principito',
            'FECHA': '6/04/2022',
            'ESTADO': 'Prestado'
            }
        }
    },
    
    '2' : {
        'NOMBRE' : 'Gabriela',
        'EDAD' : 17,
        'LIBROS': {
            '1':{
            'NOMBRE': 'Hábitos Atómicos',
            'FECHA': '5/02/2023',
            'ESTADO': 'Prestado'
            },
            '2':{
            'NOMBRE': 'Principito',
            'FECHA': '6/04/2022',
            'ESTADO': 'Prestado'
            }
        }
    }
}

@app.get('/')
def check():
   return {
       'Título' : 'Biblioteca STEAM ACADEMY',
       'Versión' : 'v 0.0.1'
   }


@app.get('/personas')
def todos():
   return biblioteca


@app.get('/personas/{id}')
def uno(id:str):
    if id not in biblioteca:
        return 'El usuario no se encuentra disponible'
    else:
        return biblioteca[id]


@app.post('/personas/{id}/agregar')
def uno_mas(request:PerBiblioteca):
    biblioteca.update({request.id : request})
    return 'El usuario se ha agregado correctamente'


@app.delete('/personas/{id}/eliminar')
def uno_menos(id:str):
    if id not in biblioteca:
        return 'El usuario no se encuentra disponible'
    else:
        biblioteca.pop(id)
        return 'El usuario se ha eliminado correctamente'


@app.put('/personas/{id}/cambiar')
def uno_diferente(id:str, NewNom:str, NewEdad:int):
    nuevo = {
        'NOMBRE': NewNom,
        'EDAD' : NewEdad,
        'LIBROS' : biblioteca[id]['LIBROS']
        }
    biblioteca.update({id:nuevo})
    return 'Tu usuario se ha cambiado correctamente'


@app.put('/personas/{id}/devolverLib')
def devolver_libro(id:str, IdLib:str):
    biblioteca[id]['LIBROS'][IdLib]['ESTADO'] = 'Devuelto'
    return 'El libro se ha devuelto correctamente'