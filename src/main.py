# -*- coding: UTF-8 -*-
#limapercia.main.py
"""Tutoria dois - brincando de git

..codeautor:: Autor: Isabel Hortencia <hortencia.garnica@nce.ufrj.br>

. Como criar um repositorio no github
. como clonar usando o comando git
. como commitar usando o comando git

Classes neste modulo:

    :py:class: 'Main' exemplos de classe qualquer.

Changelog
---------
..versionadded::    20.07
       Documentacao do tutorial.
"""

class Main:
    """classe exemplo.

         :param versao: versao deste exemplo.

    """
    def __init__(self, versao="20.07"):
        self.versao = versao
        print("classe exemplo, versao{}".format(versao))

    def get_versao(self):
        return self.versao


if __name__ == "__main__":
    print(Main().get_versao())