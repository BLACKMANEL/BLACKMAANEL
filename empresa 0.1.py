ms = int(input("Quantos meses serao avaliados"))
# aqui eu criei uma variavel ms para usar no comando do for/ digite o numero de quantas vezes ele vai rodar

positivo = []
prejuizo = []
empatado = []
# aqui eu criei 3 caixas vazias, para guarda os meses com, lugro, prejuizo e empatados

mes_maior_lucro = ""
# aqui coloquei pra rodar antes do loop, para guarda o nome do mes_maior_lucro começa vazio para depois rodar com os dados 
maior_lucro = 0
# aqui para guarda o lucro, começando com zero, pos nao esta rodando ainda

maior_prejuizo = 0
mes_menor_lucro = ""

total_lucros = 0 
total_despesas = 0


for num in range(ms):
 meses = (input("Qual mes será analisado?:"))
 # usando o for/ (ms) variavel para rodar a quantidade de vez nescessaria
 receita1 = int(input("Quanto dinheiro entrou?:"))
 despesas1 = int(input("Quanto dinheiro saiu?:"))
 lucro = receita1 - despesas1 
 
 if lucro >0:
  print("Mes com lucro", lucro)
  positivo.append(meses)
 # aqui guarda o mes dentro da lista de positivos
 elif lucro <0 :
  print("Mes com prejuizo", lucro)
  prejuizo.append(meses)
 else:
  print("Mes empatado", lucro) 
  empatado.append(meses)

 if lucro > maior_lucro:
    mes_maior_lucro = meses
    maior_lucro = lucro
 # e aqui ele so atualiza o mes com maior lucro e o maior lucro ate agora

 if lucro < maior_prejuizo:
    maior_prejuizo= lucro
    mes_menor_lucro = meses
 
 total_lucros = total_lucros + lucro
 total_despesas = total_despesas + despesas1

 media = total_lucros / ms
 # aqui vai calcular a media total dos lucros

print("Quantidade de positivos", len(positivo))
print("Positivos:", positivo)

print("Quantidade de prejuizo", len(prejuizo))
print("Prejuizos:", prejuizo)

print("Quantidade de empatados", len(empatado))
print("Empatados:", empatado)
 # aqui mostra o conteudo na lista no final 

print("Maior lucro", maior_lucro)
print("Mes do maior lucro", mes_maior_lucro)

print("Maior prejuizo", maior_prejuizo)
print("Mes do maior prejuizo", mes_menor_lucro)

print(total_lucros)
print("Total media", media)
print("Total de despesas", total_despesas)

if len(positivo) > len(prejuizo):
   print("Em crecimento")
elif len(positivo) == len(prejuizo):
   print("Em estabilidade")
else:
   print("Em crise")
