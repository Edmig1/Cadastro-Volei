from flask import Flask, render_template, request, redirect
id = 0
app = Flask(__name__)
class player():
    def __init__(self,nome,jogo,rank,posicao,img,num):
        self.nome = nome
        self.jogo = jogo
        self.rank = rank
        self.posicao = posicao
        self.img = img
        self.num =num

@app.route('/')
def esports():

    return render_template('Times.html',Titulo ='Volei Cadastro', listatimes = lista)


@app.route('/cadastro')
def cadastro():

    return render_template('Cadastro.html',Titulo ='Volei Cadastro')

@app.route('/criar',methods = ['POST'])
def criar():
    global id
    nome = request.form['nome']
    jogo= request.form['jogo']
    rank = request.form['rank']
    posicao = request.form['posicao']
    img = request.form['img']
    id+=1
    obj = player(nome,rank,jogo,posicao,img,id)
    lista.append(obj)
    return redirect('/')

@app.route('/excluir/<idplayer>',methods = ['GET','DELETE'])
def excluir(idplayer):
    for i, p in enumerate(lista):
        if p.num == int(idplayer):
            lista.pop(i)
            break
    return redirect('/')

@app.route('/editar/<idplayer>',methods = ['GET'])
def editar(idplayer):
    for i, p in enumerate(lista):
        if p.num == int(idplayer):
            return render_template('Editar.html', player=p, Titulo='Alterar Player')
@app.route('/alterar', methods = ['POST','PUT'])
def alterar():
    id = request.form ['id']
    for i, p in enumerate(lista):
        if p.num == int(id):
            p.nome = request.form['nome']
            p.jogo = request.form['jogo']
            p.rank = request.form['rank']
            p.posicao = request.form['posicao']
            p.img = request.form['img']
    return redirect('/')
lista = []
if __name__ == '__main__':
    app.run()