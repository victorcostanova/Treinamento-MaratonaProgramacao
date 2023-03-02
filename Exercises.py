
def exe2():

    #Inicializar os 2 primeiros numeros
    n1, n2 = 0, 1
    stop = 0

    #Informar o numero de entrada
    n = int(input("Digite um número: "))

    #Caso seja negativo, automaticamente não será reconhecido
    if n < 0:
        print("O número não pertence a sequência")
    #Caso contrário, sera feita a sequencia
    else:
        print("Sequencia de Fibonacci: ")
        #Enquanto não houver condição de parada ira imprimir os numeros
        while stop == 0:
            print(n1)
            next = n1 + n2
            n1 = n2
            n2 = next
            if n1 == n:
                print(n1)
                print("O número pertence a sequência!")
                stop = 1
            elif n1 > n:
                print(n1)
                print("O número não pertence a sequência")
                stop = 1
        
def exe3():
    #Iniciar vetor com os dados oferecidos
    dailyb = [ 22174.1664, 24537.6698, 26139.6134, 0.0, 0.0, 26742.6612, 0.0, 42889.2258, 46251.174, 11191.4722, 0.0, 0.0, 3847.4823, 373.7838, 2659.7563, 48924.2448, 18419.2614, 0.0, 0.0, 35240.1826, 43829.1667, 18235.6852, 4355.0662, 13327.1025, 0.0, 0.0, 25681.8318, 1718.1221, 13220.495, 8414.61]
    #Criar um vetor auxiliar e variaveis utilizadas
    aux = []
    count = 0
    sum = 0

    #Transferir todos os elementos, exceto os 0 para o array auxiliar, e somar todos os elemntos
    for i in dailyb:
        if i != 0.0:
            aux.append(i)
            sum += i
            count += 1

    #Calcular a media dos elementos somados
    media = sum / count
    count = 0
    for x in aux:
        if x > media:
            count += 1

    print("Menor valor de faturamento diário: ", min(aux))
    print("Maior valor de faturamento diário: ", max(aux))
    print("Em", count, "dias o valor de  faturamento diário foi superior à média mensal.")

def exe4():
    #Iniciar os valores em cada variavel

    esSP = 67836.43 
    esRJ = 36678.66
    esMG = 29229.88
    esES = 27165.48
    Outros = 19849.53
    #Somar o total
    Total = (esSP + esRJ + esMG + esES + Outros)
    

    print("Representação que cada estado teve: ")
    pSP = esSP / Total * 100
    print("SP: ", pSP,"%")
    pRJ = esRJ / Total * 100
    print("RJ: ", pRJ,"%")
    pMG = esMG / Total * 100
    print("MG: ", pMG,"%")
    pES = esES / Total * 100
    print("ES: ", pES,"%")
    pOutros = Outros / Total * 100
    print("Outros: ", pOutros,"%")

def exe5():
    #Entrar com uma string
    string = input("String: ")
    #Criar uma string aux, onde será armazenada a string invertida
    straux = ""

    #Percorrer cada elemento da string, e inserir os caracteres á esquerda
    for i in string:
        straux = i + straux 
    
    print("A string invertida é: ", straux)


#Executando os exercícios
print("2)")
exe2()
print("\n")

print("3)")
exe3()
print("\n")

print("4)")
exe4()
print("\n")

print("5)")
exe5()
