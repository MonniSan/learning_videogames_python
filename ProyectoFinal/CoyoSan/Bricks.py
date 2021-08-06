from random import random

# Clase Padre 
class CrytoBlock:
  def __init_(self,line,floor,cryptos):
    super().__init__(line, floor, cryptos)
    self.__line = line
    self.__floor = floor
    self.__cryptos = cryptos
  
  """
  methods:
  get random floors and lines and cryptos 
  move down 
  went to blockchain (delete block when they have 0 cryptos)
  touch floor 1 (bottom is GAME OVER)
  """

# Clase Hija
class UsdtBlock(CrytoBlock):
  MIN_CRYPTO = 10
  MAX_CRYPTO = 50

# Clase Hija
class BtcBlock(CrytoBlock):
  MIN_CRYPTO = 100
  MAX_CRYPTO = 200
  
# Clase Hija
class EthBlock(CrytoBlock):
  MIN_CRYPTO = 60
  MAX_CRYPTO = 80
  
# Clase Hija
class DogeBlock(CrytoBlock):
  MIN_CRYPTO = 5
  MAX_CRYPTO = 35
