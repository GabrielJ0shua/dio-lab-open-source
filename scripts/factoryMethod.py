from abc import ABC, abstractmethod # O abstract serve para delegar para criar a propriedade de gerador de instancias


class Creator(ABC):
    @abstractmethod
    def produto(self):
        #Aqui fica a geração de instancias do nosso produto.
        pass

    def outrasOperacoes(self) -> str:
        return "Aqui deixa a sua criatividade fluir também"
    

class ConcreteCreator1(Creator):

    def produto(self, args) -> Algo:
        return AlgumaClasse(args)