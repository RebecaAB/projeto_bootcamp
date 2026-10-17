
# Dicionário 
agenda_pessoas = {
    "1": {
        "nome": "Ana Silva",
        "data_nascimento": "15/05/2005",
        "categoria": "Família",
        "notificacao": True
    },
    "2": {
        "nome": "Carlos Souza",
        "data_nascimento": "22/10/2008",
        "categoria": "Professor",
        "notificacao": False
    }
}

import os
#=============================================
def f_listar(v_lista):
    # print das pesoas presnetes na lista
    os.system('cls')
    print('=== LISTAR PESSOAS ===')
    for id_pessso, dados in v_lista.items():
        print('-------------')
        print(f'Nome: {dados['nome']}')
        print(f'Categoria: {dados['categoria']}')
        print(f'Data de Nascimento: {dados['data_nascimento']}')
        print(f'Notificação: {dados['notificacao']}') 

    input('\nPressione Enter para continuar...')
    os.system('cls')

#============================================
def f_buscar():
    # busca pelas chaves do dicionário
    os.system('cls')
    print('=== BUSCAR PESSOA ===')
    print('[nome] [data] [categoria]')
    v_busca = input('Buscar por: ').lower().strip()
    
    # Permite aceitar apenas 'data' para além de 'data_nascimento'
    if v_busca == 'data':
        v_busca = 'data_nascimento'

    if v_busca not in ['nome', 'data_nascimento', 'categoria']:
        print('Critério de busca inválido!')
        input('Pressione Enter para continuar...')
        os.system('cls')
        return

    encontrada = False
    print('-----------------')

    # NOME BUSCAR[cite: 1]
    if v_busca == 'nome':
        nome_pessoa = input('Informe o nome: ').strip().lower()
        for id_pessoa, dados in agenda_pessoas.items():
            if nome_pessoa in dados['nome'].lower():
                print(f"Nome: {dados['nome']}")
                print(f"Categoria: {dados['categoria']}")
                print(f"Data de Nascimento: {dados['data_nascimento']}")
                print(f"Notificação: {dados['notificacao']}")
                print('-----------------')
                encontrada = True
        
        if not encontrada:
            print(f'Nenhum registo encontrado com o nome "{nome_pessoa}".')

    # DATA BUSCAR[cite: 1]
    elif v_busca == 'data_nascimento':
        print('Buscar por data 00/00/0000')
        print('Pode ser informado por parte (dia, mês ou ano)')
        data_pessoa = input('Informe a busca: ').strip()
        partes_busca = data_pessoa.split('/')

        for id_pessoa, dados in agenda_pessoas.items():
            data_nascimento = dados['data_nascimento']
            partes_nasc = data_nascimento.split('/') 
    
            # Apenas um valor - busca por dia, mês ou ano
            if len(partes_busca) == 1:
                termo = partes_busca[0]
                if termo in partes_nasc:
                    print(f"Nome: {dados['nome']} | Data: {data_nascimento} | Categoria: {dados['categoria']}")
                    encontrada = True
                
            # Dois valores - dia + mês
            elif len(partes_busca) == 2:
                dia_busca = partes_busca[0]
                mes_busca = partes_busca[1]
                if partes_nasc[0] == dia_busca and partes_nasc[1] == mes_busca:
                    print(f"ID: {id_pessoa} | Nome: {dados['nome']} | Data: {data_nascimento} | Categoria: {dados['categoria']}")
                    encontrada = True

            # Data completa é informada
            elif len(partes_busca) == 3:
                if data_nascimento == data_pessoa:
                    print(f"Nome: {dados['nome']} | Data: {data_nascimento} | Categoria: {dados['categoria']}")
                    encontrada = True

        if not encontrada:
            print('Nenhuma pessoa encontrada com essa data.')

    # CATEGORIA BUSCAR[cite: 1]
    elif v_busca == 'categoria':
        categorias_unidade = set()
        for dados in agenda_pessoas.values(): # Corrigido de .valores() para .values()[cite: 1]
            if 'categoria' in dados:
                categorias_unidade.add(dados['categoria'])
                
        print('Categorias disponíveis:')
        for cada in categorias_unidade: 
            print(f'- {cada}')
            
        categoria_pessoa = input('Informe a categoria da busca: ').strip().lower()
        print('-----------------')
        
        for id_pessoa, dados in agenda_pessoas.items():
            if dados['categoria'].lower() == categoria_pessoa:
                print(f"Nome: {dados['nome']} | Data: {dados['data_nascimento']} | Categoria: {dados['categoria']}")
                encontrada = True
                
        if not encontrada:
            print('Nenhuma pessoa encontrada nessa categoria.')

    input('\nPressione Enter para continuar...')
    os.system('cls')

