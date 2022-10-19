# Estruturas condicionais
#   if, else, elif
"""
# Exemplos:

Estrutura condicional if, else em C:
if(idade < 18){
    printf("Menor de idade");
}else{
    printf("Maior de idade")
}

Estrutura condicional if, else em java:
if(idade < 18){
    system.out.println("Menor de idade");
}else{
    system.out.println("Maior de idade")
}
"""
idade = float(input('digite sua idade '))

if idade < 18:
    print('Menor de idade')
elif idade == 18:
    print('Tem 18 anos')
else:
    print('Maior de idade')
