from random import random 

#Clase Padre
class CryptoPower:
  def _init_(self, line, floor, power):
    super().__init__(line, floor, power)
    self.__line = line
    self.__floor = floor
    self.__power = power
  
  """
  Methods 
  Get random floor and line
  Give power to ledgers bullets depending the Crypto Power in which they collided. 
  Deleted the crypto power once collation. 
  """

#Clase Hija
class VerticalMP(CryptoPower):
  def _init_(self, line, floor, power):
    return super()._init_(line, floor, power)
  
#Clase Hija
class HorizontalMP(CryptoPower):
  def _init_(self, line, floor, power):
    return super()._init_(line, floor, power)
  
#Clase Hija
class CrossMP(CryptoPower):
  def _init_(self, line, floor, power):
    return super()._init_(line, floor, power)
  
#Clase Hija
class ExtraLB(CryptoPower):
  def _init_(self, line, floor, power):
    return super()._init_(line, floor, power)
  
#Clase Hija
class DoubleCrush(CryptoPower):
  def _init_(self, line, floor, power):
    return super()._init_(line, floor, power)
  