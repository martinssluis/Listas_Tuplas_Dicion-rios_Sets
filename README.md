# Coleções em Python: Lista, Tupla, Dicionário e Conjunto

Este projeto demonstra como usar e entender as coleções em Python, que são estruturas de dados que podem armazenar múltiplos itens. As coleções usadas neste código são:

1. **Lista**
2. **Tupla**
3. **Dicionário**
4. **Conjunto (Set)**

## Objetivo

O objetivo deste código é mostrar como cada tipo de coleção funciona, suas características e como iterar sobre elas. O código imprime exemplos de cada coleção e descreve suas principais características.

## Código

O código segue o formato básico de cada tipo de coleção e demonstra as principais operações:

### Lista

A **lista** é uma coleção ordenada e mutável, ou seja, os itens podem ser alterados após a criação da lista. Ela também permite membros duplicados.

Exemplo de código:

```python
lista = ["Luffy", True, 11, 0.65]
```
Ordenada: A ordem dos itens é preservada.
Mutável: Você pode modificar, adicionar ou remover itens da lista.
Permite duplicados: Itens repetidos podem ser armazenados.

### Tupla
A tupla é semelhante à lista, mas é imutável. Após ser criada, seus itens não podem ser modificados. Ela também permite duplicação de itens.

Exemplo de código:

```python
tupla = ("Zoro", True, 11, 0.65)
```

Ordenada: A ordem dos itens é preservada.
Imutável: Não é possível alterar os itens após a criação.
Permite duplicados: Assim como as listas, as tuplas permitem a duplicação de valores.

### Dicionário
O dicionário é uma coleção não ordenada, mas mutável. Ele armazena pares de chave-valor, onde as chaves são únicas, mas os valores podem ser duplicados.

Exemplo de código:

```python
dicionario = {
    "nome": "Sanji",
    "Booleano": True,
    "Inteiro": 11,
    "Float": 0.65
}
```
Não ordenado: Não há garantia de que a ordem dos itens será mantida.
Mutável: Os itens podem ser modificados, adicionados ou removidos.
Chaves únicas: As chaves não podem ser duplicadas, mas os valores podem.

### Conjunto (Set)
O conjunto é uma coleção não ordenada, não indexada e sem membros duplicados. Ele é usado quando a ordem dos itens não importa e duplicatas não são permitidas.

Exemplo de código:

```python
conjunto = {"Nami", True, 11, 0.65}
```
Não ordenado e não indexado: Os itens não têm uma posição fixa e não podem ser acessados por um índice.
Sem duplicados: Um conjunto não permite elementos duplicados.
Mutável: Apesar de ser não ordenado, você pode adicionar e remover itens do conjunto.

## Resumo
Cada tipo de coleção tem seu próprio conjunto de características e é útil para diferentes casos de uso. A escolha da coleção depende de requisitos como a necessidade de mutabilidade, ordenação ou a presença de duplicados.

Este código exemplifica como usar e iterar sobre essas coleções, permitindo uma compreensão melhor sobre como elas funcionam em Python.


### Lista
As listas em Python são coleções ordenadas e mutáveis, ou seja, a ordem dos itens é mantida e você pode adicionar, remover ou alterar elementos. As listas são úteis quando você precisa de uma sequência de elementos que pode ser modificada ao longo do tempo. Além disso, elas permitem itens duplicados.

### Tupla
As tuplas são semelhantes às listas, mas são imutáveis. Isso significa que, uma vez criados, os itens de uma tupla não podem ser alterados. A imutabilidade faz com que as tuplas sejam mais eficientes em termos de desempenho e sejam usadas quando você precisa de uma sequência de dados que não deve ser modificada.

### Dicionário
Dicionários são coleções de pares chave-valor. Ao contrário de listas e tuplas, que são indexadas por posição, os itens de um dicionário são acessados usando uma chave única. Dicionários são mutáveis, permitindo adicionar, modificar ou remover elementos. No entanto, as chaves em um dicionário são únicas e não podem ser duplicadas.

### Conjunto (Set)
Os conjuntos são coleções não ordenadas e não indexadas, o que significa que a ordem dos itens não é garantida. Eles são usados quando você precisa garantir que todos os elementos em uma coleção sejam únicos. Além disso, conjuntos são mutáveis e permitem adicionar ou remover itens, mas não permitem elementos duplicados.