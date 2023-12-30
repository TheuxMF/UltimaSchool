'''Um freelancer está com dificuldade para calcular qual valor cobrar por um projeto que está estimado em 80 horas.
Após pensar e revisitar o preço de alguns projetos que cobrou no passado, ele montou a seguinte fórmula: 
valor inicial + quantidade de horas estimadas * valor da hora + 15% do valor calculado. 
Crie um programa que faça essa conta para o freelancer. Considere que o valor inicial sempre será R$ 1000,00 
e o valor da hora cobrada é de R$ 20,45. A aplicação deve imprimir o valor calculado pelo projeto considerando 
duas casas decimais na formatação do valor. Dica: Preste atenção na ordem que as operações da fórmula devem ser 
realizadas.
'''
PORCENTAGEM = 0.15
valorInicial = 1000
quantidadeHoras = 80
valorHora = 20.45

valorCalculado = valorInicial + quantidadeHoras * valorHora
valorFinal= valorCalculado+(valorCalculado*PORCENTAGEM)

print("valor final {:.2f}".format(valorFinal))

