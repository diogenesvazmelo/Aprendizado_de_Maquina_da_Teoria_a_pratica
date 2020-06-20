def add(a,b):
  """
  Realiza a soma de dois numeros
  @author: Diógenes Vaz de Melo
  """
  return a+b

def maior(a,b):
  """
  Verifica, entre dois números, qual é o maior
  @author: Diógenes Vaz de Melo
  """
  if a > b:
    return a
  else:
      return b

def soma(lista,x=0):
  """
  retorna o somatório dos valores passados pela lista.
  O argumento x deve é opcional, se passado será somado ao resultado final.
  @author: Diógenes Vaz de Melo
  """
  lista.append(x)
  return sum(lista)

def media(lista):
  """
  Retorna a média dos valores passados pela lista.
  @author: Diógenes Vaz de Melo
  """
  import statistics
  return statistics.mean(lista)

def valores_iguais(lista1,lista2):
  """
  Retorna uma lista contendo os valores iguais entre as duas listas passadas como parâmetro
  @author: Diógenes Vaz de Melo
  """
  return list(set(lista1).intersection(lista2))

def indice_prim_valor_igual(lista1,lista2):
  """
  Retorna a posição na lista1 do primeiro valor igual ao da lista2.
  Caso não exista, é retornado None.
  @author: Diógenes Vaz de Melo
  """
  temp = set(lista2)
  lista3 = [idx for idx, value in enumerate(lista1) if value in temp]
  if len(lista3) > 0:
      return lista3[0]
  else:
      return None

if __name__ == "__main__":
  lista1 = [4, 2, 0, 10]
  lista2 = [5, 6, 3, 5]
  x = indice_prim_valor_igual(lista1, lista2)
  print(x)

