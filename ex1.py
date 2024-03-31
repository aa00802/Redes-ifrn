n =  int(input("Digite um número de quatro no máximo algarismo: "))

if n <= 0 :
 print("Esse numero não pode ser transformado")
 
n1 = n % 10
n = n//10
n2 = n % 10
n = n//10
n3 = n % 10
n = n//10
n4 = n 
soma = n1 + n2 + n3 + n4
print(n1)
print(n2)
print(n3)
print(n4)
print(soma)
 