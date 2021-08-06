from World import WEIGHT, HIGHT 


# Clase Padre
class CoyoSan:
  px = WEIGHT/2
  py = 25

  def __init__(self,px, py, walletU, walletB, walletE, walletD, face):
    super().__init__(walletU, walletB, walletE, walletD, face)
    self.__px = px
    self.__py = py
    self.__walletU = walletU
    self.__walletB = walletB 
    self.__walletE = walletE 
    self.__walletD = walletD 
    
"""
Metods:
Add cryptos in their correspondent wallet 
Change face dependig the angle of shoting
Change face depneding the floor of the nearest brick. 
"""