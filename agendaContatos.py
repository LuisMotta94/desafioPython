import re

def adicionar_contato(contatos, nome, telefone, email):
    contato = {
        "Nome":nome,
        "Telefone":telefone,
        "E-mail":email,
        "Favorito":False
    }
    contatos.append(contato)
    
    return

def validar_tefone():
    
    while True:
        telefone = input("Qual telefone: ")
        if telefone.isdigit()==False:
            print("Isso não é um número de telefone")
        else:
            if len(telefone) != 1:
                print("Está faltando alguma coisa no seu numero de telefone")
            else:
                print("Número validado!")
                break
    return telefone

def validar_email():
    regex_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    while True:
        email = input("e por último o E-mail: ")
        if re.match(regex_email,email):
            print("E-email validado")
            break
        else:
            print("E-email inválidado")
    return email

def visualizar_contatos(contatos):
    print("\nSua lista de contatos")

    for indice, contato in enumerate(contatos,start=1):
        favorito = '★' if contato['Favorito'] else "✰"

        nome = contato['Nome']
        telefone = contato['Telefone']
        email = contato['E-mail']

        print(f'{indice}. {favorito} - Nome: {nome} | Telefone: {telefone} | E-mail: {email}')
    return

def editar_contato(contatos, indice_ajustado, info_contato, nova_info):
    contatos[indice_ajustado][info_contato] = nova_info
    print("✓ Contato atualizado sucesso!")
    return

def favoritar_contato(contatos, indice):
    indice_ajustado = int(indice) - 1
    contatos[indice_ajustado]['Favorito'] = True
    print(f"Contato {contatos[indice_ajustado]['Nome']} favoritado ★!")
    return

def desfavoritar_contato(contatos, indice):
    indice_ajustado = int(indice) - 1
    contatos[indice_ajustado]['Favorito'] = False
    print(f"Contato {contatos[indice_ajustado]['Nome']} desfavoritado ✰!")
    return

def visualizar_favoritos(contatos):
    for indice,contato in enumerate(contatos,start=1):
        if contato['Favorito'] == True:
            favorito = '★' if contato['Favorito'] else "✰"
            print(f"{indice}. {favorito} - Nome: {contato['Nome']} | Telefone: {contato['Telefone']} | E-mail: {contato['E-mail']}")
        else:
            print("="*50)
            print("--> Não existe contatos favoritados ★")
            print("="*50)
    return

def deletar_contato(contatos, indice):
    indice_ajustado = int(indice)-1
    contatos.remove(indice_ajustado)
    print("Contato deletado com sucesso!")
    return

contatos = []
while True:
    print("-"*50)
    print("Gerencidor de agenda")
    print("-"*50)

    print("1. Adicionar contato")
    print("2. Visualizar lista de contatos")
    print("3. Editar contato")
    print("4. Favoritar contato")
    print("5. Desfavoritar contato")
    print("6. Ver contatos favoritados")
    print("7. Apagar contatos")
    print("8. Sair")

    escolha = input("\nDigite sua escolha: ")

    if escolha == "1":
        nome = input("Qual nome do contato: ")
        telefone = validar_tefone()
        email = validar_email()        
        adicionar_contato(contatos, nome, telefone, email)
        print("-> Contato adicionado com sucesso!")
        
    elif escolha == "2":
        if len(contatos) != 0:
            visualizar_contatos(contatos)
        else:
            print('\n--> Não existe nenhum contato!')
        
    elif escolha == "3":
        if len(contatos) != 0:
            visualizar_contatos(contatos)

            indice = int(input("\nDigite o indice de contato para você editar: "))
            indice_ajustado = indice - 1
            if indice_ajustado >= 0 and indice_ajustado < len(contatos):
                print(f'Nome: {contatos[indice_ajustado]["Nome"]} \nTelefone: {contatos[indice_ajustado]["Telefone"]} \nEmail: {contatos[indice_ajustado]["E-mail"]}')

                while True:
                    info_editar_contato = input("\nDigite qual informação você quer editar: ")
                    if info_editar_contato not in ['Nome','Telefone','E-email']:
                        print('Informação inválida. Digite informação correta!')
                    else:
                        nova_info = input(f"\nDigite {info_editar_contato} atualizado: ")
                        editar_contato(contatos, indice_ajustado, info_editar_contato,nova_info)
                        break
        else:
            print('\n--> Não existe nenhum contato!')

    elif escolha == "4":
        if len(contatos) != 0:
            visualizar_contatos(contatos)
            indice = input("Digite o número do contato que você quer favoritar ★: ")
            favoritar_contato(contatos, indice)
        else:
            print('\n--> Não existe nenhum contato!')

    elif escolha == "5":
        if len(contatos) != 0:
            visualizar_favoritos(contatos)
            indice = input("Digite o número do contato que você quer favoritar ✰: ")
            desfavoritar_contato(contatos, indice)
        else:
            print('\n--> Não existe nenhum contato!')

    elif escolha == "6":
        if len(contatos) != 0:
            visualizar_favoritos(contatos)
        else:
            print('Não existes contatos!')

    elif escolha == "7":
        if len(contatos) != 0:
            visualizar_contatos(contatos)
            indice = input("Digite o número do contato que você quer remover: ")
            indice_ajustado = int(indice)-1
            contatos.remove(indice_ajustado)
            print("Contato deletado com sucesso!")
        else:
            print('\n--> Não existe nenhum contato para ser apagado!')
        
    elif escolha == "8":
        break