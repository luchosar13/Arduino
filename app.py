from flask import Flask

from conexion import conect_to_db, db_params

app = Flask('Api Test')

@app.route('/', methods=['GET', 'POST', 'PUT'])
def index():
    return 'Hola Mundo desde Flask Server'

@app.route('/conect')
def conect():
    conect_to_db(db_params)
    return 'Connected to the database'

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
