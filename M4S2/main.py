def printar(func):
    def interno(capital, taxa, tempo):   
        print(f"capital R${capital}, taxa {taxa}%, tempo {tempo}")
        func(capital,taxa, tempo)
    return interno
        
@printar
def juros_simples(capital, taxa, tempo):
    juros = capital * (taxa/100) * tempo
    print(juros)



taxa=float(input("Digite a porcentagem :"))
tempo=int(input("digite o tempo de aplicacao :"))
capital = float(input("digite o Capital R$ "))
juros_simples(capital, taxa, tempo)