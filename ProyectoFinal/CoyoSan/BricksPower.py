from random import random 

#Clase Padre
class CryptoPower:
  def _init_(self, px, py, power):
    super().__init__(px, py, power)
    self.__px = px
    self.__py = py
    self.__power = power
  
  """
  Methods 
  Give power to ledgers depending the Crypto Power in which they collided. 
  Deleted the crypto power once used. 
  """

#Clase Hija
class VerticalMP(CryptoPower):
  def _init_(self, px, py, power):
    return super()._init_(px, py, power)
  
#Clase Hija
class HorizontalMP(CryptoPower):
  def _init_(self, px, py, power):
    return super()._init_(px, py, power)
  
#Clase Hija
class CrossMP(CryptoPower):
  def _init_(self, px, py, power):
    return super()._init_(px, py, power)
  
#Clase Hija
class ExtraLB(CryptoPower):
  def _init_(self, px, py, power):
    return super()._init_(px, py, power)
  
#Clase Hija
class DoubleCrush(CryptoPower):
  def _init_(self, px, py, power):
    return super()._init_(px, py, power)
  