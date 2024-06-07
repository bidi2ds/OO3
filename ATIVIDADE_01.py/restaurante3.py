#criando uma classe usando decoreitor @proprety

class Restaurante:
    restaurantes=[]
    def __init__(self,nome,categoria):
        self.nome=nome.title()
        self.categoria=categoria.upper()
        self._ativo=False
        Restaurante.restaurantes.append(self)

    def __str__(self):
       # return self.nome
        return f'{self.nome}|{self.categoria}|{self.ativo}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'Nome do Restaurante | Categoria | Status')
        for restaurante in cls.restaurantes:
            print(f'{restaurante.nome.ljust(20)}|{restaurante.categoria.ljust(20)}|{restaurante.ativo}')

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'

restaurante_praca=Restaurante('Praça','Italiana')
restaurante_pizza=Restaurante('Baeti','Mexicana')

# restaurantes=[restaurante_praca,restaurante_pizza]

#print(restaurante_praca.ativo)

# print(dir(restaurante_praca))
# print('')
# print(vars(restaurante_praca))
#print(restaurante_praca)
Restaurante.listar_restaurantes()