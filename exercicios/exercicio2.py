"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
    - Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
    - Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta, exiba a letra
    - Se a letra digitada não estiver na palavra secreta, exiba *.
    - Faça a contagem de tentativas do seu usuário
"""

serie = "supernatural";
letrasAcertadas = '';
quantidadeTentatidas = 0;

print("Desafio - Advinhe uma série misteriosa  \nDica: O melhor personagem morre por causa de um prego (: \n");

while True:
    letra = input("Digite uma letra para advinhar a série: ");
    if (len(letra) > 1):
        print("Digite uma letra para continuar");
        continue; 
    
    quantidadeTentatidas = quantidadeTentatidas + 1; 
    if (letra in serie):
        print(f"A letra {letra} está na série secreta. Continue ...");
        letrasAcertadas += letra;

    palavraFormada = '';
    for letraSecreta in serie:
        if (letraSecreta in letrasAcertadas):
            palavraFormada += letraSecreta;
        else:
           palavraFormada += "*";
    
    print("\nPalavra formada: ", palavraFormada);
    
    if (palavraFormada == serie):
       print("\nVocê acertou a série secreta com ", quantidadeTentatidas, " tentativas. Parabéns! \nSupernatual é a melhor série! :) ");
       break;