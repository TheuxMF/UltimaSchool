import requests as re

class VolksWagen:
    def __init__(self):
        self.data = {}
        self.index=0
        self.nextindex = 0
        
    def add(self, value):
        self.data[self.index]=value
        self.index=self.index+1

    def __iter__(self):
        return self
        
    def __next__(self):
        if self.nextindex >= self.index:
            self.nextindex = 0
            raise StopIteration
        value = self.data[self.nextindex]
        self.nextindex += 1         
        
        return value
    
    def __str__(self):
        return f'{self.__class__.__name__}{self.data}'
    
#importando os dados da api tabela fipe e instaciando um objeto   
marca = VolksWagen()
modelo = re.get("https://parallelum.com.br/fipe/api/v1/carros/marcas/59/modelos").json()

#adicionando valores na class 
for itens in modelo['modelos']:
    marca.add(itens)

#fazendo a iteração
for carros in marca:
    print(carros)
    











