# importa as classes para se organizar aqui

class Facade():

    _list = None
    def __init__(self) -> None:
        self._list = []

    @property # pegar a lista - Get
    def list(self):
        return self._list
    
    @list.setter # setar a lista
    def list(self, args: list):
        self._list = args

    @property #Deletar a lista
    def listDel(self):
        self._list = None

    # Com essas funções podemos manipular listas de informações sem 
    #o código principal saber o que está acontecendo e quais classes está utilizando.