print ('Informe o primeiro valor; ')
v1 = int(input())
print("Informe o segundo valor: ")
v2 = int(input())
print("Informe o terceiro valor: ")
v3 = int(input())

if v1>=v2 and v1>v3 : maior = v1
if v2>v1 and v2>=v2 : maior = v2
if v3>=v1 and v3>=v2 : maior = v3

print ('Maior: ' , maior) 