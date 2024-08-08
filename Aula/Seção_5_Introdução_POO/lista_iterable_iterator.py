
from collections.abc import Sequence
from typing import Iterator

from pandas import value_counts


class MyList(Sequence):
  def __init__(self):
    self._data = {}
    self._index = 0
    self._next_index = 0
    
  def append(self, *values):
    for values in values:
      self._data[self._index] = values
      self._index += 1
    
  def __len__(self) -> int:
    return self._index
  
  def __getitem__(self, index):
    return self._data[index]
  
  def __setitem__(self, index, values):
    self._data[index] = values
  
  def __iter__(self):
    return self
  
  def __next__(self):
    if self._next_index >= self._index:
      self._next_index = 0
      raise StopIteration
    
    values = self._data[self._next_index]
    self._next_index += 1
    return values

    
if __name__ == '__main__':
  lista = MyList()
  lista.append('Maria', 'Human')
  lista[0] = 'João'
  lista.append('Vanessa')
  # print(len(lista))
  for item in lista:
   print(item)