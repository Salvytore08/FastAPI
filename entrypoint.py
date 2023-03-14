from fastapi import FastAPI
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

@app.get('/{id}')
def usuario(id:str):
   return biblioteca[id]


@app.get('/{id}/{idlib}')
def libro(id:str, idlib:str):
   return biblioteca[id]["LIBROS"][idlib]



