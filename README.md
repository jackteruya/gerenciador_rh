Para ambiente linux.

Com do docker instaldo, caso não tenha -> https://docs.docker.com/engine/install/ e https://docs.docker.com/compose/install/

Primeiro passo, altere o arquivo env.tex para .env;


Para rodar a aplicação, no docker-compose.yml para subir um container, no terminal.

    $ docker-compose up



Ou caso não tenha o docker instalado, mas será necessario ter o python instalado, de preferencia a versão 3.11:
    
    1-Craindo o ambiente:
        $ python -m venv .venv

    2-Ativando o ambiente no linux:
        $ source .venv/bin/activate

    3-Instalando os requisitos:
        $ pip install -r requierements.txt

    4-Rodar a aplicação django, (sera htt:/http://127.0.0.1:8000/)
        $ python manage.py runserver

    5-Teste unitario:
        $ pytest
    
    6-Usuario para autenticação:
        username: admin
        password: 123456