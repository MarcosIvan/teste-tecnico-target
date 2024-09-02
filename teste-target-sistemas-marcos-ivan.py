def fibo(): #função que verifica se o número digitado pertence à sequência de Fibonacci
    #defino os valores de ant = 0 e atual = 1 pois são os 2 primeiros termos da sequência, e temos que salvar esses valores pra descobrir o próximo
    num = int(input("1- Digite um número inteiro: "))
    ant = 0
    atual = 1

    while True:
        if atual > num and num != 0: #caso o atual tenha extrapolado o valor digitado e seja diferente de 0
            print("O número não pertence à sequência de Fibonacci")
            break
        if atual == num or num == 0: #caso tenha encontrado o valor na sequência de Fibonacci ou o valor digitado seja igual à zero
            print("O número pertence à sequência de Fibonacci")
            break
        aux = atual
        atual += ant
        ant = aux

def letra_a():
    a = input("2- Digite uma palavra: ")
    palavra = str.lower(a) #deixo a palavra em letras minúsculas
    cont_a = 0 #variável para armazenar quantos caracteres 'a' existem na palavra digitada
    for i in range(len(palavra)):
        if palavra[i] == 'a':
            cont_a += 1
    print(cont_a)


fibo()
letra_a()