from flask import Flask, Response,request, jsonify
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import json

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/projeto'

db = SQLAlchemy(app)

class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(50))
    data_de_nascimento = db.Column(db.String(10))
    endereco = db.Column(db.String(100))
    cpf = db.Column(db.String(15))
    civil = db.Column(db.String(50))

    def to_json(self):
        return {"id":self.id, "nome":self.nome, "data_de_nascimento": self.data_de_nascimento,"endereco": self.endereco, "cpf": self.cpf, "civil":self.civil}

with app.app_context():
    db.create_all()

#selecionar tudo
@app.route('/pessoas', methods=["GET"])
def seleciona_pessoas():
    try:
        pessoas_classe = Pessoa.query.all()
        pessoas_json = [pessoas.to_json() for pessoas in pessoas_classe]
        mensagem = 'Operação concluida com sucesso'
        status = 200

    except Exception as e:
        mensagem = 'Erro ao concluir operação' + str(e)
        status = 500

    return jsonify({"status": status, "mensagem":mensagem, "pessoas":pessoas_json}), status

#selecionar individual
@app.route('/pessoas/<id>',methods=["GET"])
def seleciona_usuario(id):
    try:
            pessoa_classe = Pessoa.query.filter_by(id=id).first()
            pessoa_json = pessoa_classe.to_json()
            mensagem = 'Operação concluida com sucesso'
            status = 200
    except Exception as e:
            mensagem = 'Erro ao concluir operação' + str(e)
            status = 500

    return jsonify({"status": status, "mensagem": mensagem, "pessoa": pessoa_json}), status

#cadastrar
@app.route("/cadastro", methods=["POST"])
def cria_pessoa():
    try:
        body = request.get_json()
        pessoa = Pessoa(nome=body["nome"], data_de_nascimento=body["data_de_nascimento"], endereco=body["endereco"], cpf=body["cpf"],civil=body["civil"])
        db.session.add(pessoa)
        db.session.commit()
        mensagem = 'Pessoa cadastrada com sucesso'
        status = 201
    except Exception as e:
        mensagem = 'Erro ao cadastrar pessoa'
        status = 400
    return jsonify({"mensagem": mensagem}), status

#atualizar
@app.route("/atualizar/<id>", methods=["PUT"])
def atualiza_pessoa(id):
    try:
        pessoa_classe = Pessoa.query.filter_by(id=id).first()


        if pessoa_classe:
            body = request.get_json()
            if 'nome' in body:
                pessoa_classe.nome = body['nome']

            if'data_de_nascimento' in body:
                pessoa_classe.data_de_nascimento = body['data_de_nascimento']
            if'endereco' in body:
                pessoa_classe.endereco = body['endereco']
            if'cpf' in body:
                pessoa_classe.cpf = body['cpf']
            if'civil' in body:
                 pessoa_classe.civil = body['civil']

            db.session.commit()
            mensagem = 'Pessoa atualizada com sucesso'
            status = 200

        else:
            mensagem = 'Pessoa não localizada'
            status = 404

    except Exception as e:
        mensagem = 'Erro ao atualizar pessoa'
        status = 400

    return jsonify({'mensagem': mensagem, 'pessoa': pessoa_classe.to_json()}), status

#deletar
@app.route('/deletar/<id>', methods=["DELETE"])
def deleta_pessoa(id):
    try:
        pessoa_classe = Pessoa.query.filter_by(id=id).first()
        if pessoa_classe:
            db.session.delete(pessoa_classe)
            db.session.commit()
            mensagem = 'Pessoa deletada com sucesso'
            status = 200
        else:
            mensagem = 'Pessoa não encontrada'
            status = 404

    except Exception as e:
        mensagem = 'Erro ao deletar usuario'
        status = 500

    return jsonify({'mensagem': mensagem}), status
app.run()


