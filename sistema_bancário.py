soma = 0
contador_saque = 0
extrato = ''
extrato_saque = ''

while True:
    opcoes = int(input('''
    BANCO PEPÉ 
    
    [1] REALIZAR DEPÓSITO 
    [2] REALIZAR SAQUE 
    [3] MOSTRAR EXTRATO 
    [0] SAIR 
    ---------------------
    Digitar: '''))
    print()
    if opcoes == 1:
        print('DEPÓSITO')
        print(f'Saldo: R${soma}')
        deposito = int(input('Valor de deposito: R$'))
        while deposito < 0:
            deposito = int(input('Deposito deve ser positivo: R$'))

        soma += deposito
        extrato += f'Depósito: + R${deposito}\n'
        
        continue

    if opcoes == 2:
        if contador_saque == 3:
            print('limite de saque atingindo!')
            continue
        if soma == 0:
            print('Sem saldo')
            continue
        
        print('SAQUE')
        print(f'Saldo: R${soma}')
        saque = int(input('Valor de saque (MAX R$500,00): R$'))
        
        while saque > 500:
            saque = int(input('O valor de saque deve ser inferior a R$500: R$'))
        
        while saque > soma:
            saque = int(input)
        soma -= saque
        
        extrato_saque += f'Saque: - R${saque}\n'
        contador_saque += 1
        
    if opcoes == 3:
        print('========EXTRATO=======')
        print(f'{extrato}')
        print(f'{extrato_saque}')
        print(f'Saldo: R${soma}')
        print('=======================')
    
    if opcoes == 0:
        break