from abc import ABC, abstractmethod


class AbstracaoDeServicos(ABC):

    @abstractmethod
    def request(self) -> None: # Implementa as funcionalidades que vai precisar realmente de um controle.
        pass


class Servico(AbstracaoDeServicos):

    def request(self) -> None:
        print("Trabalhando...")


class Proxy(AbstracaoDeServicos):
    
    def __init__(self, servico: Servico) -> None:
        self._real_subject = servico

    def request(self) -> None:

        if self.acesso():
            self._real_subject.request()
            self.logs()

    def acesso(self) -> bool:
        print("Proxy: Verificando credenciais.")
        return True

    def logs(self) -> None:
        print("Proxy: Logging requisitado.", time="")
