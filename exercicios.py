import json


class exercicio01 :
    print(' -----Exercício 01 -----')
    INDICE = 13
    soma =0 
    k=0

    for k in range (0, INDICE):
        soma+=k
        
    print(f'Resposta: {soma}')

class exercicio02:
    print()
    print(' -----Exercício 02 -----')
    n=int(input("Informe um valor para verificar se está em Fibonacci: "))
    presente=False

    
    anterior=0
    atual=1
    posterior=anterior+atual
        

    while(posterior<=n):
    
        if(posterior==n):
            presente=True
            break
            
        anterior=atual
        atual=posterior
        posterior=anterior+atual     
        
    
    resultado ='Está na sequencia!!!'if presente else 'Não está na sequência...'
    print(resultado)

class exercicio03:
    print()
    print(' -----Exercício 03 -----')
    with open(f'Exercicios\dados.json') as arquivo:
        dados_faturamento=json.load(arquivo)

    #Calcular a media mensal
    quantidade_valores=0
    soma=0
    for i in dados_faturamento:
        if(i['valor']!=0):
            quantidade_valores+=1
            soma+=i['valor']
    media_mensal= soma/quantidade_valores
    print(f'Média mensal de faturamento: {media_mensal:.2f}')

    #Calcular maior, menor e quantidade de dias
    maior_valor=1
    menor_valor=99999999
    qtd_dias_superior_media=0
    for j in dados_faturamento:
        if(j['valor']!=0):
            if(j['valor']>maior_valor): maior_valor=j['valor']
            if(j['valor']<menor_valor): menor_valor=j['valor']
            if(j['valor']>media_mensal): qtd_dias_superior_media+=1

    print(f'Quantidade de dias que o valor de faturemento foi superior a média mensal: {qtd_dias_superior_media:.2f}')
    print(f'O menor valor de faturamento diário foi de: {menor_valor:.2f}')
    print(f'O maior valor de faturamento diário foi de: {maior_valor:.2f}')

class exercicio04:
    print()
    print(' -----Exercício 04 -----')
    #Usando uma tupla para declarar os valores de cada cidade
    faturamento = [('São Paulo', (67836.43)),('Rio de Janeiro', (36678.66)),('Minas Gerais', (29229.88)), ('Espírito Santo', (27165.48)),('Outros Estados', (19849.53))]

    #Calcular valor total de todos os estados
    valor_total=0
    for estado, fat in faturamento:
        valor_total+=fat
    print(f'Valor total de faturamento: {valor_total:.2f}')
    

    #Calcular qual é a representação do estado no total
    for estado,fat in faturamento:
        porcentagem_fat=(fat*100)/valor_total
        representa=(f'{estado} representa {porcentagem_fat:.2f}% do faturamento total') if estado!='Outros Estados' else (f'{estado} representam {porcentagem_fat:.2f}% do faturamento total')
        print(representa)

class exercicio05:
    print()
    print(' -----Exercício 05 -----')
    frase=input('Informe a frase que vai ser invertida:  ')
    #Colocando as letras da frase num vetor
    letras_da_frase=[]
    for i in frase:
        letras_da_frase.append(i)
    
    #Colocando as letras do vetor numa variável
    frase_invertida=''
    #Rodando o for de trás pra frente (Seria mais fácil em C# e Java rsrs)
    for j in range(len(letras_da_frase)-1,-1,-1):
        frase_invertida+=letras_da_frase[j]

    
    print(f'Frase Invertida: {frase_invertida}')
    