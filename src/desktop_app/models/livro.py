from datetime import date
from desktop_app.models.editora import Editora
from desktop_app.utils import validate as val

class Livro:
    __ISBN: str
    __Titulo: str
    __idioma: str
    __tipo: list
    __tema: list
    __data_publicacao: int
    __editora: Editora | None
    __disponivel: str

    _by_ISBN: dict[str, "Livro"] = {}

# Constructores
    def __init__(self, ISBN, Titulo, idioma, tipo, tema, data_publicacao, editora: Editora | None, disponivel: str = "disponivel"):
        self.__ISBN = ISBN
        self.__Titulo = Titulo
        self.__idioma = idioma
        self.__tipo = tipo
        self.__tema = tema
        self.__data_publicacao = data_publicacao
        self.__editora = editora
        self.__disponivel = disponivel

    def to_dict(self):
        return {
            "ISBN": self.ISBN, 
            "Titulo": self.Titulo, 
            "Idioma": self.Idioma, 
            "Tipo": self.Tipo, 
            "Tema": self.Tema, 
#            "Data_Publicacao": self.Data_Publicacao.strftime("%d-%m-%Y"), 
            "Data_Publicacao": self.Data_Publicacao,
            "Editora": self.Editora,
            "Disponivel": self.Disponivel,
        }

    @classmethod
    def _create_unique(cls, ISBN, Titulo, idioma, tipo, tema, data_publicacao, editora, disponivel="disponivel"):
        if ISBN in cls._by_ISBN:
            raise ValueError(f"Livro com ISBN {ISBN} já existe.")
        obj = cls(ISBN, Titulo, idioma, tipo, tema, data_publicacao, editora, disponivel)
        cls._by_ISBN[ISBN] = obj
        return obj

    @classmethod
    def from_dict(cls, d):
        return cls(
            d["ISBN"], 
            d["Titulo"], 
            d["Idioma"], 
            d["Tipo"], 
            d["Tema"], 
            d["Data_Publicacao"], 
            d["Editora"],
            d.get("Disponivel", "disponivel"),
        )
    
    @classmethod
    def from_input(cls):
        ISBN = val.valid_vazio("ISBN do Livro")
        if ISBN in cls._by_ISBN:
            raise ValueError(f"Livro com ISBN {ISBN} já existe.")
        Titulo = val.valid_vazio("Título do Livro")
        idioma = val.valid_vazio("Idioma do Livro")
        tipo = []
        tema = []
        while True:
            novo_tipo = input("Adicionar tipo (deixar vazio para nenhum): ").strip()
            if not novo_tipo:
                break
            tipo.append(novo_tipo)
        while True:
            novo_tema = input("Adicionar contacto (ou deixar vazio para terminar): ").strip()
            if not novo_tema:
                break
            tema.append(novo_tema)
        data_publicacao = val.valid_date("Data de Publicação do Livro") 
        editora = None
        return cls._create_unique(ISBN, Titulo, idioma, tipo, tema, data_publicacao, editora, "disponivel")

# Descritores
    def __str__(self):
        if self.__editora is not None:
            return f"Livro: {self.__Titulo}, com ISBN: {self.__ISBN}, \n" \
                   f"editado a {self.__data_publicacao} por {self.__editora.get_nome()}, em {self.__idioma}"
        else:
            return f"Livro: {self.__Titulo}, com ISBN: {self.__ISBN}, \n" \
                   f"editado a {self.__data_publicacao}, em {self.__idioma}"
        
# Propriedades: Setters, Getters e Deleters (nenhum definifo)
    @property
    def Titulo(self):
        return self.__Titulo
    @Titulo.setter
    def Titulo(self, titulo):
        self.__Titulo = titulo

    @property
    def ISBN(self):
        return self.__ISBN   
    @ISBN.setter
    def ISBN(self, isbn):
        self.__ISBN = isbn

    @property
    def Editora(self):
        return self.__editora
    @Editora.setter
    def Editora(self, editora):
        self.__editora = editora

    @property
    def Data_Publicacao(self):
        return self.__data_publicacao   
    @Data_Publicacao.setter
    def Data_Publicacao(self, data_publicacao):
        self.__data_publicacao = data_publicacao

    @property
    def Idioma(self):
        return self.__idioma    
    @Idioma.setter
    def Idioma(self, idioma):
        self.__idioma = idioma

    @property
    def Tipo(self):
        return self.__tipo  
    @Tipo.setter
    def Tipo(self, tipo):
        self.__tipo = tipo

    @property
    def Tema(self):
        return self.__tema  
    @Tema.setter
    def Tema(self, tema):
        self.__tema = tema

    @property
    def Disponivel(self):
        return self.__disponivel

    @Disponivel.setter
    def Disponivel(self, disponivel: str):
        self.__disponivel = disponivel

# Métodos adicionais da classe
    def adicionar_tipo(self, tipo):
        if tipo not in self.__tipo:
            self.__tipo.append(tipo)

    def adicionar_tema(self, tema):
        if tema not in self.__tema:
            self.__tema.append(tema)