#========================================           
def f_adicionar():
    os.system('cls')
    print('=== ADICIONAR NOVA PESSOA ===')
    nome = input('Informe o nome: ').strip()
    if not nome:
        print('O nome não pode estar vazio!')
        input('\nPressione Enter para continuar...')
        os.system('cls')
        return

    data_nascimento = input('Informe a data de nascimento (DD/MM/AAAA): ').strip()
    # Validação simples do formato da data
    if len(data_nascimento) != 10 or data_nascimento[2] != '/' or data_nascimento[5] != '/':
        print('Formato de data inválido! Utilize DD/MM/AAAA.')
        input('\nPressione Enter para continuar...')
        os.system('cls')
        return

    categoria = input('Informe a categoria (ex: Família, Professor, Amigos): ').strip()
    if not categoria:
        categoria = 'Geral'

    notificacao_input = input('Ativar notificação? (S/N): ').strip().upper()
    if notificacao_input == 'S':
        notificacao = True
    else:
        notificacao = False

    # Gerar um ID automático único com base nas chaves existentes
    if agenda_pessoas:
        novo_id = str(max([int(k) for k in agenda_pessoas.keys()]) + 1)
    else:
        novo_id = "1"

    # Adicionar ao dicionário principal
    agenda_pessoas[novo_id] = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "categoria": categoria,
        "notificacao": notificacao
    }

    print(f'\nPessoa "{nome}" adicionada com sucesso! (ID atribuído: {novo_id})')
    input('Pressione Enter para continuar...')
    os.system('cls')

#=========================
def f_excluir():
    os.system('cls')
    print('=== EXCLUIR PESSOA ===')
    if not agenda_pessoas:
        print('A agenda está vazia. Não há registos para excluir.')
        input('\nPressione Enter para continuar...')
        os.system('cls')
        return

    print('Deseja procurar o registo a excluir por:')
    print('[1] - ID')
    print('[2] - Nome')
    opcao = input('- ').strip()

    id_para_remover = None

    if opcao == '1':
        id_input = input('Informe o ID do registo: ').strip()
        if id_input in agenda_pessoas:
            id_para_remover = id_input
        else:
            print('ID não encontrado.')

    elif opcao == '2':
        nome_busca = input('Informe o nome (ou parte dele): ').strip().lower()
        correspondencias = []
        for id_p, dados in agenda_pessoas.items():
            if nome_busca in dados['nome'].lower():
                correspondencias.append((id_p, dados['nome']))

        if not correspondencias:
            print('Nenhum registo encontrado com esse nome.')
        elif len(correspondencias) == 1:
            id_para_remover = correspondencias[0][0]
            print(f'Encontrado: ID {id_para_remover} - {correspondencias[0][1]}')
        else:
            print('\nMúltiplos registos encontrados:')
            for id_p, nome_p in correspondencias:
                print(f"ID: {id_p} | Nome: {nome_p}")
            id_para_remover = input('Informe o ID exato da pessoa que deseja excluir: ').strip()
            if id_para_remover not in [item[0] for item in correspondencias]:
                print('ID inválido.')
                id_para_remover = None
    else:
        print('Opção inválida.')

    # Se encontrarmos um ID válido, confirmamos e excluímos
    if id_para_remover:
        pessoa_removida = agenda_pessoas[id_para_remover]['nome']
        confirmacao = input(f'Tem certeza que deseja excluir "{pessoa_removida}"? (S/N): ').strip().upper()
        if confirmacao == 'S':
            del agenda_pessoas[id_para_remover]
            print(f'\nRegisto de "{pessoa_removida}" excluído com sucesso!')
        else:
            print('\nOperação cancelada.')

    input('\nPressione Enter para continuar...')
    os.system('cls')


rodar= True
while rodar == True:
    print('=== AGENDA DE ANIVERSÁRIOS ===')
    print('Ben-vindo a agenda de aniversários')
    print('O que deseja fazer:')
    print('[1] - listar')
    print('[2] - buscar')
    print('[3] - adicionar')
    print('[4] - excluir')
    print('[0] - sair')

    try:
        acao = int(input('- '))
        if acao == 1:
            f_listar(agenda_pessoas)
        
        elif acao == 2:
            f_buscar()
        
        elif acao == 3:
            f_adicionar()
        
        elif acao == 4:
            f_excluir()
        
        elif acao == 0:
                print('=== SISTEMA FECHADO ===')
                break
        else: 
            print('Ação não comportada, tente novamente')
            continue
    

    except ValueError:
        os.system('cls')
        print('Entrada inválida! Digite apenas números.')
        continue
    
