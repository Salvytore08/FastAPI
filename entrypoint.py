from fastapi import FastAPI

app = FastAPI()

@app.get('/hola/{nombre}')
def hola(nombre):
    return f'Hola {nombre}'


@app.get('/adios')
def adios():
    return 'Adiós mundo'


@app.get('/mañana')
def hola():
    return 'Buenos días'


@app.get('/tarde')
def adios():
    return 'Buenas tardes'


@app.get('/noche')
def hola():
    return 'Buenas noches'

