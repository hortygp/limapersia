# -*- coding: UTF-8 -*-

"""Tutoria dois - brincando de git
..codeautor:: Autor: Isabel Hortencia <hortencia.garnica@nce.ufrj.br>
. Como criar um repositorio no github
. como clonar usando o comando git
. como commitar usando o comando git

sem classes neste modulo:

Changelog
---------
..versionadded::    20.07
       Adiciona o gerenciador de chamadas http via bottle
"""
from bottle import default_app, route


@route('/')
def hello_world():
    return 'Tutorial 2 aprendendo Git e Bottle!'

@route('/oi')
def oi_mundo():
    return 'Tutorial 2 ensaiando uma nova rota'
application = default_app()

