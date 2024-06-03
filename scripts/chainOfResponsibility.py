from __future__ import annotations
from abc import ABC, abstractmethod

class Manipulador(ABC): # A cadeia de responsabilidade é muito eficiente para validar os dados de cada parte,
    # sendo assim o conceito geral é criar os Handlers para passar por vários testes até ter a certeza de que está tudo ok.
    
    @abstractmethod
    def proxManipulacao(self, manipulador: Manipulador) -> Manipulador:
        pass
    
    @abstractmethod
    def manipulador(self, request):
        pass

class ManipuladorAbstrato():
    _proxManipulacao: Manipulador = None

    def proxManipulacao(self, manipulador: Manipulador):
        pass
    
    @abstractmethod
    def manipulador(self, request):
        if self._proxManipulacao:
            return self._proxManipulacao.manipulador(request)

        return None


