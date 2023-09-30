# Autora: Tainara Mello

Sejam bem vindos!!

Projeto desenvolvido em Python, utilizando framework Flask. Utilizando banco de dados MySql Workbench

# Execução
Projeto testado no Insomnia.
CRUD completo com Cadastro, Lista, Delete e Atualização

### Fazer o clone do repositorio
### Rodar o cod no Pycharm para que fique disponível no localhost da máquina
	python versão 3.11.5
 baixar dependências
 
 	pip install flask
  	pip install flask_sqlalchemy
   	pip install mysql-connector-python
    	pip install mysqlclient
    	
### Usar o tester de sua preferência 

## http://127.0.0.1:5000/cadastro URL DE CADASTRO 

	"nome": "",
	"data_de_nascimento": "",
	"endereco": "",
	"cpf": "",
	"civil": ""

 ## http://127.0.0.1:5000/deletar/ID URL DO DELETE
 Inserir o ID que deseja deletar na url
 
	"mensagem": "Pessoa deletada com sucesso"

## http://127.0.0.1:5000/atualizar/ID URL ATUALIZAR
Inserir o ID que deseja atualizar + o campo que irá atualizar

			"civil": "Atualização",
			"nome": "Atualização "

## http://127.0.0.1:5000/pessoas LISTAR TUDO
Retorno da lista total no banco de dados.
		
 

