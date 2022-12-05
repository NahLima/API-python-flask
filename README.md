# API-python-flask

**Este projeto faz parte do desafio BackEnd Telavita.**

**Sobre o projeto:**
- Solicitações HTTP com Connexion
- Endpoints de API usando a especificação OpenAPI
- Documentação de API com Swagger UI

obs: _O projeto foi realizado com um PC windows._


Para conseguir rodar o projeto em sua máquina é preciso criar o ambiente virtual, em algumas máquinas é necessário colocar **python3** ao invés de somente **python**, 
aqui vou manter somente python, caso perceba que não funciona com o seu computador tentar com python3.

```console
 python -m venv myvenv  # cria o ambiente 
 
 ./myvenv/Scripts/activate # ativa o ambiente no windows 
 
 source myvenv/bin/activate # ativa o ambiente no MAC 
```

Instalar as dependências do  `requirements.txt`:

```console
(myvenv)  python -m pip install -r requirements.txt
```
Se der problemas para instalar com o requirements rodar os comandos abaixo com a myvenv habilitada

```console
(myvenv) python -m pip install flask

(myvenv) python -m pip install "connexion[swagger-ui]==2.14.1"

(myvenv) python -m pip install "flask-marshmallow[sqlalchemy]==0.14.0"

(myvenv) python pip install pytest
```

Na pasta `API_python_flask/`  inicie o web server:

```console
(myvenv)  python app.py 
```

Você verá a home page em: `http://127.0.0.1:8000`

A página com o Swagger UI API em: `http://127.0.0.1:8000/api/ui`

### Banco de dados

![painel](https://raw.githubusercontent.com/NahLima/API-python-flask/main/imgs/BD.png)

**_A  etapa abaixo só é necessária caso o BD não funcione_**

Se você não tiver em seu computador o Sqlite será necessário baixar e intalar o mesmo.

link https://www.sqlite.org/index.html

No diretório: `API-python-flask/banco_de_dados/` contém os arquivos do BD.

Após rodar a aplicação, abrir o  SQLite e importar o arquivo : `api_flask.db`
ou criar um novo caso seja necessário. 

````
# para abrir o arquivo 

CRTL + O = abre uma janela para importar o arquivo 
clicar em test conection 
````
![painel](https://raw.githubusercontent.com/NahLima/API-python-flask/main/imgs/painel1.JPG)

````
# para criar um arquivo novo é só clicar no + e colocar um nome

````

Se criado um novo arquivo, é necessário rodar os comandos, que estão no arquivo `create_data_base.sql`
- verificar se você está no BD correto e só depois rode os comandos!

Para validar você pode rodar os comandos que estão no arquivo `queries.sql`

### Para rodar os testes
````console
(myvenv)  python -m pytest 
````

### Possíveis erros

Caso  você receba algum erro referente ao Dll

``ImportError: DLL load failed: The specified module could not be found.``

Aqui tem uma possível solução:
https://stackoverflow.com/questions/54876404/unable-to-import-sqlite3-using-anaconda-python
