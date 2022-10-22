# Módulo Collecitons - Deque

"""
Podemos dizer que o deque é uma lista de alta performace.

"""

from collections import deque

# [1] Criando o deque:

deq = deque('Matheus')
print(deq)

# [2] Adicionado elementos no deque:

deq.append('D')  # Adiciona no final
print(deq)

deq.appendleft('>')  # Adiciona no começo da lista
print(deq)

# [3] Remover elementos no deque:

deq.pop()  # Remove e retorna o último elemento
print(deq)

deq.popleft()  # Remove e retorna o primeiro elemento
print(deq)
