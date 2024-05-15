nome = input("Digite seu nome:");
idade = input("Digite sua idade:");

if (nome == '' and idade == ''):
    print("Desculpe! Você deixou campos vazios");
else: 
    print(f"Seu nome é {nome}");

    print(f"Seu nome {nome} tem {len(nome)} letras");
    
    print(f"Seu nome inverso é: {nome[::-1]}");

    if (' ' in nome):
        print("Seu nome tem espaços");
    else:
        print("Seu não nome tem espaços");

    print(f"A primeira letra do seu nome é: {nome[0]}");

    print(f"A ultima letra do seu nome é: {nome[-1]}");