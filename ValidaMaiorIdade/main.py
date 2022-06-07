class Pessoa:

# Metodo construtor
    def __init__(self, Nome, Idade):
    #def _init_(self, Nome, Idade):
        self.Nome = Nome
        self.Idade = Idade

    def Boas_Vindas(self):
        print("Olá seja bem vindo", self.Nome)

    def Recusado(self):
        print("Seu acesso foi recusado!")

# Função
    def Maior_Idade(self):

        if self.Idade >= 18:
            print("Usuario maior de idade")
            self.Boas_Vindas()
        else:
            print("Usuário é menor de idade")
            self.Recusado()


Dados = Pessoa("Renato", 20)

Dados.Maior_Idade()