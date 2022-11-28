"""
Estruturas condiconais
if, else, elif


"""

idade = 20

"""
# Estrutura condicional if, em C

if(idade < 18){
    printf('Menor de idade');
}else if(idade == 18){
    pritf('Tem 18 anos');
}else{
    print('É menor de idade');
}
    
"""

"""
# Estrutura condicional if, else em java

if(idade < 18){
    System.out.println('Menor de idade');
}else if(idade == 18){
    System.out.println('Tem 18 anos');
}else{
    System.out.println('É menor de idade');
}
"""

if idade < 18:
    print('Menor de idade')
elif idade == 18:
    print('Tem 18 anos')
elif idade == 26:
    print('Tem 26 anos')
else:
    print('Maior de idade')


