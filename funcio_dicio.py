funcionarios =[ {'100':{'nome':'Pedro',
                        'idade':25,
                        'cargo':'TI',
                        'salario':3200.00},
                    '101':{'nome':'Lucas',
                        'idade':43,
                        'cargo':'Gerente-Geral',
                        'salario':9000.00}, 
                        
                    '102':{'nome':'Carol',
                        'idade':37,
                        'cargo':'Chefe Marketing',
                        'salario':8600.00},

                    '103':{'nome':'Julia',
                        'idade':28,
                        'cargo':'TI',
                        'salario':4500.00}} 
                ]

def chamar():
    for f in funcionarios:
            for chave, valor in f.items():
                 print(f'matricula: {chave}')
                 print(f"nome: {valor['nome']} - Cargo: {valor['cargo']}")
                 '''
                 ou

                for funcionario in funcionarios:
                    for chave in funcionarios.keys():
                        print(f'matricula: {chave}')
                        print(f"nome: {funcionario[chave]['nome']} - Cargo: {funcionario[chave]['cargo']}")
                 '''

def media_salal():
    soma_salal = 0
    for funcionario in funcionarios:
         for chave in funcionario.keys():
              soma_salal += funcionario[chave]['salario']
    print(f'média salarial: {soma_salal/len(funcionarios)}')

def mais_5k():
     for f in funcionarios:
          for chave, valor in f.items():
               if valor['salario'] > 5000.00:
                    print(f"nome: {valor['nome']}")

     
    
while True:
    print('Mercadinho Big-Bom_Enterprises'
            '\noq desejas fazer?'
            '\n\n 1 - empregados'
            '\n 2 - media salarial'
            '\n 3 - Funcionarios com mais de 5k'
            '\n 4 - sair')
    X = input('diz ae: ')

    if X == '1':
        chamar()
    
    elif X == '2':
        media_salal()
    
    elif X == '3':
         mais_5k()
    
    else:
        break
         
    


