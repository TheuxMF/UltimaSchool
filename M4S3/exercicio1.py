import pytest
def porcentagem_desconto(quantidade):
    desconto = 1
    if  quantidade  >=  10  and  quantidade  <=  99 :
        desconto = 0.95
        return desconto
    elif  quantidade  >=  100  and  quantidade  <=  999 :
        desconto = 0.90
        return desconto
    elif  quantidade  >=  1000 :
        desconto  =  0.85
        return desconto

    # No desconto o completo de até 1 é o valor do desconto.
    # Ex: 0,85 tem 15% de desconto. -> 1 - 0,85 = 0,15
    
def valor_normal(preco, quant):
    return preco  *  quant

def valor_descontado(valor_total, porcentagem):
    return valor_total * porcentagem

if  __name__  ==  '__main__' :
    valor_unitario  =  float ( input ( 'Valor unitário do produto: ' ))
    quantidade  =  int ( input ( 'Quantidade: ' ))
    
    desconto=porcentagem_desconto(quantidade)
    
    valor_sem_desconto = valor_normal(valor_unitario, quantidade)
    
    valor_com_desconto  =  valor_descontado(valor_sem_desconto, desconto)
    
    
    print ( f'Valor total sem desconto R${ valor_sem_desconto } ' )
    print ( f'Valor total com desconto R${ valor_com_desconto } ' )    