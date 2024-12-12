class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        print(f'\n{'Nome do Restauramte'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}')

    @property
    def ativo (self):
        return 'Ativo' if self._ativo else 'Desativado'




restaurante_outback = Restaurante('Outback','Fast Food',)

restaurante_el_shaday = Restaurante('EL SHADAY','Italiana')

Restaurante.listar_restaurantes()
    
