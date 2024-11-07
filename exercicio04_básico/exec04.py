
#apresentador de notas
lista = []


    
nota_01 = int(input('Adicione sua primeira nota: '))
nota_02 = int(input('apresente sua segunda nota: '))
nota_03 = int(input('apresente sua terceira nota: '))
nota_04 = int(input('apresente sua quarta nota: '))
        
        
def media_nota():
    res = (nota_01 + nota_02 + nota_03 + nota_04) /4
        
    if res >= 6 :
        print('Você está aprovado!')
        lista.append(f'Nota final: {res}')
        print(lista)
    
    elif res <= 5:
        print('você está reprovado')
        lista.append(f'sua nota de reprovado: {res}')
        print(lista)
        
    else:
        print('digite um valor correto!')
        
media_nota()


    