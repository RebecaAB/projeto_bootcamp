
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
def f_listar(v_lista):
    # print das pesoas presnetes na lista
    for id_pessso, dados in v_lista.items():
        print('-------------')
        print(f'Nome: {dados['nome']}')
        print(f'Categoria: {dados['categoria']}')
        print(f'Data de Nascimento: {dados['data_nascimento']}')
        print(f'Notificação: {dados['notificacao']}') 

    continar  = input(' ')
    os.system('cls')

def f_buscar():
    # busca pelas chaves do dicionário
    print('[nome] [data de nascimento] [categoria]')
    v_busca = input('Buscar por: ').lower()
    for id_pessoa , dados in agenda_pessoas.items():

        # VERIFICA SE EXISTE
        if v_busca not in dados:
            print('Termo não encontrado')
            break
            fora = input('')
            os.system('cls')

        # NOME BUSCAR
        elif v_busca == 'nome':
            nome_pessoa = input('Informe o nome: ') #tratamento para MAriA
            if dados['nome'] == nome_pessoa:
                print(f'Nome: {dados['nome']}')
                print(f'Categoria: {dados['categoria']}')
                print(f'Data de Nascimento: {dados['data_nascimento']}')
                print(f'Notificação: {dados['notificacao']}') 
            else: 
                print(f'{nome_pessoa} não está salvo')
                break

# ================================
        # DATA BUSCAR
        elif v_busca == 'data_nascimento': #Preciso diminuir esse nome ser aceito apenas 'data'
            print('Buscar por data 00/00/0000 ')
            print('Pode ser infomado por parte')
            data_pessoa = input('Informe a busca: ')
            partes_busca = data_pessoa.split('/')

            encontrada = False 

            for id_pessoa, dados in agenda_pessoas.items():
                data_nascimento = dados['data_nascimento']
                partes_nasc = data_nascimento.split('/') 
        
            # Apenas um valor - bbusccca por dia e mês
            if len(partes_busca) == 1:
                termo = partes_busca[0].strip()
                # Verifica se bate com o dia, com o mês ou com o ano
                if termo in partes_nasc:
                    print('Pessoas encontradas: ')
                    print(f"\nNome: {dados['nome']} | Data: {data_nascimento}")
                    encontrada = True
                
            # Dois valores - dia + mês
            elif len(partes_busca) == 2:
                dia_busca = partes_busca[0]
                mes_busca = partes_busca[1]
            
                if partes_nasc[0] == dia_busca and partes_nasc[1] == mes_busca:
                    print('Pessoas encontradas: ')
                    print(f"\nNome: {dados['nome']} | Data: {data_nascimento}")
                    encontrada= True

        # Data completa é informada
            elif len(partes_busca) == 3:
                if data_nascimento == data_pessoa:
                    print(f"\n[Encontrado] ID: {id_pessoa} | Nome: {dados['nome']} | Data: {data_nascimento}")
                    encontrada= True

# ==================================

        elif v_busca == 'categoria':
            categorias_unidade = set(dados['categoria'])
            for dados in agenda_pessoas.valores():
                if 'categoria' in dados:
                    categorias_unidade.add(dados['categoria'])
            for cada in categorias_unidade: 
                print(f'- {cada}')
            
            categoria_pesssoa = input('informe a categoria da busca: ')
            encontrada = False
            print('Pessoas encontradas: ')
            for id_pessoa, dados in agenda_pessoas.items():
                if dados['categoria'].lower() == categoria_pessoa:
                    print(f"Nome: {dados['nome']} | Data: {dado['data_nascimento']} | Categoria: {dados['categoria']}")
                    encontrada = True
                if not encontrada :
                    print('Nenhuma pessoa encontrada')
            

'''
def f_adicionar:
    pass 

def f_excluir(v_nome):
    pass
'''
rodar= True
while rodar == True:
    print('===================================')
    print('Ben-vindo a agenda de aniversários')
    print('O que deseja fazer:')
    print('[1] - listar')
    print('[2] - buscar')
    print('[3] - adicionar')
    print('[4] - excluir')
    print('[0] - sair')
    acao= int(input('- ')) # tratmento para try - com int
    
    if acao == 1:
        f_listar(agenda_pessoas)

    elif acao == 2:
        f_buscar()

    else: 
        print('ação não comportada, tente novamente')
        continue


