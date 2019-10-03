from flask import Flask

nome='novo_projeto_web'

app = Flask(__name__)
@app.route('/') 
def inicio(): 
    return ('<h1> {} </h1>'.format(nome))
app.run()