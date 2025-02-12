## Estrutura Básica

A estrutura básica de uma condicional em Python é a seguinte:

```python
if condição:
  # bloco de código executado se a condição for verdadeira
elif outra_condição:
  # bloco de código executado se a outra_condição for verdadeira
else:
  # bloco de código executado se nenhuma das condições anteriores for verdadeira
```

### Exemplo

```python
idade = 18

if idade < 18:
  print("Você é menor de idade.")
elif idade == 18:
  print("Você tem exatamente 18 anos.")
else:
  print("Você é maior de idade.")
```

## Condicionais Aninhadas

Você pode aninhar condicionais dentro de outras condicionais para verificar múltiplas condições:

```python
nota = 85

if nota >= 90:
  print("A")
else:
  if nota >= 80:
    print("B")
  else:
    if nota >= 70:
      print("C")
    else:
      print("D")
```

## Operadores de Comparação

Os operadores de comparação são usados para comparar valores dentro das condicionais:

- `==` : igual a
- `!=` : diferente de
- `>` : maior que
- `<` : menor que
- `>=` : maior ou igual a
- `<=` : menor ou igual a

### Exemplo

```python
a = 10
b = 20

if a == b:
  print("a é igual a b")
elif a != b:
  print("a é diferente de b")
```

## Operadores Lógicos

Os operadores lógicos permitem combinar múltiplas condições:

- `and` : verdadeiro se ambas as condições forem verdadeiras
- `or` : verdadeiro se pelo menos uma das condições for verdadeira
- `not` : inverte o valor lógico da condição

### Exemplo

```python
idade = 25
tem_carteira = True

if idade >= 18 and tem_carteira:
  print("Pode dirigir.")
else:
  print("Não pode dirigir.")
```

## Condicionais Ternárias

As condicionais ternárias são uma forma compacta de escrever uma condicional simples:

```python
idade = 18
status = "maior de idade" if idade >= 18 else "menor de idade"
print(status)
```