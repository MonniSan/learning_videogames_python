from World import WEIGHT, HIGHT


# Create Class 
class LedgerBullet:
  px = WEIGHT/2
  py = 30
  
  def __init__(self,px,vx,py,vy,angle,power):
    super().__init__(px,py,angle,power) 
    self.__px = px
    self.__py = py
    self.__angle = angle
    self.__power = power

"""
methods:
get randoms floors and lines
cruch to add cryptos to wallet, 
break blocks at the left and right position,
break blocks at the top and bottom position,
break blocks at the left and right and top and bottom position, 
add a new ledger, 
get double crypto with one crush
"""