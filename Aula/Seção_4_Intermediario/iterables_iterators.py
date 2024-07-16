# Interável é um item sequencial que pode acessar coisas sequencialmente
# Iterator a única responsabilidade dele é entragar um valor por vez, é saber qual é o próximo valor

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))