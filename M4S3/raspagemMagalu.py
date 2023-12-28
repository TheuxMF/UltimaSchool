'''codigo para acessar o site da magazile luiza e extrair dados
o intuito dele é acessar o link de todas as categorias contidas na aba 'todos os departamentos'
em cada categoria pegar nome do produto, valor e o link para o produto de todos os produtos da primeira pagina
por fim adicionar tudo em uma lista de dicionarios e mandar para um banco de dados'''
import sqlite3
from requests_html import HTMLSession

#url que sera acessada
url = 'https://www.magazineluiza.com.br' 
sessao = HTMLSession()
site = sessao.get(url)

#lista que vai armazenar todos os dados
produtos =[]

#acessando todos os links contidos na classe .hnUCVe
for link in site.html.find('.hnUCVe li a'):
    
    #decidindo ponto de parada
    if link.text == "Consórcio Magalu":
        break
    
    #link da categoria que esta sendo acessada no momento
    print(link.attrs['href'])
    respostaLink = sessao.get(link.attrs['href'])

    #pegando as urls de cada produto
    enderecos =respostaLink.html.find('.hmLryf a')
    #pegando o nome de cada produto
    nomeProdutos = respostaLink.html.find('.hmLryf h2')
    #pegando o valor de cada produto
    valores = respostaLink.html.find(".hmLryf .ryZxx p")   

    #adicionando endereco, produto, valor na forma de dicionario na lista produtos 
    for endereco, produto, valor in zip(enderecos, nomeProdutos, valores):
        produtos.append(
            {
                'produto':produto.text,
                'valor':valor.text,
                'endereco': url + endereco.attrs['href']  
            }
        
        )
             
#criando conexao com bando de dados
conexao = sqlite3.connect('M4S3\DBraspagem.sqlite3')
cursor = conexao.cursor()

#comando sql para inserir os dados
sql = 'insert into produtos (nomeProduto, valorProduto, urlProduto) values (?, ?, ?)'


for itens in produtos:
    valores = [itens['produto'], itens['valor'], itens['endereco']]
    cursor.execute(sql ,valores )
    
    
conexao.commit()
conexao.close()

