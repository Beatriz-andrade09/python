print("Hello, world!");

print(12, 15, sep="-", end="#\n");
print(20);

sNome = 'Kiara';
sSobrenome = 'Andrade'
iIdade = 12;
bMaiorIdade = iIdade >= 18;

print("Nome:",  sNome);
print("Sobrenome:", sSobrenome);
print("Maior de idade:", bMaiorIdade);

a = 'A';
b = 'B';
c = 1.11;

print('a={} b={} c={:.1f}'.format(a,b, c));

sLivro = input("Qual é seu livro favorito?");

if (sLivro == 'todas as suas imperfeições') :
    print(sLivro, "é um  ótimo livro!");
elif (sLivro  == 'tarde demais'):
    print(sLivro, "é um ótimo livro. Definitivamente é o mais impactante da CoHo.")
else:
    print(sLivro, "parece ser interessante.");