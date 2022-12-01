# API-python-flask

### Este projeto faz parte do desafio BackEnd Telavita.

_O projeto foi realizado com um PC windows._

Para conseguir rodar o projeto em sua máquina é preciso criar o ambiente virtual:

```console
$ python -m venv myvenv
$ source myvenv/bin/activate
```

Instalar as dependências do  `requirements.txt`:

```console
(myvenv) $ python -m pip install -r requirements.txt
```

Na pasta `API_python_flask/`  inicie o web server:

```console
(myvenv) $ python app.py 
```

Você verá a  home page em: `http://127.0.0.1:8000`

A página com o  Swagger UI API em: `http://127.0.0.1:8000/api/ui`

### Banco de dados

Se você não tiver em seu computador o Sqlite será necessário baixar e intalar o mesmo.

link https://www.sqlite.org/index.html

No diretório: `API-python-flask/banco_de_dados/` contém os arquivos do BD.

Após rodar a aplicação, abrir o  SQLite e importar o arquivo : `api_flask.db`

````
CRTL + O = abre uma janela para importar o arquivo 
clicar em test conection 
````
![painel](imgs\painel1.JPG )


Depois é necessário rodar os comandos, que estão no arquivo `create_data_base.sql`
- verificar se você está no BD correto e só depois rode os comandos!

Para validar você pode rodar os comandos que estão no arquivo `queries.sql`



### Possíveis erros

Caso  você receba algum erro referente ao Dll

``ImportError: DLL load failed: The specified module could not be found.``

Aqui tem uma possível solução:
https://stackoverflow.com/questions/54876404/unable-to-import-sqlite3-using-anaconda-python
