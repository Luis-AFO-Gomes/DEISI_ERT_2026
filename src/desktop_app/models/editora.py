class Editora:
    __nipc: str
    __nome: str
    __morada: str
    __contactos: list = []

    def __init__(self, nipc, nome, morada, contacto):
        self.__nipc = nipc
        self.__nome = nome
        self.__morada = morada
        self.__contactos.append(contacto)

    def get_id(self):
        return self.__nipc

    def set_id(self, id):
        self.__nipc = id

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_morada(self):
        return self.__morada

    def set_morada(self, morada):
        self.__morada = morada

# Getters e Setters para contactos
# Note-se que a função varia do sintaxe usual de getters e setters
# devolvendo um string formatada no getter e adicionando um contacto no setter em vez da atribuição simples
    def get_contactos(self):
        return f"{', '.join(map(str, self.__contactos))}"
    
    def set_contactos(self, contacto):
        self.__contactos.append(contacto)

    def add_contacto(self, contacto):  # Método para adicionar um contacto
        self.set_contactos(contacto)   # chama o setter interno, que tem a mesma função    

    def del_contactos(self):        # Método para eliminar todos os contactos
        self.__contactos.clear()

    def rem_contacto(self, contacto):  # Método para eliminar um contacto específico, se existir
        if contacto in self.__contactos:
            self.__contactos.remove(contacto)

    def __str__(self):
        return f"Editora {self.__nome}, ID: {self.__nipc}, Morada: {self.__morada}"